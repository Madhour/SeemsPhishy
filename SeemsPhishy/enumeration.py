from bs4 import BeautifulSoup
import requests
import random

from lib.user_agents import user_agents


class ENUMERATION:

    def __init__(self, company_name):
        self.company_name = company_name
        self.files = {} #{header-title : url}
        self.query_results = 0


    def getFiles(self):
        '''
        This function initiates the enumeration
        '''
        
        print("Searching for files at \"{}\"".format(self.company_name))
        
        self.query()
        
        print("files ", self.files)
        
        #if not self.files:
        #    print("No results found, try again!")
            
        return self.files


    def query(self):
        '''
        This function queries the bing search engine for all pdf-files of a company,
        using refined search operators.
        To navigate through the search engine results, the amount of results on a page are
        summed up and stored in `self.total_results`. This is then used to append the url to
        `&first=n`, where n is `self.total_results`. The bing search engine will then skip the
        first n results that were already seen and show the new results.
        To end the enumeration, the function keeps track of the results of the last page. If 
        the same results appeared twice, then end is reached. This is because choosing an 
        arbitrary large number for n in `&first=n` will always return the last bing search page.
        '''
        
        self.total_results = 0      # Total results found by search engine
        self.previous_results = []  # Keeps track of results on the previous page
        session = True

        while session:
            
            search_url = self.generateURL()
            
            url_header = {'User-Agent':random.choice(user_agents),  # Bing search engine requires user agent
                          'Accept-Language': 'en-US,en'}            # Receiving results in english unifies the scraping process
            
            resp = requests.get(search_url, headers=url_header)

            if resp.status_code == 200:
                current_links = self.resultsParser(resp)
                print("Found {} ({})".format(self.total_results, resp.request.url))
            elif resp.status_code != 200:
                print("Cannot fetch page")

            if (current_links == self.previous_results) or (self.total_results > 50):#checks if the current side has the same results as the previous, if yes then end of search is reached
                print("Reached end of search")
                session = False
                
            self.previous_results = current_links
        return


    def generateURL(self):
        ''' 
        Translates the refined search operators into a URL.
        '''
        return f'http://www.bing.com/search?q={self.company_name}+filetype:pdf&first={self.total_results}'


    def resultsParser(self, resp):
        '''
        Parses out the results of the bing response.
        '''
        results = []
        soup = BeautifulSoup(resp.content, 'lxml')
        
        for result in soup.findAll('li', {"class" : "b_algo"}):   #results are stored inside list with the class-name `b_algo`
            results.append(result)

        for result in results:
            self.total_results += 1
            try:
                if self.enumerateResults(result):
                    self.query_results += 1
                    
            except:
                pass
        
        return results


    def enumerateResults(self, result):
        '''
        This function processes found query results.
        '''
        header = result.a   # Header is stored inside <a> tag
        try:
            self.files[header.text] = header.attrs['href']

        except Exception as e:
            print("Error: {}".format(header.text))
            return False



