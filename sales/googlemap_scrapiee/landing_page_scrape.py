from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langchain.llms import Ollama
import time
import pandas as pd

service = Service("chromedriver.exe")
service = Service("chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
chrome_options.add_argument("--disable-notifications")  # Disable notifications
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
chrome_options.add_argument("--no-sandbox")  # No sandboxing (optional)
chrome_options.add_argument("--disable-images")  # Disable images to speed up loading
chrome_options.add_argument("--disable-javascript")  # Disable JavaScript if not needed
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
chrome_options.add_argument("--disable-notifications")  # Disable notification
driver = webdriver.Chrome(service=service, options=chrome_options)


content=[]
websites = [
    "http://aticoftworth.com/",
    "http://calivibessmokeshop.com/",
    "http://www.hybridsmokes.com/",
    "https://www.smokehubdistro.com/",
    "https://noveltywholesaledfw.com/",
    "https://www.monstersmokewholesale.com/",
    "https://ludicrousdistro.com/",
    "https://lakeworthcigar.com/",
    "https://kingcandle.us/",
]

for website in websites:
    try:
        driver.get(website)
        time.sleep(3)  # Wait for the page to load (adjust as needed)
        
        # Handle age verification
        try:
            # Example: Click an "Enter" button for age verification
            enter_button = driver.find_element(By.XPATH, '//button[contains(text(), "Enter")]')
            enter_button.click()
            time.sleep(3)  # Wait for the page to load after age verification
        except:
            print(f'No age verification needed or failed to bypass for {website}')
        
        # Extract main content while ignoring header and footer
        try:

            # Assuming main content is within a specific element, e.g., <div id="main-content">
            main_content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
            
            # Get the remaining content
            content_text = main_content.text

            content.append(content_text)

            print(f'Content: {content_text}')  # Print first 100 characters of content
            
        except Exception as e:
            pass
        
    except Exception as e:
        pass


ollama = Ollama(base_url="http://localhost:11434", model="mymdl")

trend_products=[ollama.invoke(raw_text) for raw_text in content]

dict={"website":websites,
      "Trending_Products": trend_products}

df=pd.DataFrame(dict)

df.to_excel("trending_products.xlsx", index=False)


