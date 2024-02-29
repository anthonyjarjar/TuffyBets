from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import Optional
from datetime import date


class UserAuth(BaseModel):
    """
    Used for authenticating a user
    """
    username: str
    password: str

class Token(BaseModel):
    """
    Access token for authentication
    """
    access_token: str
    token_type:   str

class User(SQLModel, table=True):
    """
    This is the schema for a user in the database. 

    id: Generated by database to identify user
    username: user inputed screen name
    password: user password to authenticate their account
    dob: user date of birth for ensuring age
    credits: Quantity of credits owned by user
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    dob: date 
    credits: Optional[int] = Field(default=0)

    # def __repr__(self):
    #     return f"User({self.id}, {self.username})" 

class UserUpdate(BaseModel):
    """
    Represents the data used to update an existing user record in the database.
    """
    username: Optional[str] = None
    password: Optional[str] = None
    credits: Optional[int] = None

class Game(SQLModel):
    game_id: int
    players: list

