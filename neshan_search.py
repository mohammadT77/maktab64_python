import requests

search_location_api_url = "https://api.neshan.org/v1/search"
# Authentication API token
api_key = "service.TRYQqR6tuZMPTsJ40x3YCygDm2V5t6GudAZwngTG"


params = {
   'term': 'اکبر',
   'lat': 36.2880443,
   'lng': 59.615743,
}

resp = requests.get(search_location_api_url, params=params,
                    headers={'Api-key': api_key})
print(resp.json())
