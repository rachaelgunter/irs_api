import requests 
from requests_html import HTMLSession
import json

# session = HTMLSession()

def search_irs(params):
    params = "+".join()
    search_by_title = '&criteria=title&submitSearch=Find'
    try:
        url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
        response = requests.get(url + params + search_by_title)
        

        # , params=)

    #     params = {
    #     "form_number": ,
    #     "form_tite": ,
    #     "min_year": ,
    #     "max_year": 
    # }

    except requests.exceptions.RequestException as e:
        print(e)

# print("hello", search_irs.response.status_code)
print("response", search_irs.response())
# print("with params", search_irs(params))

"""
print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

"""




# when queried download the pdf and ad to a subfolder 