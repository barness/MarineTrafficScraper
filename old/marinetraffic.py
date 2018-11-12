# -*- coding: utf-8 -*-
import regex
from sixgill.sixgill_spider import SixGillSpider


class MarineTrafficSpider(SixGillSpider):

    name = "marinetraffic"
    allowed_domains = [u'www.marinetraffic.com']
    main_url = u'https://www.marinetraffic.com/en/ais/details/ships/shipid:442329/vessel:NORTHWESTERN'
    
    username = 'ndevine@conncoll.edu'
    password = '7gFh0JI1KM0hF0H5qxHfJnGLwmEz17y'

    force_tor = False
    
    ###
    username_login_xpath = '//input[@id="email"]'
    password_login_xpath = '//input[@id="password"]'
    submit_login_xpath = '//button[@type="submit"]'
    bad_credentials_xpath = '//div[@id="login-alert"]'
    logout_xpath = '//span[contains(text,"Logout")]'
    ###

    imo_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[1]/div[1]/b/node()'
    mmsi_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[1]/div[2]/b/node()'
    call_sign_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[1]/div[3]/b/node()'
    flag_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[1]/div[4]/b/node()'
    ais_vessel_type_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[5]/div[1]/b/node()'
    
    gross_tonnage_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[1]/b/node()'
    deadweight_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[2]/b/node()'
    length_breadth_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[3]/b/node()'
    year_built_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[4]/b/node()'
    status_xpath = u'html/body/main/div/div/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[5]/b/node()'
    
    position_received_xpath = u".//*[@id='tabs-last-pos']/div/div/div[1]/div[1]/strong/text()"
    local_time_xpath = u".//*[@id='tabs-last-pos']/div/div/div[1]/div[2]/strong/span/text()"
    area_xpath = u".//*[@id='tabs-last-pos']/div/div/div[1]/div[3]/span[2]/strong/text()"
    latitude_longitude_xpath = u".//*[@id='tabs-last-pos']/div/div/div[1]/div[4]/span[2]/strong/a/text()"
    position_status_xpath = u".//*[@id='tabs-last-pos']/div/div/div[1]/div[5]/span[2]/strong/text()"
    speed_xpath = u".//*[@id='tabs-last-pos']/div/div/div[1]/div[6]/span[2]/strong/text()"
    
    def start_requests(self, **kwargs):
        return super(MarineTrafficSpider, self).start_requests(
            self.login_url,
            [{'page_indicator': self.username_login_xpath,
              'items':
                  [
                      InputField(self.username_login_xpath, self.username),
                      InputField(self.password_login_xpath, self.password),
                      ClickField(self.submit_login_xpath),
                      BadCredentialsElement(self.bad_credentials_xpath)
                  ]
              }]
        )
