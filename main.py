from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# ----THIS IS FOR THE USER LOGIN AND SIGNUP
from db.schemas import Signup
from db.schemas import Login


app = FastAPI(
    title="Quick Project"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:9002", "*"],# For production, this should be a specific list of frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#--- This is for the sign up section to put value in the database
@app.post("/Signup")
def signup (user: Signup):
    return {"message": f"Welcome To Quick Project {user.username}"}


#--- This is for the log in section to fetch value in the database
@app.get("/Login")
def login(Username:str , Password:int):
    return {"message": f"Welcome Back {Username}"}