from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.model
import database
import crud
from schemas.model import ModelOut

router = APIRouter()

@router.get('/countries/{id}/models', response_model=List[ModelOut])
def get_models(id: str, db: Session = Depends(database.get_db)):
    models = crud.model.get_models(id, db)
    if models is None:
        raise HTTPException(
            status_code=404,
            detail=f"No models found for {id}"
        )
    return models

@router.get('/models/{id}', response_model=ModelOut)
def get_model(id:str, db: Session = Depends(database.get_db)):
    model = crud.model.get_model(id, db)
    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"No model found for {id}."
        )
    return model