import time
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from abc import ABC, abstractmethod

class AbstractNavigatorMarionette(ABC):
    """ This class defines common methods for Marionette navigators.
    The process of initialization of navigator options follows
    the Template Method software design pattern;
    see methods "init_<any>", which are invoked in the constructor.
    """

    def __init__(self, delay_of_page_load = 3):
        self.webdriver_path = str(os.getenv("NAVIGATOR_WEBDRIVER_PATH"))
        self.user_data_dir = str(os.getenv("NAVIGATOR_DATA_DIR_OF_USER"))
        self.delay_of_page_load = delay_of_page_load # seconds

        # Internal components
        self.options = None
        self.init_options()
        self.service = None
        self.init_service()
        self.driver = None
        self.init_driver()


    @abstractmethod
    def init_options(self):
        pass # To be overriden

    @abstractmethod
    def init_service(self):
        pass # To be overriden
    
    @abstractmethod
    def init_driver(self):
        pass # To be overriden


    def set_delay_of_page_load(self, delay):
        """Setter method for the delay of page load in seconds."""
        self.delay_of_page_load = delay


    def get_html_content(self):
        """Get the raw HTML content of the current page."""
        return str(self.driver.page_source)


    def navigate(self, url, wait = True):
        """Navigate to the specified URL,
        and optionally wait for the page to load.
        """
        self.driver.get(str(url))
        if wait:
            time.sleep(self.delay_of_page_load)
        return str(self.driver.page_source)
    

    def navigate_and_wait_forever(self, url):
        """Navigate to the specified URL,
        and wait indefinitely.
        """
        self.driver.get(str(url))
        wait = WebDriverWait(self.driver, 6000000)
        try:
            wait.until(EC.presence_of_element_located((\
                By.CSS_SELECTOR, "div[class*=\"inexistent\"]")))
        except TimeoutException:
            None
    

    def click(self, css_selector, wait = False):
        """Click on the element specified by the CSS selector,
        and optionally wait for the page to load.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        if element is not None:
            element.click()
            if wait:
                time.sleep(self.delay_of_page_load)


    def scroll_down(self, css_selector, wait = False):
        """Send the scroll down order to the HTML DOM element
        specified by the CSS selector,
        and optionally wait for the page to load.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        if element is not None:
            element.click()
            element.send_keys(Keys.PAGE_DOWN)
            if wait:
                time.sleep(self.delay_of_page_load)


    def quit(self):
        """Quit the WebDriver and stop the service."""
        if self.driver:
            self.driver.quit()
        if self.service:
            self.service.stop()
