import selenium.webdriver as webdriver # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore

def scrape_website(website):
    print("Launching Chrome Browser...")

    chrome_driver_path = r"C:\Users\vikra\chromedriver.exe"  # Ensure this path is correct
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source

        return html
    finally:
        driver.quit()


website_url = "https://globalpolybags.com/"
html_content = scrape_website(website_url)

print(html_content)
def export_to_html_file(html_content, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)


export_to_html_file(html_content, 'global_polybags.html')

print("HTML content exported successfully.")
