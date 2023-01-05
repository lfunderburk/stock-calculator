import requests
from dotenv import load_dotenv
import pandas as pd
import json
import sys, os

def api_data_extraction(url) -> pd.DataFrame:
    """
    Extract data from an api
    """
    try:
        
        json_resp = requests.get(url)
        return json_resp
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)

if __name__=="__main__":

    # Append root directory and read .env
    sys.path.append(".")
    load_dotenv(".env") 

    # Get API key
    api_key = os.environ.get("API")

    # Test query
    symbol = "AAPL"
    url  = f"http://api.marketstack.com/v1/eod?access_key={api_key}&symbols={symbol}"
    resp = api_data_extraction(url)

    print(resp)
    