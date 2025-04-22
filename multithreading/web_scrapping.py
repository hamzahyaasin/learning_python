'''
A use-case scenario of multithreading using web scrapping.
as these tasks are I/O bound, we can use multithreading to speed up the process.
'''

'''
These are the three different urls i am going to scrap

https://python.langchain.com/docs/tutorials/

https://python.langchain.com/docs/concepts/

https://python.langchain.com/docs/introduction/


'''

import threading 
import requests
from bs4 import BeautifulSoup

urls = ['https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/concepts/',
'https://python.langchain.com/docs/introduction/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
    

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    thread.start()
    threads.append(thread) 
    
for thread in threads:
    thread.join()
    
print('All web pages fetched')




