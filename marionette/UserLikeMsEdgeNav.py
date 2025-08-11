from marionette.AbstractNavigatorMarionette import AbstractNavigatorMarionette

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service


class UserLikeMsEdgeNav(AbstractNavigatorMarionette):
    """UserLikeNav initialises the options of the navigator,
    so the server does not detect the automation.
    
    This class implements the abstract initialization
    methods required by AbstractNavigatorMarionette.

    These methods "init_<any>" are invoked by the
    superclass as part of the Template Method pattern.
    """

    def init_options(self):
        """Init the navigator options for the Marionette
        instance. These options disguise the automation
        and set the user data directory.
        """

        self.options = Options()
        self.options.use_chromium = True

        self.options.add_experimental_option(\
            name = "excludeSwitches",\
            value = ["enable-automation"])
        
        self.options.add_experimental_option(\
            name = "useAutomationExtension",\
            value = False)
        
        self.options.add_argument(\
            argument = "--disable-blink-features=AutomationControlled")
        
        self.options.add_argument(\
            argument = f"--user-data-dir={self.user_data_dir}")
    

    def init_service(self):
        """This service is used to start the WebDriver service."""

        self.service = Service(self.webdriver_path)
    

    def init_driver(self):
        """Get the navigator WebDriver instance."""

        self.driver = webdriver.Edge(\
            service = self.service, options = self.options)
        self.driver.execute_cdp_cmd(\
            cmd = "Network.setUserAgentOverride",\
            cmd_args = {"userAgent": self.user_agent})
        self.driver.execute_script(\
            ("Object.defineProperty(navigator, 'webdriver',"
                "{get: () => undefined})"))
