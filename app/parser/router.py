from fastapi import APIRouter
from app.parser.parser import ParseWB

router = APIRouter(
    prefix="/parser",
    tags=["Parser"]
)


@router.post("/")
def parse():
    ParseWB("https://www.wildberries.by/catalog?brandpage=27445__MSI").parse()
    return "Спарсили"
