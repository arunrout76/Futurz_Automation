import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


def launch_url():
    options = Options()
    options.add_experimental_option("detach", True)
    driver_path = r"C:\Users\arun\OneDrive\Desktop\WizklubFuturz\Driver\119.0.6045.106\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    #driver = webdriver.Chrome(EdgeChromiumDriverManager().install(), options=options)
    return driver

# def launch_url():
#     options = Options()
#     options.add_experimental_option("detach", True)
#     # # Set the path to your ChromeDriver executable
#     # driver_path = r"C:\Users\arun\PycharmProjects\WizklubFuturz\Driver\119.0.6045.106\chromedriver.exe"
#     # Get the current script's directory
#     current_directory = os.path.dirname(os.path.realpath(__file__))
#     # Construct the relative path to the driver
#     driver_path = os.path.join(current_directory, 'Driver', '119.0.6045.106', 'chromedriver.exe')
#     # Define desired capabilities for Chrome
#     capabilities = DesiredCapabilities.CHROME.copy()
#     capabilities['platform'] = 'LINUX'  # Set the appropriate platform
#     # capabilities['version'] = 'latest'  # Set the desired browser version
#     # Create a Chrome WebDriver instance with desired capabilities
#     # http://localhost:4444
#     # http://HubService:4444
#     # http://172.17.0.2:4444

#     driver = webdriver.Remote(command_executor="http://HubService:4444",
#                           desired_capabilities=capabilities,
#                           options=options)
#     # driver = webdriver.Remote(command_executor="http://localhost:4444",
#     #                       desired_capabilities=capabilities,
#     #                       options=options)
    
#     driver.set_page_load_timeout(60)  # Set the page load timeout to 60 seconds
#     driver.set_script_timeout(60)     # Set the script timeout to 60 seconds
#     driver.implicitly_wait(10)        # Set the implicit wait time to 10 seconds


#     return driver
