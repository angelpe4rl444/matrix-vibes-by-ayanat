from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date

app = FastAPI(title="AuraMatrix API", version="1.0.0")

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

def reduce_number(num: int) -> int:
    while num > 22:
        num = sum(int(digit) for digit in str(num))
    return num

@app.post("/api/calculate")
def calculate_matrix(user: UserDate):
    try:
        parsed_date = date.fromisoformat(user.birthdate)
        date = parsed_date.day
        month = parsed_date.month
        year = parsed_date.year
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверный формат даты. Используйте YYYY-MM-DD")
    point_A = reduce_number(day)
    point_B = reduce_number(month)

    year_sum = sum(int(digit) for digit in str(year))
    point_V = reduce_number(year_sum)

    point_G = reduce_number(point_A + point_B + point_V)
    point_D = reduce_number(point_A + point_B + point_V + point_G)

    return {
        "status": "success",
        "meta": {
            "name": user.name,
            "birthdate": f"{day:02d}.{month:02d}.{year}"
            },
            "matrix": {
                "pointA": point_A,
                "pointB": point_B,
                "pointV": point_V,
                "pointG": point_G,
                "pointD": point_D
                }
        }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",
host="127.0.0.1", port=8000,
reload=True)
                
            






                  
