from fastapi import FastAPI
from Other.schemas import User_Model

app = FastAPI()


@app.get("/")
def GetROOT():
    return {"Seen": "Working"}


@app.post("/AddUser")
def AddUser(User: User_Model):
    return {"User Received  ": f"{User.Name}"}
