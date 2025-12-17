from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from app.services import intouch_service
from app.services.email_service import send_email
from app.core.security import validar_acesso

router = APIRouter()

# AQUI FICA A ROTA DE CONSULTAR O USUARIO, UTILIZANDO A MATRICULA
@router.get("/consultar/{matricula}", dependencies=[Depends(validar_acesso)])
def consultar_usuario(matricula: str):
    resultado = intouch_service.buscar_funcionario(matricula)

    if not resultado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return resultado

# AQUI FICA A ROTA DE DESATIVAR O USUARIO, UTILIZANDO A MATRICULA
@router.post("/desativar/{matricula}", dependencies=[Depends(validar_acesso)])
def desativar_funcionario(
    matricula: str,
    background_tasks: BackgroundTasks
):
    resultado = intouch_service.desativar_funcionario(matricula)

    if not resultado:
        raise HTTPException(status_code=400, detail="Erro ao desativar usuário")

    # EMAIL ENVIADO EM BACKGROUND PARA OTIMIZAR
    background_tasks.add_task(send_email, matricula)

    return {
        "message": "Usuário desativado com sucesso",
        "matricula": matricula
    }
