from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pyttsx3

# Set up TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Configure Chrome options to handle SSL issues
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def speak_commentary(commentary):
    engine.say(commentary[8:])
    engine.runAndWait()

# Navigate to the target webpage
try:
    driver.get("https://www.google.com/search?q=aus+v+ind&sourceid=chrome&ie=UTF-8#cobssid=s&sie=m;/g/11vysh7rwr;5;/m/021q23;cm;fp;1;;;")
    print("Python tts commentry is staring ...")
    # Wait for the page to load (adjust if needed)
    print("waiting for page to load ...")
    driver.implicitly_wait(5)
    print("page loaded ...")
    # Locate the div or container that contains the tables
    container = driver.find_element(By.CLASS_NAME, "imso-ani.tb_cbg")
    divs = container.find_elements(By.TAG_NAME, "div")
    for div in divs:
        tables = div.find_elements(By.TAG_NAME, "table")
        print("Commentary ...")
        for table in tables:
            speak_commentary(table.text)
            print(table.text)

except Exception as e:
    print(f"An error occurred: {e}")

# Close the WebDriver
driver.quit()
