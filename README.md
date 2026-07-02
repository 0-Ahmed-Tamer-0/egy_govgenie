# EGY-GovGenie — Generative AI Team

> "Simplifying Government. Empowering Citizens."

A Generative & Agentic AI platform that transforms complex Egyptian government procedures into personalized, step-by-step citizen guidance.

---

## Project Structure

```
egy_govgenie_genai/
├── data/
│   ├── raw/
│   │   ├── regulations/      ← Egyptian legal texts & decrees (never commit)
│   │   ├── procedures/       ← Government service procedure docs
│   │   └── mock/             ← Mock DS outputs for dev/testing
│   └── processed/
│       ├── chunks/           ← Text chunks after splitting
│       └── vector_db/        ← FAISS index files
│
├── govgenie/                 ← Main Python package
│   ├── agents/
│   │   ├── gpga.py           ← Generative Procedure Guidance Agent
│   │   ├── dma.py            ← Document Management Agent
│   │   ├── pfa.py            ← Proactive Follow-up Agent
│   │   └── state.py          ← Shared agent state object
│   ├── app/
│   │   ├── main.py           ← FastAPI endpoints
│   │   └── streamlit_app.py  ← Streamlit demo UI
│   ├── config/
│   │   ├── prompts.py        ← ALL prompt templates (edit here, nowhere else)
│   │   └── settings.py       ← Config loaded from .env
│   ├── core/
│   │   ├── llm.py            ← LLM client (OpenAI / Gemini / Ollama)
│   │   ├── embeddings.py     ← Embedding model setup
│   │   └── vectorstore.py    ← FAISS wrapper
│   ├── ingestion/
│   │   ├── loaders.py        ← Load PDFs, txt files
│   │   ├── chunking.py       ← Split text into chunks
│   │   └── indexer.py        ← Build & save FAISS index
│   ├── rag/
│   │   ├── retriever.py      ← Query the vector store
│   │   └── chain.py          ← Full RAG pipeline (retrieve → prompt → generate)
│   ├── services/
│   │   ├── guidance_service.py   ← Orchestrates GPGA
│   │   ├── document_service.py   ← Orchestrates DMA
│   │   └── followup_service.py   ← Orchestrates PFA
│   ├── tools/
│   │   ├── rag_tool.py           ← RAG as a LangChain tool
│   │   ├── document_tool.py      ← Document checklist tool
│   │   └── alert_tool.py         ← Alert generation tool
│   └── schemas/
│       ├── citizen.py            ← CitizenProfile schema
│       ├── application.py        ← ApplicationState schema
│       └── contract.py           ← DS→GenAI JSON contract (source of truth)
│
├── notebooks/
│   ├── 01_rag_basics.ipynb           ← Week 1: learn RAG from scratch
│   ├── 02_gpga_prompts.ipynb         ← Week 2: GPGA prompt engineering
│   ├── 03_dma_document_logic.ipynb   ← Week 2: DMA document matching
│   ├── 04_pfa_alerts.ipynb           ← Week 2: PFA alert generation
│   └── 05_full_pipeline.ipynb        ← Week 4: end-to-end integration
│
└── tests/
    ├── test_gpga.py
    ├── test_dma.py
    ├── test_pfa.py
    ├── test_rag.py
    └── test_ingestion.py
```

---

## Team Split

| Pair | Owns | Files |
|------|------|-------|
| Pair A | GPGA + RAG pipeline | `agents/gpga.py`, `rag/`, `ingestion/`, `config/prompts.py` |
| Pair B | DMA + Document logic | `agents/dma.py`, `tools/document_tool.py`, `services/document_service.py` |
| Pair C | PFA + API + UI | `agents/pfa.py`, `app/main.py`, `app/streamlit_app.py` |

---

## Quick Start

```bash
# 1. Clone & create virtual environment
git clone <repo-url>
cd egy_govgenie_genai
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment
cp .env.example .env
# Open .env and add your OPENAI_API_KEY or GOOGLE_API_KEY

# 4. Run the Streamlit demo
streamlit run govgenie/app/streamlit_app.py

# 5. Run the FastAPI backend
uvicorn govgenie.app.main:app --reload
```

---

## DS → GenAI Contract

The Data Science team delivers a `DSInsights` object (see `schemas/contract.py`).  
**Do not change this schema without notifying both teams.**

```json
{
  "service": "start_import_business",
  "complexity_score": 0.72,
  "avg_processing_days": 21,
  "num_steps": 8,
  "rejection_risk": 0.35,
  "missing_doc_flags": ["tax_id", "import_license"],
  "common_rejection_reason": "Missing Tax Registration Certificate"
}
```
