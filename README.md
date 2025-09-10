# Backend FastAPI - Sistema de Envio de E-mails

Este projeto é um backend em Python utilizando FastAPI para envio de e-mails via Resend, registro dos envios em banco SQLite e consulta dos envios realizados.

## Requisitos
- Python 3.11+
- FastAPI
- Uvicorn
- Resend SDK
- SQLite3
- venv (ambiente virtual)

## Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/alexandremendes381/project_wdc_backend.git
   cd project_wdc_backend
   ```
2. Crie e ative o ambiente virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure o arquivo `.env` com sua chave da Resend:
   ```env
   RESEND_API_KEY=seu_token_resend
   EMAIL_FROM=seu_email@seudominio.com
   ```

## Como rodar o sistema
Execute o backend com o comando:
```sh
python main.py runserver
```
Ou diretamente com Uvicorn:
```sh
uvicorn main:app --reload
```

## Endpoints
### 1. Enviar e-mail
- **POST** `/api/v1/email/send`
- Body (JSON):
  ```json
  {
    "to": "destinatario@exemplo.com",
    "subject": "Assunto do email"
  }
  ```
- Retorno: status do envio

### 2. Listar e-mails enviados
- **GET** `/api/v1/email/list`
- Retorno: lista dos envios registrados no banco

## Banco de dados
- Utiliza SQLite (`emails.db`) para registrar os envios.

## Observações
- Para enviar e-mails reais, o domínio do remetente precisa estar verificado na Resend.
- O template do e-mail está em `email_template.py`.
- O sistema segue boas práticas de organização e validação.

## Dúvidas
Abra uma issue ou entre em contato pelo GitHub.
