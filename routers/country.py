# # routers/countries.py
# from fastapi import APIRouter, Depends, HTTPException, Query
# from sqlmodel import select
# from database import get_db
# from typing import List
# from sqlalchemy import text
# from fastapi.responses import JSONResponse
# import os
# from dotenv import load_dotenv
# from models.country_detail import CountryDetail

# from shapely.geometry import Polygon, shape

# load_dotenv()

# PG_HOST = os.getenv("PG_HOST")
# PG_PORT = os.getenv("PG_PORT")
# PG_DATABASE = os.getenv("PG_DATABASE")
# PG_USER = os.getenv("PG_USER")
# PG_PASSWORD = os.getenv("PG_PASSWORD")

# router = APIRouter()

# # @router.get("/countries", response_model=List[Country])
# # def get_countries(session=Depends(get_session)):
# #     return session.exec(select(Country)).all()


# # @router.get("/countries/{iso}", response_model=Country)
# # def get_country(iso:str, session=Depends(get_session)):
# #     country = session.get(Country, iso.upper())
# #     if not country:
# #         raise HTTPException(status_code=404, detail="Country not found")
# #     return country

# # test for hex demands data
# @router.get("/hex/tgo")
# def get_tgo(
#     resolution: int = Query(5, ge=4, le=6), 
#     session= Depends(get_session)):
#     hex_col = f"hex{resolution}"
#     query = text(f"""
#                  SELECT 
#   {hex_col} AS hex_id, 
#   SUM("GDP") AS gdp 
# FROM public."TGO_hex_demands"
# GROUP BY {hex_col}
# HAVING SUM("GDP") > 20000000
#       """)
#     rows = session.execute(query).mappings().all()
#     results = []
#     for row in rows:
#         results.append({
#             "GDP": row["gdp"],
#             "h3_hex8": row["hex_id"]
#         })
#     print(len(results))

#     return results


# @router.get("/hex/texas")
# def get_fiberPromise_texas(
#     resolution: int = Query(5, ge=2, le=8), 
#     session= Depends(get_session)):
#     h3_res_id = f"h3_res{resolution}_id"
#     query = text(f"""
#                  SELECT 
#                     {h3_res_id} AS h3_id,
#                     COUNT(brand_name) AS brand_count,
#                     CASE 
#                         WHEN BOOL_OR(business_residential_code = 'B') AND BOOL_OR(business_residential_code = 'B') THEN 'mixed'
#                         WHEN BOOL_OR(business_residential_code = 'R') AND BOOL_OR(business_residential_code = 'X') THEN 'mixed'
#                         WHEN BOOL_OR(business_residential_code = 'B') AND BOOL_OR(business_residential_code = 'X') THEN 'mixed'
#                         WHEN BOOL_OR(business_residential_code = 'X') THEN 'mixed'
#                         WHEN BOOL_OR(business_residential_code = 'R') THEN 'residential'
#                         WHEN BOOL_OR(business_residential_code = 'B') THEN 'business'
#                         ELSE 'unknown'
#                     END AS business_residential_code
#                 FROM public.fiber_promise
#                 GROUP BY {h3_res_id};
#             """)
#     rows = session.execute(query).mappings().all()
#     results = []
#     for row in rows:
#         results.append({
#             "brand_count": row["brand_count"],
#             "h3_id": row["h3_id"],
#             "business_residential_code": row["business_residential_code"]
#         })
#     print(len(results))

#     return results





# @router.get("/countries", response_model=CountryListResponse)
# def get_country_list():
#     return {
#         "countries": [
#             {"id": "NG", "name": "Nigeria"},
#             {"id":"TG", "name": "Togo"},
#             {"id": "BD", "name": "Bangladesh"},
#             {"id": "BJ", "name": "Benin"},
#             {"id": "BW", "name": "Botswana"},
#             {"id": "BF", "name": "Burkina Faso"},
#             {"id": "BI", "name": "Burundi"},
#             {"id": "KH", "name": "Cambodia"},
#             {"id": "CM", "name": "Cameroon"},
            
#         ]
#     }

# # mock data 
# mock_country_db = {
#     "NG": {"name": "Nigeria"},
#     "TG": {"name": "Togo"},
#     "IN": {"name": "India"},
# }
# @router.get("/countries/{id}", response_model=CountryDetail)
# def get_country_detail(id: str):
#     country = mock_country_db.get(id.upper())
#     if not country:
#         raise HTTPException(status_code=404, detail="Country not found")
#     return {
#         "id": id.upper(),
#         "name": country["name"],
#         "models":[],
#     }


# mock_country_model_db = {
#     "NG": {
#         "id": "NG",
#         "name": "Nigeria",
#         "models": [
#             {"id": "bf", "name": "Brownfield"},
#             {"id": "gf", "name": "Greenfield"},
#         ]
#     },
#     "TG": {
#         "id": "TG",
#         "name": "Togo",
#         "models": [
#             {"id": "bf", "name": "Brownfield"},
#             {"id": "gf", "name": "Greenfield"},
#         ]
#     }
# }
# @router.get("/countries/{id}/models",)
# def get_country_models(id: str):
#     models = mock_country_model_db.get(id.upper())
#     if not models:
#         raise HTTPException(status_code=404, detail="Country Models not found")
#     return {
#         "id": id.upper(),
#         "name": models["name"],
#         "models":models["models"],
#     }
from sqlalchemy.orm import Session
import crud.country
from fastapi import APIRouter, Depends, HTTPException
import crud, database

router = APIRouter()

@router.get('/countries')
def get_countries(db: Session = Depends(database.get_db)):
    countries =  crud.country.get_countries(db)
    if countries is None:
        raise HTTPException(
            status_code=404,
            detail="No countries found."
        )
    return countries
