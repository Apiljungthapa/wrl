from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException, NoSuchWindowException, NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


def search(location, store_type,driver):

    try:
        
        # Search for the location
        place = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="searchboxinput"]'))
        )
        place.send_keys(location)
        submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="searchbox-searchbutton"]'))
        )
        submit.click()
        time.sleep(5)
        
        # Search for the store type
        place = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="searchboxinput"]'))
        )
    
        place.clear()
        place.send_keys(store_type)
        submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="searchbox-searchbutton"]'))
        )
        submit.click()
        time.sleep(8)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
shop = []
shop_address = []
shop_phone_number = []
shop_website = []
shop_category = []
shop_ratings = []
shop_reviews = []


with open("scrape_input.txt", "r") as f:
    
    location = f.readline().strip()
    
    search_keyword = f.readline().strip()

# Set to track processed shops
processed_shops = set()

def findshopss(driver):
    try:
        # Click to open the menu list of shops
        menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/a'))
        )
        menu_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="feed"]'))
        )

        # Scroll to load more content
        scrollable_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
        last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)

        while True:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="feed"]'))
            )
            time.sleep(2)  # Add sleep to ensure content loads properly
            new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
            if new_height == last_height:
                break
            last_height = new_height

        # Find all shop menu items
        shop_menus = driver.find_elements(By.CLASS_NAME, "Nv2PK")
        print(f"Number of shop menus found: {len(shop_menus)}")  

        for menu in shop_menus:
            shop_name = menu.text
            if shop_name in processed_shops:
                continue  # Skip already processed shops

            try:
                # Click on the shop menu item
                driver.execute_script("arguments[0].scrollIntoView(true);", menu)
                ActionChains(driver).move_to_element(menu).click().perform()
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'DUwDvf.lfPIob'))
                )

                # Add to processed shops
                processed_shops.add(shop_name)
                
                href_value = "N/A"
                contact = "N/A"
                loca = "N/A"
                rate = 'N/A'
                review = "N/A"
                stype = "N/A"

                # For shop name
                try:
                    shop_ = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/h1')
                    shop_name = shop_.text
                except NoSuchElementException:
                    pass
                shop.append(shop_name)

                # For shop type
                try:
                    All_shop_type = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/span[1]/span/button')
                    stype = All_shop_type.text
                except NoSuchElementException:
                    pass
                shop_category.append(stype)

                # For ratings
                try:
                    All_shop_ratings = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]')
                    rate = All_shop_ratings.text
                except NoSuchElementException:
                    pass
                shop_ratings.append(rate)

                # For total reviews 
                try:
                    All_shop_reviews = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[2]/span/span')
                    review = All_shop_reviews.text
                except NoSuchElementException:
                    pass
                shop_reviews.append(review)

                # For address
                try:
                    All_shop_address = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[9]/div[3]/button/div/div[2]/div[1]')
                    loca = All_shop_address.text
                except NoSuchElementException:
                    pass
                shop_address.append(loca)

               

                # For website
                try:
                    All_shop_website = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[9]/div[5]/a/div/div[2]')
                    href_value = All_shop_website.text
                except NoSuchElementException:
                    pass
                shop_website.append(href_value)

                # For phone number
                try:
                    All_shop_number = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[9]/div[6]/button/div/div[2]/div[1]')
                    contact = All_shop_number.text
                except NoSuchElementException:
                    pass
                shop_phone_number.append(contact)

                # Add some delay between processing shops to avoid issues
                time.sleep(3)

            except ElementClickInterceptedException:
                print("Element click intercepted, retrying...")
                time.sleep(2)
                continue
                
            except StaleElementReferenceException:
                print("Stale element reference exception, retrying...")
                time.sleep(2)
                continue

    except Exception as e:
        
        print(f"An error occurred in findshopss: {e}")
        
    # return shop, shop_address, shop_phone_number, shop_website, shop_category, shop_ratings, shop_reviews, img_url


def scrape(location, search_keyword):
    
    service = Service(executable_path=r"C:\Users\apil xetri\OneDrive\Desktop\SCRAP_SELENIUM\chromedriver.exe")

    driver = webdriver.Chrome(service=service)

    driver.get("https://www.google.com/maps")
    
    search(location, search_keyword, driver)
    
    findshopss(driver)
    
    driver.quit()
  
    

    # Save to CSV
    df = pd.DataFrame({
        'Shop Name': shop,
        'Category': shop_category,
        'Address': shop_address,
        'Phone Number': shop_phone_number,
        'Website': shop_website,
        'Ratings': shop_ratings,
        'Reviews': shop_reviews,
    })
    

    df.to_csv(f"{location}_{search_keyword}_shops.csv", index=False)
    
    print("Data saved successfully")


    # # Save the data to a CSV file
    # df = pd.DataFrame({
    #     'Shop Name': shop,
    #     'Category': shop_category,
    #     'Address': shop_address,
    #     'Phone Number': shop_phone_number,
    #     'Website': shop_website,
    #     'Ratings': shop_ratings,
    #     'Reviews': shop_reviews,
    #     'Image URL': img_url
        
    # })
 
    # df.to_csv(f"{location}_{search_keyword}_shops.csv", index=False)
    
    # print("Successfully Saved !..")
   

if __name__ == "__main__": 
       
    scrape(location, search_keyword)
              
