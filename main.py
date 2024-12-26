from selenium import webdriver
from selenium.webdriver.common.by import By
import pyttsx3
import time

# Set up TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def fetch_google_sports_commentary(driver):
    try:
        # Locate the live commentary container
        commentary_elements = driver.find_elements(By.CSS_SELECTOR, ".imspo_cmt__cmt-ov-con.imso-regular-font")
        # Extract text from the elements
        commentary = [element.text for element in commentary_elements]
        return commentary[-1] if commentary else "No live commentary available."
    except Exception as e:
        return f"Error fetching commentary: {e}"

def speak_commentary(commentary):
    engine.say(commentary)
    engine.runAndWait()

if __name__ == "__main__":
    print("Starting Google Sports Commentary Scraper...")
    
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--disable-gpu')  # Disable GPU for headless
    options.add_argument('--no-sandbox')  # Bypass OS-level restrictions
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.google.com/search?q=aus+v+ind&sourceid=chrome&ie=UTF-8#cobssid=s&sie=m;/g/11vysh7rwr;5;/m/021q23;cm;fp;1;;;")
        time.sleep(5)  # Allow the page to load
        
        last_commentary = ""
        while True:
            commentary = fetch_google_sports_commentary(driver)
            if commentary and commentary != last_commentary:
                print("New Commentary:", commentary)
                speak_commentary(commentary)
                last_commentary = commentary
            time.sleep(30)  # Fetch updates every 30 seconds
    
    except KeyboardInterrupt:
        print("Exiting...")
    
    finally:
        driver.quit()
