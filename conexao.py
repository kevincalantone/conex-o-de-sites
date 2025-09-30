import requests
x = []

while True:
    site = input("Digite o site para testar conexão (ex: google, facebook, github): ").strip().lower()
    x.append(site)
    url = f"https://www.{site}.com"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(f"{url} está online!")
       
        elif resposta.status_code == 401:
            print(f"{url} requer autenticação (401 Unauthorized).")
        
        elif resposta.status_code == 404:
            print(f"{url} não foi encontrado (404 Not Found).")
       
        else:
            print(f"Erro: {resposta.status_code}")    
   
    except requests.exceptions.ConnectionError:
        print("Erro de conexão: site não encontrado ou indisponível.")
  
    except requests.exceptions.Timeout:
        print("Erro: o tempo de conexão expirou.")
   
    except requests.exceptions.RequestException as e:
        print(f"Erro inesperado: {e}")

    sair = int(input("Deseja insirir mais algum site? [1-sim] e [2-não]: "))
    
    if sair == 2:
        print("Encerrando o teste de conexão!.")
        print(f"Sites digitados: {x} ")
        break

    elif sair == 1:
        print("Ok, continuando...")
        continue
    
    else:
        print("SOMENTE 1 PARA SIM E 2 PARA NÃO")