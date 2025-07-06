from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models.page_model import get_shop


router = APIRouter()
templates = Jinja2Templates(directory="app/views")


@router.get("/shop/{name}", response_class=HTMLResponse)
async def shop_page(request: Request, name: str):
    shop_data = get_shop(name)

    if not shop_data:
        raise HTTPException(status_code=404, detail=f"Shop {name} not found!")
    
    context = {
        "request": request,
        "shop": shop_data
    }

    return templates.TemplateResponse("index.html", context)