import requests 
from requests_html import HTMLSession
import json
import os

session = HTMLSession()

# initial intake of params given in the first query
# takes a list of form names 
list_to_json = []

def pinwheel_query(*terms):
    search_terms_list = format_search_terms_list(terms)
    traverse_list(search_terms_list)
    JSON = format_to_json(list_to_json)
    
    return JSON

# initial intake of params given in the second query
# takes in a form name and a range of years
def pdf_query(form_title, years):
    term = form_title
    low, high = years.split("-")
    pdf_traversal(term, low, high)

# traverses the steps to query for the second style query
def pdf_traversal(term, low, high):
    search_term = format_search_terms_list(term)
    param = search_term_url(search_term)
    response = search_irs(param)
    pdf_dict = compile_pdf_list(response, term, low, high)
    make_directory(pdf_dict)

# appends all of the dict information to a list
def add_dicts_to_list(dict):
    list_to_json.append(dict)

# formats the list of dicts to JSON format
def format_to_json(list):
    j_son = json.dumps(list)
    return j_son

# traverses the steps to query for the first style query
def traverse_list(search_terms):
    print(len(search_terms))
    for term in search_terms:
        print("term",term)
        param = search_term_url(term)
        response = search_irs(param)
        format_response(response, term)

# takes a list of form names and breaks them down into seperate strings
def format_search_terms_list(terms):
    search_terms = []
    if len(terms) > 1:
        for term in terms:
            search_terms.append(term)
    else: 
        str = ''
        for item in terms:
            term = str + item
            search_terms.append(term)
            return search_terms
    return search_terms   

# formats the term to make it useful to complete the url
def search_term_url(terms):
    params = ""
    for term in terms:
        if term !=  " ":
            params += term
        if term == " ":
            params += "+"
    return params

# compiles a list of pdfs matching the query parameters 
def compile_pdf_list(response, term, low, high):
    pdf_dict = {}
    forms_odd = response.html.find(".odd")
    forms_even = response.html.find(".even")
    forms = forms_odd + forms_even
    low = int(low)
    high = int(high)
    for form in forms:
        pdf = form.links
        pdf = str(pdf)
        information = form.text.split('\n')
        form_number = information[0]
        year = int(information[2])
        if form_number == term and low <= year <= high:
            pdf_dict[f"{term} - {year}"] = pdf[2:-2]
    return pdf_dict

# makes a directory with the queried pdfs
def make_directory(dictionary):
    for form, p in dictionary.items():
        form_name = form.split(" -")[0]
        year = form.split("- ")[-1]

        url = p
        response = requests.get(url)

        if not os.path.exists(form_name):
            os.mkdir(form_name)

        with open(f"{form_name}/{form}.pdf", "wb") as f:
            f.write(response.content)


# formats the response given from the api query and saves the information to a dict
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

    
# uses given params to search the irs api
def search_irs(params):
    search_by_title = f'?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&value={params}&criteria=formNumber&submitSearch=Find&isDescending=false'
    try:
        url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html;jsessionid=Il6d7TJ1xhxsV5gDw_wsC_cZ.21'
        response = session.get(url + search_by_title)
    except requests.exceptions.RequestException as e:
        print(e)
    return response


print(pinwheel_query("Form W-2 P", "Form 1095-C"))

pdf_query("Form W-2", "2018-2020")