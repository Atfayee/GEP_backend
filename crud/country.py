from sqlalchemy.orm import Session

import models.country
import models, schemas
from database import SessionLocal
from models.country import Country

def init_country_data():
    db: Session = SessionLocal()
    try:
        if not db.query(models.country.Country).first():
            db.add_all([
                Country(id="NG", name="Nigeria"),
                Country(id="TG", name="Togo")
            ])
            db.commit()
    finally:
        db.close()

def get_countries(db: Session):
    return db.query(models.country.Country).all()