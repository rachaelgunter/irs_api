import requests 
from requests_html import HTMLSession
import json

session = HTMLSession()

def pinwheel_query(terms):
    dict = {
            "form_number": "",
            "form_title": "",
            "min_year": "",
            "max_year": ""
        }

    def search_irs(terms):
        params = str(terms)
        # terms = "".join(terms)
        # print(terms)
        # params = "+".join(terms)
        print(params)
        # search_by_title = '&criteria=title&submitSearch=Find'
        search_by_title = f'?value={params}&criteria=title&submitSearch=Find'

        try:
            # url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
            # url with session
            url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html;jsessionid=Il6d7TJ1xhxsV5gDw_wsC_cZ.21'
            response = session.get(url + search_by_title)
            # response = session.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
            print(response.html)


            # how to get the form number from the response
            nums = response.html.find(".LeftCellSpacer")
            for num in nums:
                # print(page.text)
                form_num = num.text
            
            print("form num", form_num)
            dict["form_number"] = form_num

            # how to get the title from the resonse
            titles = response.html.find(".MiddleCellSpacer")
            for title in titles:
                # print(title.text)
                form_title = title.text

            print("form title", form_title)
            dict["form_title"] = form_title

            # how to get the min year from the response
            

            # how to get the max year from the response
            max_years = response.html.find(".EndCellSpacer")
            for m_year in max_years:
                # print(m_year.text)
                max_year = m_year.text

            print("max year", max_year)
            dict["max_year"] = max_year

            print(dict)
            # pages = response.html.find(".LeftCellSpacer")
            # for page in pages:
            #     print(page.text)

            # pdf_elements = response.html.find("a[href$='.pdf']")
            # print(pdf_elements)
            # for each in pdf_elements:
            #     print(each.absolute_links)
                # print()


        except requests.exceptions.RequestException as e:
            print(e)

    def jay_soning(dict):
        final_json = json.dumps(dict)
        print(final_json)
    jay_soning(dict)



print("calling", pinwheel_query("new+york"))




# when queried download the pdf and ad to a subfolder 