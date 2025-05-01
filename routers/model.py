from fastapi import APIRouter

router = APIRouter()

@router.get('/countries/{id}/models')
def get_models(id:str):
    return []