from selenium import webdriver
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver_path = 'C:\\Users\\shaguna awasthi\\Desktop\\WEB projects other\\googlePlacesScrape\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.google.com/maps/place/Gaiety+Heritage+Cultural+Complex+Shimla/@31.1046203,77.1714985,17z/data=!3m1!4b1!4m10!1m2!2m1!1samphitheater+shimla!3m6!1s0x390578936fe8021b:0xf78d4ba52f040fb6!8m2!3d31.1046157!4d77.1736872!9m1!1b1')

wait = WebDriverWait(driver, 10)

# review titles / username / Person who reviews

review_titles = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="pane"]/div/div[1]/div/div/div[2]/div[9]/div[1]/div/div[3]/div[2]/div/div/a/div[1]/span')))

review_titles = driver.find_elements_by_class_name("section-review-title ")
#print([a.text for a in review_titles])
#print("TITLE KHTM")

# review text / what did they thin'
#review_text = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="pane"]/div/div[1]/div/div/div[2]/div[9]/div[1]/div/div[3]/div[3]/div[2]/span[2]')))
review_text = driver.find_elements_by_class_name("section-review-text")


#print([a.text for a in review_text])

# get the number of stars

review_stars = driver.find_elements_by_class_name("section-review-stars")
stars=[]


for star in review_stars:
    active_stars = star.find_elements_by_class_name("section-review-star-active")
    stars.append(len(active_stars))


hi=[]
for i in range(len(review_text)):
    temp={}
    temp['name'] = review_titles[i].text
    #temp['date'] = values.postDate[i]
    temp['rate'] = stars[i]
    temp['review'] = review_text[i].text
    hi.append(temp)

for ele in hi:
    print(ele)
#first_review_stars = stars[0]
#for star in stars:
    #active_stars = star.find_elements_by_class_name("section-review-star-active")
    #print([a.text for a in active_stars])
    #print(f"the stars the first review got was {len(active_stars)}")