# routers/countries.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from database import get_session
from typing import List

from models.country_list import CountryListResponse
from models.country_detail import CountryDetail
from models.country import Country

router = APIRouter()

# @router.get("/countries", response_model=List[Country])
# def get_countries(session=Depends(get_session)):
#     return session.exec(select(Country)).all()


# @router.get("/countries/{iso}", response_model=Country)
# def get_country(iso:str, session=Depends(get_session)):
#     country = session.get(Country, iso.upper())
#     if not country:
#         raise HTTPException(status_code=404, detail="Country not found")
#     return country



@router.get("/countries", response_model=CountryListResponse)
def get_country_list():
    return {
        "countries": [
            {"id": "AO", "name": "Angola"},
            {"id": "BD", "name": "Bangladesh"},
            {"id": "BJ", "name": "Benin"},
            {"id": "BW", "name": "Botswana"},
            {"id": "BF", "name": "Burkina Faso"},
            {"id": "BI", "name": "Burundi"},
            {"id": "KH", "name": "Cambodia"},
            {"id": "CM", "name": "Cameroon"}
        ]
    }

@router.get("/countries/BD", response_model=CountryDetail)
def get_country_detail(iso: str):
    if iso.upper() == "BD":
        return {
            "id": "BD",
            "name": "Bangladesh",
            "models": [
                {
                    "id": "bd-3",
                    "country": "BD",
                    "attribution": {
                        "author": "KTH",
                        "url": "https://www.energy.kth.se/energy-systems/about-the-division-of-energy-systems-1.937036"
                    },
                    "description": "This model is developed...",
                    "disclaimer": "",
                    "filters": [...],  # You can paste your filter list here
                    "levers": [...],   # And levers too
                    "baseYear": 2020,
                    "timesteps": [2025, 2030]
                }
            ]
        }

    raise HTTPException(status_code=404, detail="Country not found")