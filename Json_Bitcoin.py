#JSON Bitcoin

json_data = {  
    "BTC": {
        "code": "BTC",
        "codein": "BTC",
        "name": "Bitcoin/Dólar American",
        "high": "68280",
        "low": "62884",
        "varBid": "3585",
        "pctChange": "5.68",
        "bid": "66740",
        "ask": "66746",
        "timestamp": "1711040215",
        "create_date": "2024-03-21 13:56:55"
    }
}

# Acessando os valores específicos
name = json_data["BTC"]["name"]
high = json_data["BTC"]["high"]
low = json_data["BTC"]["low"]
varBid = json_data["BTC"]["varBid"]
pctChange = json_data["BTC"]["pctChange"]
bid = json_data["BTC"]["bid"]
ask = json_data["BTC"]["ask"]
timestamp = json_data["BTC"]["timestamp"]
create_date = json_data["BTC"]["create_date"]

# Exibindo os valores
print('\nINFORMAÇÕES DO BITCOIN')
print("\nNome:", name,
      "\nAlto:", high,
      "\nBaixo:", low,
      "\nVariação de Bid:", varBid,
      "\nMudança percentual:", pctChange,
      "\nBid:", bid,
      "\nAsk:", ask,
      "\nTimestamp:", timestamp,
      "\nData de criação:", create_date,)
