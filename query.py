import requests 
from requests_html import HTMLSession
import json

session = HTMLSession()

def pinwheel_query(terms):
    list = [{
            "form_number": "",
            "form_title": "",
            "min_year": 0,
            "max_year": 0
        }]
    print(terms)

    def url_search_term(terms):
        params = ""
        for term in terms:
            if term !=  " ":
                params += term
            if term == " ":
                params += "+"
        return params

    params = url_search_term(terms)
    print(params)

    def search_irs(params):
        print(params)
        search_by_title = f'?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&value={params}&criteria=formNumber&submitSearch=Find&isDescending=false'
        try:
            # url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
            url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html;jsessionid=Il6d7TJ1xhxsV5gDw_wsC_cZ.21'
            response = session.get(url + search_by_title)
            # response = session.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
            print(response.html)


            # select class where the form numbers exist
            forms_odd = response.html.find(".odd")
            forms_even = response.html.find(".even")
            forms = forms_odd + forms_even
            # print(len(forms))
            for form in forms:
                # forms_prod_nums = response.html.find(".LeftCellSpacer")
                elements = form.text.split('\n')
                name = elements[0]
                des = elements[1]
                yr = int(elements[2])
                if name == terms:

                    # how to get the form number from the response
                    # print("form num", form_num)
                    list[0]["form_number"] = name
                    # print(list[0])

                    # how to get the max year from the response
                    # max_years = response.html.find(".EndCellSpacer")
                    # # print(max_years)
                    # for m_year in max_years:
                    #     # print(m_year.text)
                    #     max_year = m_year.text
                    if list[0]["max_year"] < yr:

                    # print("max year", max_year)
                        list[0]["max_year"] = yr
                    else:
                        pass
                    
                    if list[0]["max_year"] > yr:
                        list[0]["min_year"] = yr

                    # how to get the title from the resonse
                    # titles = response.html.find(".MiddleCellSpacer")
                    # for title in titles:
                    #     # print(title.text)
                    #     form_title = title.text

                    # print("form title", form_title)

                    list[0]["form_title"] = des

                    # how to get the min year from the response
                    # if year is less than max year
                    # min year == year
                    


                    # pages = response.html.find(".LeftCellSpacer")
                    # for page in pages:
                    #     print(page.text)
                
                else:
                    pass

            print(list[0])
        except requests.exceptions.RequestException as e:
            print(e)

    search_irs(params)

    # def jay_soning(dict):
    #     final_json = json.dumps(dict)
    #     print(final_json)
    # jay_soning(dict)



print("calling", pinwheel_query("Form W-2"))




# when queried download the pdf and ad to a subfolder 