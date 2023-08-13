from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from fake_useragent import UserAgent

k = 0
urls = []

UA = UserAgent(verify_ssl=False)
agent = UA.random
print("USER AGENT: " + agent)
fire_opts = webdriver.FirefoxOptions()
fire_opts.add_argument("user_agent=" + agent)

browser = webdriver.Firefox(options=fire_opts)
browser.get('https://www.citilink.ru/catalog/')
sleep(2)
links = browser.find_elements(By.CSS_SELECTOR, 'a.CatalogLayout__link_level-1.Link.js--Link.Link_type_default')

for link in links:
    urls.append(link.get_attribute('href'))

for url in urls:
    browser.get(url)
    things = []
    blocks = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-5wty15.e113kmgh0')
    sleep(2)
    for block in blocks:
        things.append(block.get_attribute('href'))

    for thing in things:
        browser.get(thing)
        pag_blocks = []
        sleep(2)
        pagination_blocks = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-peotpw.e1mnvjgw0')

        for pag in pagination_blocks:
            pag_blocks.append(pag.text)

        if pag_blocks[-2].isdigit() == True:
            for pagination_block in range(1, int(pag_blocks[-2]) + 1):
                browser.get(f'{thing}?p={pagination_block}')
                sleep(2)
                elements1 = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-9gnskf.e1259i3g0')
                elements2 = browser.find_elements(By.CSS_SELECTOR,
                                                  'span.e1j9birj0.e106ikdt0.app-catalog-j8h82j.e1gjr6xo0')
                print(elements1)
                print(elements2)
                elements1.clear()
                elements2.clear()
                k += 1
                print("---", k, "page done---")
        else:
            dop_blocks = []
            additional_blocks = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-5wty15.e113kmgh0')

            for dop in additional_blocks:
                dop_blocks.append(dop.get_attribute('href'))

            for dop_url in dop_blocks:
                browser.get(dop_url)
                pag_blocks = []
                sleep(2)
                pagination_blocks = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-peotpw.e1mnvjgw0')

                for pagin in pagination_blocks:
                    pag_blocks.append(pagin.text)
                if len(pag_blocks) != 0:
                    for pagination_block in range(1, int(pag_blocks[-2]) + 1):
                        browser.get(f'{thing}?p={pagination_block}')
                        sleep(2)
                        elements1 = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-9gnskf.e1259i3g0')
                        elements2 = browser.find_elements(By.CSS_SELECTOR,
                                                          'span.e1j9birj0.e106ikdt0.app-catalog-j8h82j.e1gjr6xo0')
                        print(elements1)
                        print(elements2)
                        elements1.clear()
                        elements2.clear()
                        k += 1
                        print("---", k, "page done---")
                else:
                    sleep(2)
                    elements1 = browser.find_elements(By.CSS_SELECTOR, 'a.app-catalog-9gnskf.e1259i3g0')
                    elements2 = browser.find_elements(By.CSS_SELECTOR,
                                                      'span.e1j9birj0.e106ikdt0.app-catalog-j8h82j.e1gjr6xo0')
                    print(elements1)
                    print(elements2)
                    elements1.clear()
                    elements2.clear()
                    k += 1
                    print("---", k, "page done---")
        pagination_blocks.clear()
        pag_blocks.clear()

browser.quit()
