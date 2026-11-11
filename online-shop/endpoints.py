from http.client import HTTPException

import uvicorn
from fastapi import FastAPI, Request, Form
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from ShopORM import Session, OrderItem, ItemDesc, Orders, Item, User
from typing import Annotated

from app.pydantic_eval import UserLogin
from evaluation import ConfirmForm, ConfirmCode
# from whatever_file import send_code, check_code
from sqlalchemy import insert, select


# def check_code(form_code, code):
#     return form_code == code


def check_code(code):
    if code:
        return True

server_code = 123456
def send_code(email):
    pass #send code to email

def get_server_code():
    return server_code

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/home')
def home(request: Request):
    with Session() as session:
        items = session.execute(select(Item.id, Item.article, Item.manufacturer, Item.amount, Item.price))
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
        return RedirectResponse(url='/confirm-order', status_code=status.HTTP_303_SEE_OTHER)
    else:
        if check_code(form.input_code):
            # with Session() as session:
            #     cart = get_from_cart()
            #     session.execute(insert(ShopOrder).values(phone=form.phone, email=form.email, item_id=cart))
            return RedirectResponse(url='/confirmed', status_code=status.HTTP_303_SEE_OTHER)
    return HTTPException()

@app.get("/signup")
def login(request: Request):
    return templates.TemplateResponse(request, 'signup.html')

@app.post("/signup")
def sign_up(form_data: Annotated[UserLogin, Form()]):
    send_code(form_data.email)
    return RedirectResponse(url=f'/send/?form_data={form_data}', status_code=status.HTTP_303_SEE_OTHER)

@app.get('/send/')
def reg_(request: Request, form_data: ConfirmForm):
    return templates.TemplateResponse(request, 'send.html')

@app.post('/send/')
def reg(form_data: ConfirmForm, confirm_code: Annotated[ConfirmCode, Form()], server_code: int = get_server_code()):
    if confirm_code.input_code != server_code:
        return HTTPException()
    with Session() as session:
        session.execute(insert(User).values(email=form_data.email, username=form_data.username, password=form_data.password))
    return RedirectResponse(url='/register/success', status_code=status.HTTP_303_SEE_OTHER)

@app.get('/register/success')
def get_reg(request: Request):
    return templates.TemplateResponse(request, 'success.html')


@app.get('/confirmed')
def confirmed(request: Request):
    return templates.TemplateResponse(request, 'confirmed.html')

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)