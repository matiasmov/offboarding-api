from fastapi import APIRouter, Depends, HTTPException
from app.services import intouch_service
from app.core.security import validar_acesso

router = APIRouter()

# Rotas estão separadas para o usuário poder visualizar quem
# é a pessoa antes dele deletar.

# rota para buscar o usuário

@router.get("/consultar/{matricula}", dependencies=[Depends(validar_acesso)])
def consultar_usuario(matricula: str):
    resultado = intouch_service.buscar_funcionario(matricula)
    
    if not resultado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
    return resultado

# aqui é rota de deletar/desativar o usuário
@router.post("/desativar/{matricula}", dependencies=[Depends(validar_acesso)])
def desativar_funcionario(matricula: str):
    
    resultado = intouch_service.desativar_funcionario(matricula)
    
    return resultado