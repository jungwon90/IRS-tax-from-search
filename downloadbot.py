import os
import re
import requests
import urllib
from urllib import request
from bs4 import BeautifulSoup

class DownloadBot:
    """ This class is used for downloading PDFs of a tax form 
    with a range of years. """

    def __init__(self, form_name, min_year, max_year):
        self.form_name = form_name
        self.min_year = min_year
        self.max_year = max_year
    
    def download(self):
        """ Create a directory and download the PDFs in the directory. """

        form_number = "+".join(self.form_name.split(' '))
        url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value={form_number}&criteria=formNumber&resultsPerPage=200&isDescending=false'
        req = request.urlopen(url).read()
        soup = BeautifulSoup(req, "html.parser")
        results = soup.find('table', class_='picklist-dataTable')
        all_links = results.find_all('a', href=re.compile(r'(.pdf)'))
      
        # Filter the links with self.form_name, self.min_year and self.max_year
        filtered_links = self.get_filtered_links(all_links)

        dir_location = os.getcwd() + f"/{self.form_name}"
        # If there is no such directory, create one automatically
        if not os.path.exists(dir_location):
            os.mkdir(dir_location)

        # Download the pdf files to a specified location
        for link in filtered_links:
            full_file_name = os.path.join(dir_location, self.form_name + " - " + link["href"][-8:])
            with open(full_file_name, "wb") as f:
                f.write(requests.get(link['href']).content)
            


    def get_filtered_links(self, all_links):
        """ Filter the links passed in as parameter with class attributes
        and Return it. """

        filtered_links = []
        # Filter the links with self.form_name and self.year
        for link in all_links:
            # Extract the year from the link
            year = int(link["href"][-8:][:4])
            if (link.text == self.form_name) and (year >= self.min_year and year <= self.max_year):
                filtered_links.append(link)

        return filtered_links

    
