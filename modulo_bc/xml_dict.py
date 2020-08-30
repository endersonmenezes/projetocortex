import xmltodict
import json


def get_json_from_xml(xml):
    dados = xmltodict.parse(xml)
    dados = json.dumps(dados)
    dados = json.loads(dados)
    return dados
