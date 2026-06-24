from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserData(BaseModel):
    name: str
    birthdate: str

def reduce_to_arcane(n: int) -> int:
    if n == 0:
        return 22
    while n > 22:
        n = sum(int(digit) for digit in str(n))
    return n

@app.post("/api/calculate")
async def calculate_matrix(data: UserData):
    try:
        parts = data.birthdate.split("-")
        year_str, month_str, day_str = parts[0], parts[1], parts[2]
    except Exception:
        day_str, month_str, year_str = "22", "09", "2010"

    day = int(day_str)
    month = int(month_str)
    year = int(year_str)

    a = reduce_to_arcane(day)
    b = reduce_to_arcane(month)
    
    year_sum = sum(int(d) for d in str(year))
    v = reduce_to_arcane(year_sum)
    
    g = reduce_to_arcane(a + b + v)
    d = reduce_to_arcane(a + b + v + g)

    return {
        "status": "success",
        "matrix": {
            "pointA": a,
            "pointB": b,
            "pointV": v,
            "pointG": g,
            "pointD": d
        }
    }






                  
