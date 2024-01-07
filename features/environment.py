import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from features.steps.Utility import ReadConfiguration


def before_scenario(context, driver):
    browser_name = ReadConfiguration.read_configuration("basic info", "browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get(ReadConfiguration.read_configuration("basic info", "url"))
    context.driver.implicitly_wait(5)


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="failed_screenshot",
                      attachment_type=AttachmentType.PNG)
