from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr
from email_service import EmailService, EMAIL_TEMPLATE
from db import save_email, get_all_emails
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
email_service = EmailService()

class EmailRequest(BaseModel):
    email: EmailStr

@app.post("/api/v1/email/send", tags=["Email"])
async def send_email(request: EmailRequest):
    try:
        response = email_service.send_html_email(
            to_email=request.email,
            subject="Bem-vindo ao nosso serviço!",
            html_content=EMAIL_TEMPLATE
        )
        save_email(request.email)
        return {"message": "Email enviado com sucesso", "resend_response": response}
    except Exception as e:
        import traceback
        return {"error": str(e), "trace": traceback.format_exc()}, 500

# Endpoint GET para listar emails enviados
@app.get("/api/v1/email/list", tags=["Email"])
def list_emails():
    return get_all_emails()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "runserver":
        import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
