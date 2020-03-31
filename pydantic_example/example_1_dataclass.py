from dataclasses import dataclass
from typing import Dict


@dataclass
class CountryDC:
    _id: int
    name: str
    population: Dict[int, int]


if __name__ == "__main__":
    country_dc = CountryDC(_id=1, name="Slovenia", population=2094060)
    print(country_dc)
