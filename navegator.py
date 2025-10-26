from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

class Navigator:
    def __init__(self, firefoxProfile):
        options = Options()
        firefox_profile = FirefoxProfile(profile_directory=firefoxProfile)
        firefox_profile.set_preference("javascript.enabled", True)
        options.profile = firefox_profile
        self.driver = webdriver.Firefox(options=options)
        self.driver.get('https://www.youtube.com')

    def driver(self):
        return self.driver

    def readTab(self):
        return self.driver.current_url

    def close(self):
        self.driver.close()

navigator = Navigator("C:/Users/joele/AppData/Roaming/Mozilla/Firefox/Profiles/22r4a326.default-release")
