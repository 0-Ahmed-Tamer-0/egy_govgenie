"""
DS → GenAI data contract.
This is the exact JSON shape the Data Science team must deliver.
If DS changes a field, update here and notify all agents.
"""
from pydantic import BaseModel
from typing import List, Optional

class DSInsights(BaseModel):
    service: str                        # e.g. "start_import_business"
    complexity_score: float             # 0.0–1.0 (DS Module A)
    avg_processing_days: int            # estimated days
    num_steps: int                      # total steps in procedure
    rejection_risk: float               # 0.0–1.0 (DS Module B)
    missing_doc_flags: List[str]        # e.g. ["tax_id", "business_plan"]
    common_rejection_reason: Optional[str] = None
