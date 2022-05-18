from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Scenario:
    def __init__(self, driver=webdriver.Chrome(executable_path='./chromedriver')):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")

    def login_site(self, login, password):
        self.driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[5]/a').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input').send_keys(login)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/input').send_keys(password)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()

    def choose_laptops(self):
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Laptops').click()
        time.sleep(1)

    def choose_dell(self):
        self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[4]/div/div/h4/a').click()

    def click_add_to_cart_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()

    def go_to_cart_and_click_place_order(self):
        self.driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[4]/a').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button').click()

    def fill_in_the_fields_and_click_button_purchase(self, name, country, city, card, month, year):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(name)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="country"]').send_keys(country)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(city)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="card"]').send_keys(card)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="month"]').send_keys(month)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="year"]').send_keys(year)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()

    def check_for_pop_up_window(self):
        if "Thank you for your purchase!" in self.driver.page_source:
            time.sleep(1)
            self.driver.close()
            self.driver.quit()
        else:
            print('purchase message miss')
