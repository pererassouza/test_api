import requests
import json


def obter_clima(cidade, chave_api):
    """
    Obtém os dados meteorológicos da cidade especificada usando a API OpenWeatherMap.

    Args:
        cidade (str): Nome da cidade para a qual obter os dados meteorológicos.
        chave_api (str): Chave da API para autenticação.

    Returns:
        dict: Dados meteorológicos da cidade, se a solicitação for bem-sucedida.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def exibir_clima(dados_clima):
    """
    Exibe a descrição do clima e a temperatura atual.

    Args:
        dados_clima (dict): Dados meteorológicos retornados pela API OpenWeatherMap.
    """
    descricao_clima = dados_clima['weather'][0]['description']
    temperatura = dados_clima['main']['temp']
    print(f"Descrição do clima: {descricao_clima.capitalize()}")
    print(f"Temperatura atual: {temperatura}°C")


def main():
    """
    Função principal que coordena a obtenção e exibição dos dados meteorológicos.
    """
    chave_api = "CHAVE API"
    cidade = input("Digite o nome da sua cidade: ")

    try:
        dados_clima = obter_clima(cidade, chave_api)
        exibir_clima(dados_clima)
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro na solicitação: {req_err}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
