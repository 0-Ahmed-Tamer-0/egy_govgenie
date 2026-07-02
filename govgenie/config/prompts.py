"""
All prompt templates live here.
Variables in {curly_braces} are filled at runtime.
"""

GPGA_SYSTEM_PROMPT = """
You are EGY-GovGenie, a helpful Egyptian government services assistant.
You speak clearly in {language}. You simplify bureaucratic procedures into
plain, friendly language. You only use information provided in the context —
never make up steps, documents, or timelines.
"""

GPGA_GUIDANCE_PROMPT = """
A citizen in {location} wants to: {citizen_request}

Based on the following official procedure information:
{retrieved_context}

And the following risk assessment from our system:
- Complexity Score: {complexity_score}/1.0
- Estimated Processing Time: {avg_processing_days} days  
- Rejection Risk: {rejection_risk}/1.0
- Watch out for: {common_rejection_reason}

Generate a clear, numbered step-by-step action plan.
For each step include: what to do, where to go, and how long it takes.
At the end, list all required documents and flag any that are commonly missing.
"""

DMA_DOCUMENT_CHECK_PROMPT = """
The citizen is applying for: {service}
Documents they already have: {existing_docs}
Documents required: {required_docs}

List which documents are missing and explain simply how to obtain each one.
"""

PFA_ALERT_PROMPT = """
Application ID: {app_id}
Service: {service}
Current status: {status}
Deadline: {deadline}
Missing documents: {missing_docs}

Write a short, friendly reminder message to the citizen in {language}.
If the deadline is within 3 days, mark it urgent.
"""
