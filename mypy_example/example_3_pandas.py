from typing import Dict, List

import pandas as pd


def df_from_dict(data: Dict[str, List[int]], columns: List[str] = None) -> pd.DataFrame:
    return pd.DataFrame.from_dict(data, orient="index", columns=columns)


if __name__ == "__main__":
    countries: Dict[str, List[int]] = {
        "Germany": [83042200, 6],
        "USA": [328239523, 2],
        "Equador": [17084358, 0],
    }
    country_data_frame = df_from_dict(countries, columns=["Population", "Cases"])
    print(country_data_frame)
