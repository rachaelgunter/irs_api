import requests 
from requests_html import HTMLSession
import json

session = HTMLSession()

def pinwheel_query(*terms):

    def format_search_terms_list(terms):
        search_terms = []
        for term in terms:
            search_terms.append(term)
        return search_terms   

    def search_term_url(terms):
        params = ""
        for term in terms:
            if term !=  " ":
                params += term
            if term == " ":
                params += "+"
        return params

    to_json = []
    def add_lists(dicts):
        to_json.append(dicts)

    def search_irs(params, term):
        dict = {
            "form_number": "",
            "form_title": "",
            "min_year": 0,
            "max_year": 0
        }
        search_by_title = f'?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&value={params}&criteria=formNumber&submitSearch=Find&isDescending=false'
        try:
            # url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
            url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html;jsessionid=Il6d7TJ1xhxsV5gDw_wsC_cZ.21'
            response = session.get(url + search_by_title)
            # print(response.html)

            forms_odd = response.html.find(".odd")
            forms_even = response.html.find(".even")
            forms = forms_odd + forms_even
            for form in forms:
                information = form.text.split('\n')
                form_number = information[0]
                form_title = information[1]
                year = int(information[2])
                if form_number == term:
                    if dict["form_number"] == form_number and dict["form_title"] == form_title:
                        if year >= dict["max_year"]:
                            dict["max_year"] = year
                        elif year <= dict["max_year"] and year <= dict["min_year"]:
                            dict["min_year"] = year
                        elif year >= dict["min_year"]:
                            pass                        
                    else:
                        dict["form_number"] = form_number
                        dict["form_title"] = form_title
                        dict["min_year"] = year
                        dict["max_year"] = year
            else:
                pass
        except requests.exceptions.RequestException as e:
            print(e)
        add_lists(dict)
        return dict

    def traverse_list(search_terms):
        for term in search_terms:
            param = search_term_url(term)
            returned_info = search_irs(param, term)

    def jay_soning(dict):
        final_json = json.dumps(dict)
        print(final_json)

    search_terms_list = format_search_terms_list(terms)

    list_for_json = traverse_list(search_terms_list)
    jay_soning(to_json)

  



print("calling", pinwheel_query("Form W-2", "Form 1095-C"))






# when queried download the pdf and ad to a subfolder 