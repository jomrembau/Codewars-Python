import re

def domain_name(url):
    url = re.split(r"//|/|\.", url)
    for x in url:
        if x != "www" and x != "http:"and x != "https:":
            return x




print(domain_name("http://www.codewars.com/kata/"))