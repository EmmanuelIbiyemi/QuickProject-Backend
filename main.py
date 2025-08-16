from fastapi import FastAPI, HTTPException, Depends , status
from fastapi.middleware.cors import CORSMiddleware

# ----THIS IS FOR THE USER LOGIN AND SIGNUP
from db.schemas import Signup
from db.schemas import Login

# ---- THIS IS FOR THE DATABASE
from db.connectiondb import SessionLocal
from db.model import User
from sqlalchemy.orm import Session

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

database = SessionLocal()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def quickMessage():
    return {"message":"Quick project use /docs to view and run it with a Ui and understand the path"}

#--- This is for the sign up section to put value in the database
@app.post("/Signup")
def signup (user: Signup ,db: Session = Depends(get_db) ):

    # had to think of when the user like input some kind cap. letter
    #  but taught of it late so i had to add it quickly to prevent any error
    lower_User = user.username.lower()

    try:
        db_user = User(name=lower_User, email=user.usermail , password=user.userpassword)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        if not db_user:
            print("Error Error for the database part")
            return {"error: ", HTTPException(status_code=status.HTTP_409_CONFLICT)}

        return {"messgae: ", db_user}
    except:
        print("Their is fire on the mountain")
        return {"message: ", "Go check the code"}



#--- This is for the log in section to fetch value in the database
@app.get("/Login")
def login( Username:str, Password:int, db: Session = Depends(get_db) ):


    # had to think of when the user like input some kind cap. letter
    #  but taught of it late so i had to add it quickly to prevent any error
    lower_User = Username.lower()

    try:
        user = db.query(User).filter(User.name == lower_User, User.password == Password).first()
        if not user:
            return "User Not Found"
            # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

        if user:
            return "success"

    except:
        return {"message: ", "Error on the code"}

    return {"message": f"Welcome Back {User.name}"}

@app.get("/checkusers")
async def checkallusers(db: Session = Depends(get_db)):
    try:
        checkusers = db.query(User).all()
        print(checkusers)
        return (checkusers)
    except:
        print("Their is fire on the mountain")
    return {"message": "This is all the users"}