from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

import requests
import dateutil.parser
from datetime import datetime
from django.utils import timezone
from .models import Moeda
import json
import xmltodict
from .xml_dict import get_json_from_xml
from django.views.decorators.cache import cache_page

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
@cache_page(60 * 30)  # Cache de 30 minutos
def converter_moedas(request):
    """
    API de CoGnversão das Moedas
    API Original: https://www3.bcb.gov.br/bc_moeda/rest/converter/<valor_desejado>/1/<codigo_moeda_origem>/<codigo_moeda_destino>/<data>
    API com Data Ultima Cotação: https://www3.bcb.gov.br/bc_moeda/rest/cotacao/fechamento/ultima/1/<codigo_moeda>/<data>

    :paramGET data_cotacao: Padrão DD/MM/AAAA | Data da Cotação Desejada
    :paramGET moeda_origem: Padrão SWIFT | Código da Moeda de Origem
    :paramGET moeda_destino: Padrão SWIFT | Código da Moeda de Destino
    :paramGET valor_desejado: XXX.XX | Valor desejado para conversão
    :returnJSON valor: XXX.XX | Valor Convertido
    :returnJSON cotacao: DD/MM/YYYY | Data da Cotação que foi possível obter

    Exemplo de Chamada: /?moeda_origem=BRL&moeda_destino=USD&valor_desejado=10&data_cotacao=10/09/2019
    """
    data = dict()
    data_cotacao = request.GET.get('data_cotacao', None)
    moeda_origem = request.GET.get('moeda_origem', None)
    moeda_destino = request.GET.get('moeda_destino', None)
    valor_desejado = request.GET.get('valor_desejado', None)
    if data_cotacao and moeda_origem and moeda_destino and valor_desejado:
        moeda_origem = Moeda.objects.get(moeda_swift=moeda_origem).moeda_codigo
        moeda_destino = Moeda.objects.get(moeda_swift=moeda_destino).moeda_codigo
        data_cotacao = datetime.strptime(data_cotacao, '%d/%m/%Y').replace(tzinfo=timezone.get_current_timezone())
        data_cotacao_str = data_cotacao.strftime('%Y-%m-%d')
        # TODO Validar os argumentos inseridos

        # ---------------------------------------------
        # Temos que verificar primeiro se a data solicitada existe cotação.
        url_data_cotacao = 'https://www3.bcb.gov.br/bc_moeda/rest/cotacao/fechamento/ultima/1/{}/{}'.format(
            moeda_destino,
            data_cotacao_str,
        )
        response = requests.get(url_data_cotacao)
        dados = get_json_from_xml(response.content)
        ultima_cotacao_disponivel = dateutil.parser.parse(dados['cotacao']['data'])
        if data_cotacao > ultima_cotacao_disponivel:
            data_cotacao_str = ultima_cotacao_disponivel.strftime('%Y-%m-%d')
            data_cotacao = ultima_cotacao_disponivel

        # ---------------------------------------------
        # Vamos converter o valor desejado agora
        valor_desejado: str = valor_desejado.replace(',', '.')
        url = 'https://www3.bcb.gov.br/bc_moeda/rest/converter/{}/1/{}/{}/{}'.format(
            valor_desejado,
            moeda_origem,
            moeda_destino,
            data_cotacao_str,
        )
        response = requests.get(url)
        data = get_json_from_xml(response.content)
        data = {
            'valor': data['valor-convertido'],
            'cotacao': data_cotacao.strftime('%d/%m/%Y')
        }
        return Response(data=data)
    else:
        raise ValidationError
