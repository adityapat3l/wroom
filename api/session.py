from config.fixtures import ERGAST_BASE_API
from utils import requests


class Season:
    def __init__(self, year):
        self.year = year
        self.base_url = f"{ERGAST_BASE_API}/{self.year}.json"

    def get_season_details(self):
        return requests.parse_url(self.base_url)


class Session:

    def __init__(self):
        pass


if __name__ == '__main__':
    print(Season(2021).get_season_details())