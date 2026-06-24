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

@app.get("/")
async def root():
    return {"message": "AuraCode API работает!"}

@app.post("/api/calculate")
async def calculate_matrix(data: UserData):
    day, month, year = 22, 9, 2010
    
    if data.birthdate:
        try:
            parts = data.birthdate.split("-")
            if len(parts) == 3:
                if len(parts[0]) == 4:
                    year = int(parts[0])
                    month = int(parts[1])
                    day = int(parts[2])
                else:
                    day = int(parts[0])
                    month = int(parts[1])
                    year = int(parts[2])
        except Exception:
            pass

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

                  
