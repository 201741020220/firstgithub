import requests
from bs4 import BeautifulSoup
import time

t1=time.time()
r = requests.get('http://www.shuhai.com/shuku/0_145_0_0_0_2_0_2.html')


c = r.text


soup = BeautifulSoup(c,'html.parser')
page_div = soup.find('div',{'class':'page3'})
page = page_div.find_all('a')[-2].text
books=[]
for i in range(2, 4):
    url='http://www.shuhai.com/shuku/0_145_0_0_0_2_0_'+str(i)+'.html'
    p_r=requests.get(url)
    p_c=p_r.text
    p_soup=BeautifulSoup(p_c,'html.parser')
    alll=p_soup.find_all('div',{'class':'one-book'})
       
    for book in alll:
        bookDic={}
        bookDic['pic']=book.find('div',{'class':'book-cover-wrapper radius'}).find('a').find('img')['src']
        bookDic['name']=book.find('div',{'class':'book-name'}).find('a').text
        bookDic['intro']=book.find('div',{'class':'book-intro cl6e'}).text
        books.append(bookDic)
t2=time.time()
print(books)
print(t2-t1)