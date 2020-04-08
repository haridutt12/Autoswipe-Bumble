from selenium import webdriver
import  random
from time import sleep
from secrets import username, password

class BumbleBot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://bumble.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        sign_in  = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        sign_in.click()

        sleep(2)
        fb_login = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div/span/span')
        fb_login.click()

        base_window = self.driver.window_handles[0]

        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)
        

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/span/span')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/span/span')
        dislike_btn.click()

    def autoswipe(self):
        while True:
            try:
                r = random.randint(1,4)
                sleep(r)
                threshold = random.random()
                if threshold > 0.3:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                self.close_pop()

    def close_pop(self):
        pop1 = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div/div[2]/div/div[2]')
        pop1.click()


if __name__ == "__main__":

    bot = BumbleBot()
    bot.login()
    sleep(5)
    bot.autoswipe()
