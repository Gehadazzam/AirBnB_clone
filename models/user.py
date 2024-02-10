#!/usr/bin/python3
"""class User that inherits from BaseModel"""


from models.base_model import BaseModel
import json

class User(BaseModel):
    """user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
