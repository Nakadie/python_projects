# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:34:32 2021

@author: Kamuela
"""
# take a url and return just the name of the website
def domain_name(url):
    split = url.replace('http://', '')
    split = url.replace('https://', '')
    
    split = split.split('.')
    if 'www' in split:
        return split[1]
    elif 'http' in split:
        return split[1]
    else:
        return split[0]
            
            
        

print(domain_name('https://google.co.jp'))
# # examples and expected answers.
# # ("http://google.com"), "google")
# # ("http://www.google.co.jp"), "google")
# # ("https://youtube.com"), "youtube")

# good example of generator comprehension. 
# def domain_name(url):
#     return string.replace('http://', '').replace('https://', '').split('.')['www' in string]
#def domain_name(url):
    # return url.split("//")[-1].split("www.")[-1].split(".")[0]