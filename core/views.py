from fastapi import Depends, HTTPException, status

def hello_world():
    response =  {"message": "Hello World"}
    return response