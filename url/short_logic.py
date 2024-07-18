from url.models import Url_Map
import random
import string
import re
class url :
    def __init__(self, url: str):
        self.url = url
        self.shorten_url = None
    def get_info(self) :
        return [ self.url, self.shorten_url]
    def generate_shorten_url(self) :
        def generate_random_string(length): # function generate random string of leters and digits
            letters = string.ascii_letters
            return ''.join(random.choice(letters) for i in range(length))
        test_existance = Url_Map.objects.filter(url=self.url)
        if test_existance.exists():
            exist = test_existance.first()
            self.shorten_url = exist.url_shorten
        else:
            # Generate a new shorten_url
            self.shorten_url = f"http://127.0.0.1:8000/url_shortener/task1/{generate_random_string(7)}"
            loop = True 
            while loop:
                if Url_Map.objects.filter(url_shorten=self.shorten_url).exists():
                    self.shorten_url = f"http://127.0.0.1:8000/url_shortener/task1/{generate_random_string(7)}"
                else:
                    loop = False
    def save (self) : # save the url and the shorten_url in the database 
        url = Url_Map(url = self.url , url_shorten=self.shorten_url)
        url.save() 
    def validation(self) :  #  return True is the url is valide 
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, self.url) is not None
    def url_from_shorten_url(self,shorten_url):
        urls_map = Url_Map.objects.filter(url_shorten=shorten_url)
        if urls_map.exists():
            url_map = urls_map.first()
            self.url = url_map.url 
            self.shorten_url = url_map.url_shorten
            return self.url
        else:
            return None 
            
        