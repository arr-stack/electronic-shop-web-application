from http.client import HTTPException

import uvicorn
from fastapi import FastAPI, Request, Form
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from ShopORM import Session, Item, ShopOrder
from typing import Annotated
from evaluation import ConfirmForm
from whatever_file import send_code, check_code
from sqlalchemy import insert



app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/home')
def home(request: Request):
    with Session() as session:
        items = session.get(Item)
    return templates.TemplateResponse(request, 'home.html', {"items": items})

@app.get('/cart')
def cart(request: Request):
    return templates.TemplateResponse(request, 'cart.html')

@app.get('/items/item/{item_id}')
def show_item(request: Request, item_id: int):
    with Session as session:
        item = session.get(Item, item_id)
    return templates.TemplateResponse(request, 'item.html', {'item': item})

@app.get("/confirm-order")
def confirm(request: Request):
    return templates.TemplateResponse(request, 'confirm.html')

@app.post("/confirm-order")
def get_confirm(form: Annotated[ConfirmForm, Form()]):
    if form.input_code == False:
        send_code()
        return RedirectResponse(url='/confirm-order', status_code=303)
    else:
        if check_code(form.input_code):
            with Session() as session:
                cart = get_from_cart()
                session.execute(insert(ShopOrder).values(phone=form.phone, email=form.email, item_id=cart))
            return RedirectResponse(url='/confirmed', status_code=303)
    return HTTPException()

@app.get('/confirmed')
def confirmed(request: Request):
    return templates.TemplateResponse(request, 'confirmed.html')
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)