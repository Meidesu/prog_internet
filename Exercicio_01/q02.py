import requests


url = input("Digite a URL: ")

try:
    response =  requests.get(url)

    # Status code
    print(response.status_code)

    # Encoding
    print(response.encoding)

    # Tamanho da resposta
    print(len(response.content))

    # Conteúdo da resposta
    print(response.text)

    # Cabeçalho da resposta
    print(response.headers)

    

except requests.exceptions.RequestException as e:
    print("Erro ao fazer requisição: ", e)