import pandas as pd
from twilio.rest import Client

account_sid = "ACc500f71149771761f37c2c5fcaf9e345"

auth_token  = "aabe5ab217fdecba3f5017a488bd8bb2"

client = Client(account_sid, auth_token)

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês de {mes} o vendedor: {vendedor} atingiu a meta, com o valor de R$:{vendas}.')
        message = client.messages.create(
            to="+5598981426972",
            from_="+12184534490",
            body=f'No mês de {mes} o vendedor: {vendedor}, atingiu a meta e ganhou a viagem, com o valor de R$:{vendas} em vendas!.')
        print(message.sid)



