#  Copyright (c) 2020. Enderson Menezes Cândido [www.endersonmenezes.com.br]
from celery import shared_task


@shared_task(soft_time_limit=1000, time_limit=1000)
def get_moedas_bc():
    """
    Cadastro de Moedas do BC
    ROTA DA API: https://www3.bcb.gov.br/bc_moeda/rest/moeda/data
    DOCUMENTAÇÃO:
    """

    api_rota = 'https://www3.bcb.gov.br/bc_moeda/rest/moeda/data'

