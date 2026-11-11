
from fastapi import FastAPI, Request, Form
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

code = 123

@app.get("/test/")
async def read_item(request: Request, success: bool = True):
    return templates.TemplateResponse(request, 'test.html', context={"success": success})

@app.post('/test/')
def test(form_code: int = Form()):
    if form_code == code:
        return {"success": "true"}
    return RedirectResponse(url='/test/?success=false', status_code=status.HTTP_303_SEE_OTHER)
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)