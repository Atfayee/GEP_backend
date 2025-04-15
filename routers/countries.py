# routers/countries.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from database import get_session
from typing import List
from sqlalchemy import text

from models.country_list import CountryListResponse
from models.country_detail import CountryDetail
from models.country import Country

from shapely.geometry import Polygon, shape
import h3
import json 

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

# test for hex demands data
@router.get("/hex/tgo")
def get_tgo(
    resolution: int = Query(5, ge=4, le=6), 
    session= Depends(get_session)):
    hex_col = f"hex{resolution}"
    query = text(f"""
                 SELECT 
  {hex_col} AS hex_id, 
  SUM("GDP") AS gdp 
FROM public."TGO_hex_demands"
GROUP BY {hex_col}
HAVING SUM("GDP") > 20000000
      """)
    rows = session.execute(query).mappings().all()
    results = []
    for row in rows:
        results.append({
            "GDP": row["gdp"],
            "h3_hex8": row["hex_id"]
        })
    print(len(results))

    return results

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
            {"id": "CM", "name": "Cameroon"},
            {"id":"TG", "name": "Togo"},
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