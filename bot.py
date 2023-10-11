from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

speed_test_url = "https://www.speedtest.net/"
twitter_url = "https://twitter.com/?logout=1692527511243"
twitter_pass = "Ha$n1998"
twitter_email = "hassan_tariq74@outlook.com"
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(speed_test_url)
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                       '/div[3]/div/div[3]/div/div/div[2]'
                                                       '/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                     '/div[3]/div/div[3]/div/div/div[2]'
                                                     '/div[1]/div[2]/div/div[2]/span').text
        print(f"Download:{self.down}")
        print(f"Upload:{self.up}")



    def tweet_at_provider(self):
        self.driver.get(twitter_url)
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        time.sleep(3)
        email = self.driver.find_element(By.NAME, 'text')
        email.send_keys(twitter_email)
        email.send_keys(Keys.ENTER)
        time.sleep(10)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(twitter_pass)
        password.send_keys(Keys.ENTER)
        time.sleep(15)

        tweet_box = self.driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
        tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}"
                            f"up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

        post = self.driver.find_element(By.XPATH, "//span[text()='Post']")
        post.click()

        time.sleep(5)
        self.driver.quit()
