from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ApplicationState(BaseModel):
    app_id: str
    citizen_id: str
    service: str
    status: str                         # "pending" | "missing_docs" | "submitted" | "approved" | "rejected"
    deadline: Optional[datetime] = None
    missing_docs: list[str] = []
    last_updated: datetime = datetime.now()
    notes: Optional[str] = None
