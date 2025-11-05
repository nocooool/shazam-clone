from fastapi import FastAPI, UploadFile, Form, Depends, HTTPException

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Backend running!"}

#for signup
'''
@app.post("/auth/signup")
def signup(user: UserSignup):


#for login
@app.post("/auth/login")
def login(user: UserLogin):


#recognize
@app.post("/recognize")
def recognize(file: UploadFile, username: str = Form(...)):


#history
@app.post("/history/{username}")
def get_history(username: str):
    return {"history": history_db.get(username, [])}\
'''