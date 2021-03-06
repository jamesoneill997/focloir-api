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

    def translate(self, term):
        url = "https://www.focloir.ie/en/dictionary/ei/" + self.format_term(term)
        #setting headers spoofs a browser session
        page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}) 
        results = self.parse_results(page)
        
        return results

    def parse_results(self, page):
        all_word_forms = {}
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("span", class_="sense", limit=3)
        
        for result in results:
            translation = self.get_translation(result)
            #skip unwanted tranlslations
            if translation == None:
                continue
            all_word_forms[translation] = []
            context = self.get_context(result)
            type = self.get_type(result)
            decl = self.get_declension(result)
            gender = self.get_gender(decl)
            example = self.get_example(result)
            all_word_forms[translation].append({"context":context, "type":type, "declension":decl, "gender":gender, "example":example})

        return all_word_forms

    def get_translation(self, result):
        try:
            translation = result.find("span",class_="cit_translation")
            result = translation.find("span", class_="quote").text
        except AttributeError:
            return None
            
        return result
        
    def get_context(self, result):
        try:
            context = result.find("span",class_="EDMEANING")
            ctx = context.text
        except AttributeError:
            ctx = "Undefined"
        return ctx
    
    def get_type(self, result):
        try:
            type = result.find("span", class_="pos").text
        except AttributeError:
            type = "Undefined"
        return type

    def get_declension(self, result):
        try:
            declension = result.find("span", class_="lbl_black_i")
            decl = declension.text
        except AttributeError:
            decl = "Undefined"
        return decl
    
    def get_gender(self, decl):
        return decl if decl == "Undefined" else decl[:-1]
    
    def get_example(self, result):
        try:
            example = result.find("span", class_="cit_example")
            ex = example.find("span", class_="quote").text
        except AttributeError:
            ex = "None"
        return ex