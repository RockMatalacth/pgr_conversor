 # JSON Dolar 
json_data = {  
    "USD": {
        "code": "USD",
        "codein": "BRL",
        "name": "Dólar Americano/Real Brasileiro",
        "high": "4.986",
        "low": "4.9506",
        "varBid": "0.0096",
        "pctChange": "0.19",
        "bid": "4.9785",
        "ask": "4.979",
        "timestamp": "1711040200",
        "create_date": "2024-03-21 13:56:40"
    }
}

# Acessando os valores específicos
name = json_data["USD"]["name"]
high = json_data["USD"]["high"]
low = json_data["USD"]["low"]
varBid = json_data["USD"]["varBid"]
pctChange = json_data["USD"]["pctChange"]
bid = json_data["USD"]["bid"]
ask = json_data["USD"]["ask"]
timestamp = json_data["USD"]["timestamp"]
create_date = json_data["USD"]["create_date"]

# Exibindo os 
print('\nINFORMAÇÕES DO DOLAR')
print("\nNome:", name,
      "\nAlto:", high,
      "\nBaixo:", low,
      "\nVariação de Bid:", varBid,
      "\nMudança percentual:", pctChange,
      "\nBid:", bid,
      "\nAsk:", ask,
      "\nTimestamp:", timestamp,
      "\nData de criação:", create_date,)
