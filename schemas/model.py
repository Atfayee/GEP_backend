from pydantic import BaseModel

class Model(BaseModel):
    id: str
    country_id: str
    description: str
    