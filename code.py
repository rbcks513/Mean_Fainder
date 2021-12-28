from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import csv 
import datetime

def main():
    now = datetime.datetime.now()
    today = str(now.month) + str(now.day)
    f = open("voca.csv", "r")
    new = open(today+"mean.csv", "w")
    new = open(today+"mean.csv", "a")
    reader = csv.reader(f)
    voca = {}
    n = 0
    for row in reader:
        temp = row[0]
        voca[n] = temp
        if ( n != 0): 
            means = Find_in_dictionary(voca[n])
            data = (row[0] + ", " + means+"\n")
            new.write(data)
        n = n + 1
        
        
    f.close()
 
        

def Find_in_dictionary(voca):
    dictionary_url = "https://dict.naver.com/search.dict?mode=all&query_euckr=&query=%s"%voca
    #dictionary_url = 'https://en.dict.naver.com/#/search?query=%s&range=all'%voca
    
    asd = urllib.request.urlopen(dictionary_url)

    a = BeautifulSoup(asd, 'html.parser')
    mean = a.find("dl", class_ = "dic_search_result")
    temp = ""
    for mn in mean.find("dd"):
        m = mn.string
        if(m == None): continue
        k = m.strip()
        temp = temp +" "+ k
      
        
    return temp
        


if __name__ == '__main__':
    main()