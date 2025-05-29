import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_images(shop_name):
    
    
    driver = webdriver.Chrome(service=Service(executable_path=r"C:\Users\apil xetri\OneDrive\Desktop\SCRAP_SELENIUM\chromedriver.exe"))
    driver.maximize_window()
    driver.get("https://www.google.com/maps")
    
    try:
        # Locate search box and enter the shop name
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/form/input"))
        )
        
        search_box.clear()
        search_box.send_keys(shop_name)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for the results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]"))
        )

        image_links = []
        
        # Try to click on the first product and then on "See all images"
        try:
            first_product = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/a"))
            )
            first_product.click()

            # Wait for the details page and click the "See all images" button
            see_all_images_button_details = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[1]/div[1]/button"))
            )
            see_all_images_button_details.click()

        except Exception as e:
            print(f"Error clicking product or 'See all images' button from details page: {e}")
            # Directly click on the 'See all images' button if the first approach fails
            try:
                see_all_images_button_direct = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button"))
                )
                see_all_images_button_direct.click()
            except Exception as e:
                print(f"Error clicking 'See all images' button directly: {e}")

        # Wait for images to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]"))
        )
        
        while len(image_links) < 10:
            try:
                image_container = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]"))
                )
                
                images = image_container.find_elements(By.XPATH, ".//a/div[1]")
                
                for image in images:
                    if len(image_links) >= 10:
                        break
                    
                    img_src = image.get_attribute("style").split('("')[1].split('")')[0]
                    if img_src and img_src != '//:0' and img_src not in image_links:
                        image_links.append(img_src)
                
                # Scroll to load more images
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", image_container)
                time.sleep(2)  # Wait for more images to load

            except Exception as e:
                print(f"Error during image collection: {e}")
                break
            
        # Replace any '//:0' in the image links with 'NaN'
        image_links = [img if img != '//:0' else 'NaN' for img in image_links]
        
        # Save image links to CSV
        with open("finally_nepa_testing_sir.csv", 'w', newline='') as csvfile:
            
            writer = csv.writer(csvfile)
            writer.writerow(['Shop Name', 'Image URL'])
            
            for img_url in image_links:
                
                writer.writerow([shop_name, img_url])   
        
        driver.quit()
        
        return image_links

    except Exception as e:
        print(f"Error scraping images for {shop_name}: {e}")
        driver.quit()
        return []

    finally:
        logging.info(f"Images for {shop_name}:")
        for img in image_links:
            logging.info(img)
