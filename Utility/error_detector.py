
class Detector:
    def __init__(self, driver):
        self.driver = driver

    def detect_error(self, actual_popup_element):
        highlight_border = """
          var element = arguments[0];
          element.style.border = '2px solid yellow';
          """
        # Use the JavaScript function to highlight the element
        self.driver.execute_script(highlight_border, actual_popup_element)

