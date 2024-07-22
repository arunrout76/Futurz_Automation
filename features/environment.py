
import os
import sys

# Assuming environment.py is located in the features directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
pages_path = os.path.join(project_root, 'pages')

# Add project root and pages to sys.path
sys.path.append(project_root)
sys.path.append(pages_path)

from pages import base
from Logs import log_config
import logging

base_url = "https://dev.infinityfuturz.com/"
# base_url = "https://dev.wizklub.com/inmobious/login/?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcnkiOjE3MDE0NjAzMTA5NDEuMTMxLCJjcmVhdGVkX29uIjoxNzAxNDQ1OTEwOTQxLjEzMSwidXNlcm5hbWUiOiJ5d2RpX2lub3VzIn0.5-e5MrV_8LBtWt4lgqNrPTJyfGk0l2ZDnarel0B0CpQ&page=olympiad&product_id=1be73b3e-7af6-4550-b049-f0378d596784"
log = log_config.get_logs()


def before_scenario(context, scenario):
    context.driver = logging.FileHandler.selenium_driver = base.launch_url()
# Set the page load timeout to 10 seconds (adjust as needed)
    context.driver.set_page_load_timeout(120)
    context.driver.get(base_url)
    context.driver.maximize_window()

