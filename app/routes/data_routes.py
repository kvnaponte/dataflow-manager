from fastapi import APIRouter

router = APIRouter(prefix="/data", tags=["Data"])

@router.get("/status")
def check_status():
    return {"status": "Todo funcionando correctamente!"}
