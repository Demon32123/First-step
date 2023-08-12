from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()
browser.get('https://www.citilink.ru/catalog/')
links = browser.find_elements(By.CSS_SELECTOR, 'a.CatalogLayout__link_level-1.Link.js--Link.Link_type_default')

for link in links:
    # try:
    browser.get(f'{link.get_attribute("href")}')
    # except StaleElementReferenceException:
    #     pass

    blocks = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-5wty15.e113kmgh0')
    for block in blocks:
        try:
            next_page_url = block.get_attribute('href')
            browser.get(next_page_url)
        except StaleElementReferenceException:
            pass

        sleep(1)
        pagination_blocks = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-peotpw.e1mnvjgw0')

        for pagination_block in range(2, int(pagination_blocks[-2].text) + 1):

            try:
                sleep(2)
                elements1 = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-9gnskf.e1259i3g0')
                elements2 = browser.find_elements(By.CSS_SELECTOR,
                                                  'span.e1j9birj0.e106ikdt0.app-catalog-j8h82j.e1gjr6xo0')
                print(elements1)
                print(elements2)
                browser.get(f'https://www.citilink.ru/catalog/smartfony/?p={pagination_block}')
                print(pagination_block)
            except StaleElementReferenceException:
                pass
        pagination_blocks.clear()


browser.close()
