from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_links(url):
    driver.get(url)
    links = []
    time.sleep(5)
    buttons = ["session-i-filter", "session-ii-filter", "session-iii-filter"]
    for button in buttons:
        print(button)
        # Click button
        driver.find_element(By.ID, button).click()
        time.sleep(2)
    
        keep_going = True

        # Repeat until no new links are found
        while keep_going:
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0, {scroll_height});")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)

            new_links = 0
            element = driver.find_elements(By.CLASS_NAME, "poster-item")
            for e in element:
                elements = e.find_elements(By.TAG_NAME, "a")
                for el in elements:
                    href = el.get_attribute("href")
                    # If href does not end in .ics and does not contain "twitter"
                    if not href.endswith(".ics") and "twitter" not in href and href not in links:
                        links.append(href)
                        print(f"Added {href}")
                        new_links += 1

            print(f"Found {len(links)} links")
            print(f"New links: {new_links}")

            # Check if new links were found
            if new_links == 0:
                keep_going = False

    return links

driver = webdriver.Chrome(ChromeDriverManager().install())
links = get_links("https://www.world-wide.org/cosyne-23/")

poster_dict = {}

for link in links:
    driver.get(link)

    # Wait for page to load
    WebDriverWait(driver, 3).until(lambda d: d.find_element(By.ID, "poster-details-wrapper"))
    details = ['']
    while details == ['']:
        element = driver.find_element(By.ID, "poster-details-wrapper")
        details = element.text.split("\n")

    poster_details = {
        "title": details[0],
        "authors": details[1],
        "date": details[2].split('/')[1].strip().split(':')[1].strip(),
        "location": details[2].split('/')[2].strip(),
        "abstract": details[4],
        "url": link
    }

    poster_dict[poster_details['title']] = poster_details

driver.quit()

# Save poster_dict to json file
import json
with open('poster_dict.json', 'w', encoding='utf-8') as fp:
    json.dump(poster_dict, fp, ensure_ascii=False, indent=4)