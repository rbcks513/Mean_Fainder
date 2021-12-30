from bs4 import BeautifulSoup
import urllib.request
import csv 
import datetime

def main():
    now = datetime.datetime.now()
    today = str(now.month) + str(now.day)
    f = open("voca.csv", "r")
    
    #this program make new file once a day 
    #thus we do not have to check whether file exsit or not
    new = open(today+"mean.csv", "w")
    new = open(today+"mean.csv", "a")
    reader = csv.reader(f)
    voca = {}
    n = 0
    
    for row in reader:
        temp = row[0]
        voca[n] = temp
        
        if ( n != 0): 
            means = find_in_dictionary(voca[n])
            
    #Replace coma in sentance to dot
            coma = ","
            for x in range(len(coma)):
                means = means.replace(coma[x],".")
    
            data = (row[0] + ", " + means+"\n")
            new.write(data)
        n = n + 1
    #Show how many cycles been carried out
        print("No.%d cycle clear"%n)
        
    f.close()
    new.close()
        
def find_in_dictionary(voca):
    #Naver dicitionary has two different url, one can be accessed, other cannot be accessed.
    dictionary_url = "https://dict.naver.com/search.dict?mode=all&query_euckr=&query=%s"%voca
    #dictionary_url = 'https://en.dict.naver.com/#/search?query=%s&range=all'%voca
    
    requsted_url = urllib.request.urlopen(dictionary_url)

    bs_obj = BeautifulSoup(requsted_url, 'html.parser')
    
    #dl is html tag
    dl = bs_obj.find("dl", class_ = "dic_search_result")
    
    #temp will contain factor in the list
    temp = ""
    
    #Select in tag 'dd'
    for mn in dl.find("dd"):
        m = mn.string
        if(m == None): continue
        k = m.strip()
        temp = temp +" "+ k
    return temp

if __name__ == '__main__':
    main()