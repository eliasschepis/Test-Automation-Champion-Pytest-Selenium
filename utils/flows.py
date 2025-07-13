from pages.login_page import LoginPage
from utils.config import Config
from pages.home_page import HomePage
import time

# Login e ir al Home

def login_and_go_to_home(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.USERNAME, Config.PASSWORD)
    time.sleep(2)
    return HomePage(driver)
