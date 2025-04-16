# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.responses import RedirectResponse
# from sqlalchemy.orm import Session
# from fastapi_sso.sso.google import GoogleSSO
# from starlette.requests import Request
# from dotenv import load_dotenv
# from pathlib import Path
# import os


# directory_path = Path(__file__).parent
# env_file_path = directory_path.parent / '.env'

# load_dotenv()
# GOOGLE_CLIENT_ID =  os.getenv("GOOGLE_CLIENT_ID")
# GOOGLE_CLIENT_SECRET =  os.getenv("GOOGLE_CLIENT_SECRET")

# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# google_sso = GoogleSSO(
#     GOOGLE_CLIENT_ID,
#     GOOGLE_CLIENT_SECRET, 
#     "http://localhost:9999/v1/google/callback",
#     allow_insecure_http=True
# )

# router = APIRouter(prefix="/v1/google")


# @router.get("/login", tags=['Google SSO'])
# async def google_login():
#     return await google_sso.get_login_redirect(params={"prompt": "consent", "access_type": "offline"})


# @router.get("/callback", tags=['Google SSO'])
# async def google_callback(request: Request, db: Session = Depends(get_db)):
#     """Process login response from Google and return user info"""

#     try:
#         user = await google_sso.verify_and_process(request)
#         user_stored = db_crud.get_user(db, user.email, provider=user.provider)
#         if not user_stored:
#             user_to_add = UserSignUp(
#                 username=user.email,
#                 fullname=user.display_name
#             )
#             user_stored = db_crud.add_user(db, user_to_add, provider=user.provider)
#         access_token = create_access_token(username=user_stored.username, provider=user.provider)
#         response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
#         response.set_cookie(SESSION_COOKIE_NAME, access_token)
#         return response
#     except db_crud.DuplicateError as e:
#         raise HTTPException(status_code=403, detail=f"{e}")
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=f"{e}")
#     except Exception as e:
#         raise HTTPException(
#             status_code=500, detail=f"An unexpected error occurred. Report this message to support: {e}")

from fastapi import FastAPI, HTTPException, Request
from pathlib import Path
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_sso.sso.google import GoogleSSO

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

directory_path = Path(__file__).parent
env_file_path = directory_path.parent / '.env'


load_dotenv()
GOOGLE_CLIENT_ID =  os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET =  os.getenv("GOOGLE_CLIENT_SECRET")

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

google_sso = GoogleSSO(
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET, 
    "http://localhost:8000/google/callback",
    allow_insecure_http=True
)
templates = Jinja2Templates(directory="template")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/google/login")
async def google_login():
    return await google_sso.get_login_redirect(params={"prompt": "consent", "access_type": "offline"})

@app.get("/google/callback")
async def google_callback(request: Request):
    """Process login response from Google and return user info"""
    try:
        user = await google_sso.verify_and_process(request)
        return {"user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred. Report this message to support: {e}")
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app)