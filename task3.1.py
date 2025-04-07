from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/pramye-divany"

driver.get(url)
time.sleep(5)

product_prices = []

price_elements = driver.find_elements(By.XPATH, '//span[contains(@class, "ui-LD-ZU") and @data-testid="price"]')

for price_element in price_elements:
    try:
        price_text = price_element.text

        price_number = int(price_text.replace('руб.', '').replace(' ', '').strip())

        product_prices.append(price_number)
    except Exception as e:
        print(f"Ошибка при обработке цены: {e}")

driver.quit()

df = pd.DataFrame({'Цена': product_prices})
df.to_csv('divan_prices.csv', index=False, encoding='utf-8')

print("Данные успешно сохранены в файл divan_prices.csv")