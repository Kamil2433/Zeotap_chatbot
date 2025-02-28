from fastapi import APIRouter
from backend.api.query_handler import handle_query

router = APIRouter()

@router.get("/query/")
async def query_chatbot(question: str):
    return handle_query(question)
