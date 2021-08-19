import requests
from bs4 import BeautifulSoup

class Focloir:
    def format_term(self, term):
        formatted_string = ""
        words = term.split(" ")
        #if only 1 word, formatting not needed
        if len(words) == 1:
            return term
        for word in words:
            if not words.index(word) == len(words) - 1:  #if it isn't the last word
                formatted_string = word + "+"
            else:
                formatted_string += word

        return formatted_string

    def get_translation(self, term):
        url = "https://www.focloir.ie/en/dictionary/ei/" + self.format_term(term)
        page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}) 
        results = self.parse_results(page)
        
        return results

    def parse_results(self, page):
        all_word_forms = []
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("span",class_="cit_translation")
        for result in results:
            all_word_forms.append(result.find("span", class_="quote").text)
        
        return all_word_forms

def main():
    focloir = Focloir()
    print(focloir.get_translation("Hello"))
if __name__ == "__main__":
    main()