import requests
import json

import pandas as pd

from .OKW_static import static_data_urls, teryt, okrSejm, wybory

API_url = 'https://aipyonouja.execute-api.us-east-1.amazonaws.com/dev/ewyb/query/tryNested/tryNested={}'

stage = "real"
year = "2019"
wyborySel = "sejm_dev"

okrSejm_df = pd.DataFrame(okrSejm, columns=['num_okr_sejm', 'nazwa_okregu', 'liczba_mandatow'])

def set_stage(new_stage):
    stage = new_stage
    return stage

def set_year(new_year):
    year = new_year
    return year

def sel_wybory(new_wybory):
    try:
        temp = wybory[new_wybory].format(stage, year)
        wyborySel = new_wybory
    except KeyError:
        print("błędna selekcja wyborów {}".format(new_wybory))
    return wyborySel

def get_static_data_url(url_key):
    urls = static_data_urls[url_key]
    df = pd.DataFrame()
    for url in urls:
        resp = requests.get(url)
        df = pd.concat([df, pd.json_normalize(resp.json(), max_level=2)])
    return df

def get_okrSejm():
    return get_static_data_url('okrsejm')

def get_okrSenat():
    return get_static_data_url('okrsenat')

def get_obw():
    return get_static_data_url('obw')
    
def get_kandyd_sejm():
    return get_static_data_url('kandsejm')

def get_kandyd_senat():
    return get_static_data_url('kandsenat')

def add_okr_name_sejm(df):
    return pd.merge(df, okrSejm_df[['num_okr_sejm', 'nazwa_okregu']], on='num_okr_sejm')
    
def get_wybory_data(level=0):
    url = API_url.format(wybory[wyborySel].format(stage, year))
    resp = requests.get(url)
    df = pd.json_normalize(resp.json(), max_level=level)
    return df
