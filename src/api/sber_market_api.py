from src.api.market_api import AbstractMarketApi

import re
from typing import List
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from src.schemas.product import ProductSchema, ProductSchemaAdd

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,10800")
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--start-maximized")
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

options.add_experimental_option(
    'prefs',
    {
        # 'profile.managed_default_content_settings.javascript': 2,
        'profile.managed_default_content_settings.images': 2,
        # 'profile.managed_default_content_settings.mixed_script': 2,
        'profile.managed_default_content_settings.media_stream': 2,
        'profile.managed_default_content_settings.stylesheets': 2
    }
)

service = Service(executable_path='C:\Projects\Business\yoda2\chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1920, 1080)


class SberMarketApi(AbstractMarketApi):
    def get_products(self, query: str, market_name: str, max_count: int) -> List:
        url = f"https://sbermarket.ru/{market_name}/search?&keywords={query}"
        driver.get(url)
        source_data = driver.page_source
        soup = bs(source_data, features='html.parser')
        products_container = soup.find_all(class_="ProductCard_root__K6IZK ProductCard_addToCartBig__h5PsY")
        res = []
        for p in products_container[:max_count]:
            title = p.find(class_='ProductCard_title__iNsaD').text
            img = p.find(class_='Image_root__yieXw')['src']
            # volume = p.find(class_='ProductCard_volume__PINyI').text
            price = re.findall(r'\d*\.\d+|\d+',
                               str(p.find(class_='ProductCardPrice_price__Kv7Q7').text).replace(',', '.'))[1]
            href = 'https://sbermarket.ru/' + \
                   p.find('a', class_='Link_root__fd7C0 Link_disguised__PSFAR ProductCardLink_root__69qxV',
                          href=True)["href"]

            product = ProductSchemaAdd(
                title=title,
                price=price,
                image=img,
                href=href,
            )
            res.append(product)
        return res
