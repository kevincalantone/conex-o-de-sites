# Teste de Conexão de Sites

Este projeto em Python permite testar se sites estão online ou não, verificando o status HTTP e tratando possíveis erros de conexão. É um exemplo prático de uso de `requests`, loops interativos e manipulação de listas em Python.

---

## Funcionalidades

- Permite ao usuário digitar múltiplos sites para teste.
- Verifica o status HTTP do site (200, 401, 404, outros).
- Trata exceções de conexão, timeout e erros inesperados.
- Armazena todos os sites testados em uma lista.
- Loop interativo para inserir novos sites até o usuário decidir encerrar.

---

## Como usar

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
Entre na pasta do projeto:

bash
Copiar código
cd NOME_DO_REPOSITORIO
Execute o script:

bash
Copiar código
python conexao_google.py
Digite o nome do site quando solicitado (apenas o nome, sem https://www. ou .com).

Escolha se deseja inserir mais sites ou encerrar o programa.

Exemplo de uso
less
Copiar código
Digite o site para testar conexão (ex: google, facebook, github): google
https://www.google.com está online!

Deseja inserir mais algum site? [1-sim] e [2-não]: 1
Digite o site para testar conexão (ex: google, facebook, github): siteinexistente
https://www.siteinexistente.com não foi encontrado (404 Not Found)

Deseja inserir mais algum site? [1-sim] e [2-não]: 2
Encerrando o teste de conexão!
Sites digitados: ['google', 'siteinexistente']
Requisitos
Python 3.x

Biblioteca requests

bash
Copiar código
pip install requests
