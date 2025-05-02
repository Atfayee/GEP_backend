from sqlalchemy.orm import Session

from database import SessionLocal
from models.model import Model, Lever


def init_model_data():
    db: Session = SessionLocal()

    try:
        if not db.query(Model).first():
            models = [
                Model(id="NG-gf", country_id="NG", description="greenfield"),
                Model(id="NG-bf", country_id="NG", description="brownfield"),
                Model(id="TG-gf", country_id="TG", description="greenfield"),
                Model(id="TG-bf", country_id="TG", description="brownfield"),
            ]
            db.add_all(models)
            db.commit()     
        if not db.query(Lever).first():
            levers = [
                Lever(model_id="NG-gf", label="Hex demand target", description="Definition: Hex demand target"),
                Lever(model_id="NG-gf", label="City demand target", description="Definition: City demand target"),
                Lever(model_id="NG-gf", label="Hex City demand target", description="Definition: Hex City demand target"),
                Lever(model_id="NG-bf", label="Hex demand target", description="Definition: Hex demand target"),
                Lever(model_id="NG-bf", label="City demand target", description="Definition: City demand target"),
                Lever(model_id="NG-bf", label="Hex City demand target", description="Definition: Hex City demand target"),
                Lever(model_id="TG-gf", label="Hex demand target", description="Definition: Hex demand target"),
                Lever(model_id="TG-gf", label="City demand target", description="Definition: City demand target"),
                Lever(model_id="TG-gf", label="Hex City demand target", description="Definition: Hex City demand target"),
                Lever(model_id="TG-bf", label="Hex demand target", description="Definition: Hex demand target"),
                Lever(model_id="TG-bf", label="City demand target", description="Definition: City demand target"),
                Lever(model_id="TG-bf", label="Hex City demand target", description="Definition: Hex City demand target"),
            ]
            db.add_all(levers)
            db.commit()
    finally:
        db.close()

def get_models(country_id: str, db: Session):
    return db.query(Model).filter(Model.country_id == country_id).all()

def get_model(model_id: str, db: Session):
    return db.query(Model).filter(Model.id == model_id).first()
