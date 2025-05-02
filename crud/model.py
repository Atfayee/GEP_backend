from sqlalchemy.orm import Session

from database import SessionLocal
import models
import models.model
from models.model import Model


def init_model_data():
    db: Session = SessionLocal()

    try:
        if not db.query(models.model.Model).first():
            db.add_all([
                Model(id="NG-gf", country_id="NG", description="greenfield"),
                Model(id="NG-bf", country_id="NG", description="brownfield"),
                Model(id="TG-gf", country_id="TG", description="greenfield"),
                Model(id="TG-bf", country_id="TG", description="brownfield"),
            ])
            db.commit()
    finally:
        db.close()

def get_models(country_id: str, db: Session):
    return db.query(models.model.Model).filter(models.model.Model.country_id == country_id).all()
