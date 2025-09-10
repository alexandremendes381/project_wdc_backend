# Backend FastAPI - Envio de Email com Resend

Este projeto é um backend em Python utilizando FastAPI, que recebe um POST com um email e dispara um email HTML para esse endereço usando Resend.

## Funcionalidades
- API REST com FastAPI
- Endpoint POST para receber email
- Envio de email HTML via Resend
- Ambiente isolado com venv

## Como rodar
1. Crie e ative o ambiente virtual (venv)
2. Instale as dependências
3. Configure a chave da API Resend
4. Execute o servidor FastAPI

## Estrutura
- `main.py`: API principal
- `email_service.py`: Serviço de envio de email
- `requirements.txt`: Dependências

## Observações
- Substitua a chave da API Resend pelo seu token.
- O template do email pode ser customizado em `email_service.py`.
