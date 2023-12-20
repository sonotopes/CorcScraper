from selectolax.parser import Node
import re
from datetime import datetime
import pandas as pd

def regex(input_str: str, pattern:str, do_what: str = "findall"):
    if do_what == "findall":
        return re.findall(pattern, input_str)
    else:
        raise ValueError("This function needs findall or some other function")



def format_and_transform(attrs=dict):
    transforms = {
        "type": lambda raw: str(raw.upper()),
        "location": lambda raw: str(raw.upper()),
        "price": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
        "beds": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
        "baths": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
        "half_baths": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
        "square_feet": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
    }

    for k, v in transforms.items():
        if k in attrs and attrs[k] != "Not listed" and attrs[k] != "Price Upon Request":
            attrs[k] = v(attrs[k])

    return attrs

def save_to_file(filename="extract", data:list[dict] = None):
    if data is None:
        raise ValueError("The function expects data as a list of dictionaries")

    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
    df.to_csv(filename, index=False)
