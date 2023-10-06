import pandas as pd

def main_data():

    data_reason = pd.DataFrame({
        'bot_id': ['Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2'],
        'queue': ['SAC', 'SAC', 'SAC', 'Default', 'Default', 'Vendas', 'Vendas', 'Cobrança', 'Cobrança', 'Cobrança'],
        'reason': ['Quitação do empréstimo', 'Envio de boleto', 'Atualizar informações de contato', 'Alteração da data de vencimento do boleto', 'Cliente não respondeu', 'Quitação do empréstimo', 'Envio de boleto', 'Atualizar informações de contato', 'Alteração da data de vencimento do boleto', 'Cliente não respondeu'],
        'total': [340, 180, 55, 90, 10, 240, 280, 155, 100, 40]
    })

    data_demand = pd.DataFrame({
        'bot_id': ['Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2'],
        'queue': ['SAC', 'SAC', 'SAC', 'Default', 'Default', 'Vendas', 'Vendas', 'Cobrança', 'Cobrança', 'Cobrança'],
        'demand': ['Valor de quitação', 'Gerar boleto de quitação', 'Esclarecer problemas com pagamento', 'Negociar novo acordo', 'Resolver problema com juros e multa', 'Valor de quitação', 'Gerar boleto de quitação', 'Esclarecer problemas com pagamento', 'Negociar novo acordo', 'Resolver problema com juros e multa'],
        'total': [390, 270, 160, 50, 40, 390, 400, 150, 260, 90]
    })

    data_action = pd.DataFrame({
        'bot_id': ['Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2'],
        'queue': ['SAC', 'SAC', 'SAC', 'Default', 'Default', 'Vendas', 'Vendas', 'Cobrança', 'Cobrança', 'Cobrança'],
        'action': ['Enviou o boleto por e-mail', 'Informou forma de pagamento cadastrada', 'Solicitou print da tela de erro', 'Informou como solicitar um empréstimo', 'Informou processo para alterar os dados cadastrais', 'Enviou o boleto por e-mail', 'Informou forma de pagamento cadastrada', 'Solicitou print da tela de erro', 'Informou como solicitar um empréstimo', 'Informou processo para alterar os dados cadastrais'],
        'total': [485, 265, 155, 45, 35, 265, 380, 255, 95, 35]
    })

    data_sentiment = pd.DataFrame({
        'bot_id': ['Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2'],
        'queue': ['SAC', 'SAC', 'SAC', 'Default', 'Default', 'Default', 'Vendas', 'Vendas', 'Vendas', 'Cobrança', 'Cobrança', 'Cobrança'],
        'sentimento': ['Positivo', 'Negativo', 'Neutro', 'Positivo', 'Negativo', 'Neutro', 'Positivo', 'Negativo', 'Neutro', 'Positivo', 'Negativo', 'Neutro'],
        'total': [454, 271, 120, 356, 271, 180, 454, 35, 250, 340, 271, 200]
    })

    data_upsell = pd.DataFrame({
        'bot_id': ['Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2'],
        'queue': ['SAC', 'SAC', 'Default', 'Default', 'Vendas', 'Vendas', 'Cobrança', 'Cobrança'],
        'oportunidade': ['True', 'False', 'True', 'False', 'True', 'False', 'True', 'False'],
        'total': [80, 463, 280, 403, 180, 463, 80, 300]
    })

    ticket_info  = pd.DataFrame({
        'bot_id': ['Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 1', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2', 'Bot 2'],
        'queue': ['SAC', 'Default', 'SAC', 'SAC','Default', 'SAC', 'Default', 'Vendas', 'Vendas', 'Vendas', 'Cobrança', 'Cobrança', 'Cobrança', 'Cobrança'],
        'ticket_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        'user_id': ['55912121212', '55923232323', '55934343434', '55945454545', '55956565656', '55967676767', '55978787878', '55989898989', '55990909090', '55914141414', '55925252525', '55947474747', '55959595959', '55938383838'],
        'sentimento': ['Positivo', 'Positivo', 'Neutro', 'Negativo', 'Negativo', 'Neutro', 'Positivo', 'Negativo', 'Neutro', 'Positivo', 'Negativo', 'Neutro', 'Positivo', 'Positivo'],
        'oportunidade': ['True', 'False', 'True', 'False', 'True', 'True', 'True', 'False', 'True', 'False', 'True', 'False', 'False', 'True']
    })


    return data_reason, data_demand, data_action, data_sentiment, data_upsell, ticket_info
