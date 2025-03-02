from fastapi import APIRouter, FastAPI, Form

from entities.UserSchema import UserSchema

router = APIRouter(tags=['login'])

@router.post('/login')
async def login(users_login_data: str = Form(title="User's login data"), password: str = Form(title="Password")):
