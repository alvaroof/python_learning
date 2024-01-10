# -*- coding: utf-8 -*-
import requests


class ApiClient:
    URL = "https://opentdb.com/api.php?amount=10&type=boolean"

    def fetch_questions(self):
        response = requests.get(self.URL)
        if response.status_code == 200:
            data = response.json()
            return data["results"]
        return []
