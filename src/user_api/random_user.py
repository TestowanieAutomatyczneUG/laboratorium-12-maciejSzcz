import requests

class RandomUser:
    def __init__(self):
        self.url = 'https://randomuser.me/api/'

    def get_user(self):
        res = requests.get(self.url)

        return res.json()["results"][0]

    def get_user_with_gender(self, gender):
        if type(gender) != str:
            raise TypeError("gender must be of string type")
        elif gender != "male" and gender != "female":
            raise ValueError("gender must be male or female")

        res = requests.get(f'{self.url}?gender={gender}')
        
        return res.json()["results"][0]

    def get_user_with_nationality(self, nationality):
        possible_nationalities = ['AU', 'BR', 'CA', 'CH', 'DE', 'DK', 'ES', 'FI', 'FR', 'GB', 'IE', 'IR', 'NO', 'NL', 'NZ', 'TR', 'US']
        if type(nationality) != str:
            raise TypeError("nationality must be of string type")
        elif nationality not in possible_nationalities:
            raise ValueError("nationality not recognized")

        res = requests.get(f'{self.url}?nat={nationality}')
        
        return res.json()["results"][0]