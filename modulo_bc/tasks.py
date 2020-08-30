#  Copyright (c) 2020. Enderson Menezes Cândido [www.endersonmenezes.com.br]
from celery import shared_task
from .models import Moeda
import requests
from .xml_dict import get_json_from_xml


@shared_task(soft_time_limit=1000, time_limit=1000)
def get_moedas_bc():
    """
    Cadastro de Moedas do BC
    ROTA DA API: https://www3.bcb.gov.br/bc_moeda/rest/moeda/data
    DOCUMENTAÇÃO:
    """
    url = 'https://www3.bcb.gov.br/bc_moeda/rest/moeda/data'
    response = requests.get(url)
    dados = get_json_from_xml(response.content)
    dados = dados['moedas']['moeda']
    data_return = {'total_moedas_api': 0,
                   'moedas_novas': 0,
                   'total_moedas_banco_antes': Moeda.objects.all().count()}
    for moeda in dados:
        data_return['total_moedas_api'] += 1
        pais_codigo = moeda['codigoPais']
        pais_nome = moeda['nome']
        moeda_codigo = moeda['codigo']
        moeda_swift = moeda['sigla']
        try:
            Moeda.objects.get(moeda_codigo=moeda_codigo)
        except Moeda.DoesNotExist:
            Moeda.objects.create(pais_codigo=pais_codigo, pais_nome=pais_nome, moeda_swift=moeda_swift, moeda_codigo=moeda_codigo)
            data_return['moedas_novas'] += 1
    data_return['total_moedas_banco_depois'] = Moeda.objects.all().count()
    return data_return
