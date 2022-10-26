import fastf1 as ff1
# import requests
import json
import requests
import warnings
import datetime
# from fastf1 import plotting
# from matplotlib import pyplot as plt
import os

BASE_URL = 'http://ergast.com/api/f1'
YEARS = [2018, 2019, 2020, 2021]

def fetch_day(year, gp=None, day=None):
    """day can be 'qualifying' or 'results'
    """
    # url = f"{base_url}/{year}/{gp}/{day}.json"
    url = f"{BASE_URL}/{year}.json"
    return _parse_json_response(requests.get(url))


def _parse_json_response(r):
    if r.status_code == 200:
        return json.loads(r.content.decode('utf-8'))
    else:
        warnings.warn(f"Request returned: {r.status_code}")
        return None

def parse_races_in_year(data):
    return data['MRData']['RaceTable']['Races']

def yield_races_in_year_list(year):
    j = fetch_day(year)
    races_in_year = parse_races_in_year(j)
    race_names = [race['raceName'] for race in races_in_year]
    return race_names


races = yield_races_in_year_list(2020)

with open('race_names.txt', 'w') as fout:
    for i in races:
        fout.write(f'{i}\n')


# race = ff1.get_session('2020', '70th Anniversary Grand Prix', 'R')
# laps = race.load_laps()


def get_seasons():
    pass

def get_tracks_in_season():
    pass

def get_drivers_on_track_season():
    pass

def get_driver_finishing_standings():
    pass


if __name__ == "__main__":
    print(fetch_day(2020))
