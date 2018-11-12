class WebDriverObject(object):
    def act(self, webdriver):
        pass

class XPathBasedWebDriverObject(WebDriverObject):
    def __init__(self, xpath):
        self._xpath = xpath

    def find_optional_element_by_xpath(self, webdriver):
        try:
            elem = webdriver.driver.find_element_by_xpath(self._xpath)
            return elem
        except NoSuchElementException as e:
            webdriver.spider_logger.info(u'Optional element not found for xpath:"%s" in %s (reason:%s)' %
                                         (self._xpath, webdriver.pg_url, e.msg))
            return None

    def find_mandatory_element_by_xpath(self, webdriver):
        try:
            elem = webdriver.driver.find_element_by_xpath(self._xpath)
            return elem
        except NoSuchElementException:
            webdriver.spider_logger.error(u'Mandatory element not found for xpath:"%s" in %s' %
                                          (self._xpath, webdriver.pg_url))
            raise

class InputField(XPathBasedWebDriverObject):

    def __init__(self, xpath, value):
        super(InputField, self).__init__(xpath)
        self._value = value

    def act(self, webdriver):
        input_element = self.find_mandatory_element_by_xpath(webdriver)
        if input_element:
            try:
                input_element.clear()
                input_element.send_keys(self._value)
                webdriver.spider_logger.info(u'Value %s set at %s in %s' % (self._value, self._xpath, webdriver.pg_url))
            except Exception:
                webdriver.spider_logger.error(u'Could not fill value {} in xpath {} '.format(self._value, self._xpath))
                # Attempt to set the value using JS
                webdriver.driver.execute_script('arguments[0].value = arguments[1];', input_element, self._value)

class ClickField(XPathBasedWebDriverObject):

    def __init__(self, xpath):
        super(ClickField, self).__init__(xpath)

    def act(self, webdriver):
        clickable_element = self.find_mandatory_element_by_xpath(webdriver)
        try:
            clickable_element.click()
        except WebDriverException:
            webdriver.spider_logger.info(u'Trying to click on {} using JS'.format(self._xpath))
            try:
                webdriver.driver.execute_script('document.evaluate(arguments[0], document, null, '
                                                'XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();',
                                                self._xpath)
            except Exception:
                webdriver.spider_logger.error(u'ClickField failed to click on {} at {}'.format(self._xpath,
                                                                                               webdriver.pg_url))
                raise
        except Exception:
            webdriver.spider_logger.error(u'ClickField failed to click on {} at {}'.format(self._xpath,
                                                                                           webdriver.pg_url))
            raise
        sleep(3)
        webdriver.spider_logger.info(u'Clicked on %s in %s' % (self._xpath, webdriver.pg_url))
        
class LoginRejection(XPathBasedWebDriverObject):
    def __init__(self, xpath, rejection_reason=None, text_lookup=None):
        super(LoginRejection, self).__init__(xpath)
        self.rejection_reason = rejection_reason
        self.text_lookup = text_lookup

    def act(self, webdriver):
        sleep(5)
        bad_credentials_element = self.find_optional_element_by_xpath(webdriver)
        if bad_credentials_element and (not self.text_lookup or self.text_lookup in bad_credentials_element.text):
            webdriver.spider_logger.error(self.rejection_reason + ' in page {}'.format(webdriver.pg_url))
            raise BadCredentialsException(self.rejection_reason)


class BadCredentialsElement(LoginRejection):
    def __init__(self, xpath, text_lookup=None):
        super(BadCredentialsElement, self).__init__(xpath, rejection_reason=u'bad credentials', text_lookup=text_lookup)