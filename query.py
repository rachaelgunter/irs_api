import requests 
from requests_html import HTMLSession
import json

session = HTMLSession()

def pinwheel_query(*terms):
    list_to_json = []

def pdf_query(form_title, years):
    term = form_title

def parse_years(years):
    low, high = years.split("-")

def pdf_traversal(term):
    search_term = format_search_terms_list(term)
    params = search_term_url(search_terms)
    response = search_irs(params)
    download_pdfs(response)

    def add_dicts_to_list(dict):
        list_to_json.append(dict)

    def format_to_json(list):
        return json.dumps(list)

    def traverse_list(search_terms):
        for term in search_terms:
            param = search_term_url(term)
            response = search_irs(param)
            format_response(response, term)

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

    def download_pdfs(response):
        pdf_list = []
        forms_odd = response.html.find(".odd")
        forms_even = response.html.find(".even")
        forms = forms_odd + forms_even
        for form in forms:
            pdf = form.links
            information = form.text.split('\n')
            form_number = information[0]
            year = int(information[2])
            if form_number == term and low <= year >= high:
                pdf_list.append(pdf)
        print(pdf_list)

    def format_response(response, term):
        info_dict = {
            "form_number": "",
            "form_title": "",
            "min_year": 0,
            "max_year": 0
            }
        forms_odd = response.html.find(".odd")
        forms_even = response.html.find(".even")
        forms = forms_odd + forms_even
        for form in forms:
            information = form.text.split('\n')
            form_number = information[0]
            form_title = information[1]
            year = int(information[2])
            if form_number == term:
                if info_dict["form_number"] == form_number and info_dict["form_title"] == form_title:
                    if year >= info_dict["max_year"]:
                        info_dict["max_year"] = year
                    elif year <= info_dict["max_year"] and year <= info_dict["min_year"]:
                        info_dict["min_year"] = year
                    elif year >= info_dict["min_year"]:
                        pass                      
                else:
                    info_dict["form_number"] = form_number
                    info_dict["form_title"] = form_title
                    info_dict["min_year"] = year
                    info_dict["max_year"] = year
        else:
            pass
        add_dicts_to_list(info_dict)
        

    def search_irs(params):
        search_by_title = f'?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&value={params}&criteria=formNumber&submitSearch=Find&isDescending=false'
        try:
            # url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
            url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html;jsessionid=Il6d7TJ1xhxsV5gDw_wsC_cZ.21'
            response = session.get(url + search_by_title)
            # print(response.html)
        except requests.exceptions.RequestException as e:
            print(e)
        return response

    
    search_terms_list = format_search_terms_list(terms)
    traverse_list(search_terms_list)
    format_to_json(list_to_json)




print("pdfffff", pdf_query("Form W-2", "2018-2020"))



# print("calling", pinwheel_query("Form W-2", "Form 1095-C"))




# when queried download the pdf and ad to a subfolder 