from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.model
import database
import crud

router = APIRouter()

@router.get('/countries/{id}/models')
def get_models(id: str, db: Session = Depends(database.get_db)):
    models = crud.model.get_models(id, db)
    if models is None:
        raise HTTPException(
            status_code=404,
            detail=f"No models found for {id}"
        )
    return models