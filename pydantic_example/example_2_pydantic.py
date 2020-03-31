from typing import Dict

from pydantic import BaseModel


class Country(BaseModel):
    _id: int
    name: str
    population: Dict[int, int]


if __name__ == "__main__":
    country1 = Country(_id=1, name="Slovenia", population=2094060)
