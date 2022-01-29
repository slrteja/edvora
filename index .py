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
