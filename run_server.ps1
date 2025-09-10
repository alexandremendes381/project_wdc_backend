# Script para rodar o servidor FastAPI
# Execute: powershell -File run_server.ps1

$env:RESEND_API_KEY = (Get-Content .env | Select-String -Pattern 'RESEND_API_KEY' | ForEach-Object { $_.ToString().Split('=')[1].Trim() })
D:/PerfilNaoApagar/Downloads/project_wdc_backend/.venv/Scripts/python.exe -m uvicorn main:app --reload
