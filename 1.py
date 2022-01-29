from logging import Manager

from numpy import append
from fastapi import Depends, load_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

# the python-multipart package is required to use the OAuth2PasswordRequestForm
@append.post('/auth/token')
def login(data: OAuth2PasswordRequestForm = Depends()):

    email = data.username
    password = data.password

    user = load_user(email)  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException
    
    access_token = Manager.create_access_token(
        data=dict(sub=email)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}
import fastapi_login
from importlib_metadata import install
import pip
from fastapi import FastApi
SECRET='cc343eaf914813a2ec50892b9919ebe60da7a2e1626b1f06'
app= FastApi()
from fastapi_login import LoginManager 
manager = fastapi_login (SECRET,token_url='/auth/token')
fake_db = {'surampuditeja@gmail.com' : {'password':'edvora@1'}}
@manager.user_loader()
def load_user(email:str):
    user=fake_db.get(email)
    return user