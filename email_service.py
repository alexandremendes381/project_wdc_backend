import os
import resend
from dotenv import load_dotenv
from email_template import EMAIL_TEMPLATE

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
RESEND_FROM = os.getenv("RESEND_FROM")
resend.api_key = RESEND_API_KEY

class EmailService:
  def send_html_email(self, to_email: str, subject: str, html_content: str):
    if not RESEND_FROM or RESEND_FROM == "no-reply@seudominio.com":
      raise Exception("O campo 'from' do email precisa ser um endereço autorizado na Resend. Configure a variável RESEND_FROM no arquivo .env com um email verificado.")
    return resend.Emails.send(
      {
        "from": RESEND_FROM,
        "to": to_email,
        "subject": subject,
        "html": html_content,
      }
    )
