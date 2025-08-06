from selenium.webdriver.common.by import By
import logging

# Configure logging (only needs to be done once in the main module)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def load(self):
        """Open the login page"""
        self.driver.get("https://www.saucedemo.com/")
        logger.info("Login page loaded")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
        logger.info(f"Entered username: {username}")

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        logger.info(f"Entered password: {'*' * len(password)}")  # Hides actual password

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        logger.info("Clicked login button")

    def login(self, username, password):
        """Combined method to perform full login"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        logger.info("Login process completed")
