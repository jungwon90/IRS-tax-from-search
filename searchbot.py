import requests
from bs4 import BeautifulSoup


class IRSFormSearchBot:
    def __init__(self, form_name):
        self.form_name = form_name
        self.data = {}

    def search(self):
        form_number = "+".join(self.form_name.split(' '))
        url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value={form_number}&criteria=formNumber&resultsPerPage=200&isDescending=false'
        req = requests.get(url)
        # Create a Beautiful Soup object that takes HTML content
        soup = BeautifulSoup(req.content, "html.parser")
        results = soup.find('table', class_='picklist-dataTable')

        # Get all form numbers 
        form_numbers_elements = results.find_all('a')
        # a list of form_number strings
        form_numbers_list = self.get_from_numbers_list(form_numbers_elements) 
        
        # Get all form titles 
        form_titles_elements = results.find_all('td', class_='MiddleCellSpacer')
        # a list of strings of form titles
        form_titles_list = self.get_form_titles_list(form_titles_elements)
        
        # Get all years
        form_years_elements = results.find_all('td', class_='EndCellSpacer')
        # a list of strings of form-years
        form_years_list = self.get_form_years_list(form_years_elements)

        # Extract the only necessary data and append it to self.data
        self.set_data(form_numbers_list, form_titles_list, form_years_list)
        
        return self.data
    

    ## Helper Functions ##

    def get_from_numbers_list(self, form_nums_elements):
        form_nums_list = []
        for form_number in form_nums_elements[9:]:
            # Extract only the text content from the HTML element
            form_number = form_number.text
            form_nums_list.append(form_number)
        
        return form_nums_list
    
    def get_form_titles_list(self, form_titles_elements):
        form_titles_list = []
        for form_title in form_titles_elements:
            form_title = form_title.text.strip()
            form_titles_list.append(form_title)
        
        return form_titles_list

    def get_form_years_list(self, form_years_elements):
        form_years_list = []
        for form_year in form_years_elements:
            form_year = form_year.text.strip()
            form_years_list.append(int(form_year))
        
        return form_years_list
        
    def set_data(self, form_nums_list, form_titles_list, form_years_list):
        form_nums_match = []
        form_titles_match = []
        form_years_match = []
        try:
            for i in range(len(form_nums_list)):
                if form_nums_list[i] == self.form_name:
                    form_nums_match.append(form_nums_list[i])
                    form_titles_match.append(form_titles_list[i])
                    form_years_match.append(form_years_list[i])
            
            #update self.data
            self.data['form_number'] = form_nums_match[0]
            self.data['form_title'] = form_titles_match[0]
            self.data['min_year'] = min([year for year in form_years_match])
            self.data['max_year'] = max([year for year in form_years_match])
        except:
            print('Check the form names again!') 
    

# irsbot = IRSFormSearchBot("Form W-2")
# data = irsbot.search()
# print(data)