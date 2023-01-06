import requests
from dotenv import load_dotenv
import pandas as pd
import json
import sys, os

def api_data_extraction(url, headers, file_name, query_string) -> pd.DataFrame:
    """
    Extract data from an api
    """
    try:
        
        json_resp = requests.request("GET", url, headers=headers, params=query_string)
        data = json_resp.json()
       
        return data

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

    # Set up url
    xrapid_url = "https://alpha-vantage.p.rapidapi.com/query"
    apilayer_url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=GBP&amount=1"
    # url = "https://api.apilayer.com/exchangerates_data/timeseries?start_date={start_date}&end_date={end_date}"

    # Get API key
    XRapidAPIKey = os.environ.get("XRapidAPIKey")
    apilayerKey = os.environ.get("apilayerKey")

    # Define headers 
    # Alpha Vantage API
    headers_alphavantage = {
        "X-RapidAPI-Key": XRapidAPIKey,
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    header_apilayer = {
        "apikey": apilayerKey
    }

    # Query for Carnival 
    query_string_le = {"function":"TIME_SERIES_DAILY","symbol":"CCL","datatype":"json","output_size":"compact"}
    query_string_nyse = {"function":"TIME_SERIES_DAILY","symbol":"NYSE:CCL","datatype":"json","output_size":"compact"}

    # # Perform query
    # resp_nyse = api_data_extraction(xrapid_url, headers_alphavantage, "./data/nyse_ccl.json",query_string_nyse)
    # resp_le = api_data_extraction(xrapid_url, headers_alphavantage, "./data/le_ccl.json",query_string_le)

    # # Reformat into dataframe object
    # nyse_ccl_df = pd.DataFrame.from_dict(resp_nyse['Time Series (Daily)']).T
    # le_ccl_df = pd.DataFrame.from_dict(resp_le['Time Series (Daily)']).T

    # # Save to csv
    # nyse_ccl_df.to_csv("./data/nyse_ccl_daily.csv")
    # le_ccl_df.to_csv("./data/le_ccl_daily.csv")

    # # US to UK Pound
    resp_us_to_gbp = api_data_extraction(apilayer_url, header_apilayer, "./data/us_gbp_2023_01-04.json",None)
    