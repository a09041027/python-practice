from selenium import webdriver
import time
import pandas as pd
#from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(8)
driver.get('https://www.baseball-reference.com/leagues/MLB/2019-schedule.shtml')
#soup = BeautifulSoup(driver.page_source,'lxml')
game = driver.find_elements_by_class_name('game')
#print(game.text)
a=list()
for i in range(len(game)):
    b= game[i].text
    a.append(b)
df = pd.DataFrame(a,columns=['Game Result'])
df.to_csv('2019schdule.txt',sep='\n',index=False)
time.sleep(5)
driver.close()
