
import requests
from credentials import language, app_key, app_id


class Dictionary:
    def __init__(self, app_id, app_key, language):
        self.app_id = app_id
        self.app_key = app_key
        self.language = language
    
    def search_word(self, word):
        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + self.language + "/" + word.lower()
        request = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
        if request.status_code == 404:
            print('Word was not found, check spelling or try another word!!!!')
            return None
        else:
            return request

    @staticmethod    
    def clean_data(response):
        r = {}
        response = response.json()
        r['etymologies'] = response['results'][0]['lexicalEntries'][0]['entries'][0]['etymologies'][0]
        r['definitions'] = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        try:
            r['examples'] = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']
        except:
            r['examples'] = None
        return r

    
