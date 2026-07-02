from pydantic import BaseModel
from typing import Optional

class CitizenProfile(BaseModel):
    citizen_id: str
    name: str
    location: str                       # e.g. "Cairo", "Alexandria"
    business_type: Optional[str] = None
    language: str = "ar"                # "ar" or "en"
    existing_docs: list[str] = []       # docs the citizen already has
