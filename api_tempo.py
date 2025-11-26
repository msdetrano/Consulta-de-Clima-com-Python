import requests
import pprint

link_api = "http://api.weatherapi.com/v1/current.json"
api_key = "SUA_CHAVE_DE_API_AQUI"

parametro = {
    "key": api_key,
    "q": "São Paulo",
    "lang": "pt"    
}

response = requests.get(link_api, params=parametro)


if response.status_code == 200:
    dados_requisicao = response.json()
    #pprint.pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    condicao = dados_requisicao["current"]["condition"]["text"]
    print(f"A temperatura em São Paulo é de {temp}°C e o tempo está {condicao}.")
else:
    print("Erro ao consultar a API de clima.")