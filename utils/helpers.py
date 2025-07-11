from pages.login_page import LoginPage
from pages.home_page import HomePage  # asumimos que ya lo tenés

from utils.config import Config

def login_and_go_to_home(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.USERNAME, Config.PASSWORD)
    return HomePage(driver)
