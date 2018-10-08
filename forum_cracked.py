# coding=utf-8
from hashlib import md5

from sixgill.chrome_driver.chrome_driver import ChromeHeadlessDriver
from sixgill.sixgill_spider import SixGillSpider
from sixgill.webdriver_objects import InputField, ClickField, BadCredentialsElement


class ForumCrackedSpider(SixGillSpider):
    name = 'forum_cracked'
    site_name = 'forum_cracked'
    allowed_domains = ['cracked.to']
    main_url = 'https://cracked.to/index.php'
    login_url = 'https://cracked.to/member.php?action=login'

    download_delay = 1
    close_driver = False

    username = 'G8Sl0Ot'
    password = 'vNax5bcOf0ron'

    site_type = 'forum'
    force_tor = False

    sub_forums_patterns = ('/Forum(-\w+)+(\?page=\d+)?$',)
    threads_patterns = ('/Thread(-\w+)+$',)

    username_login_xpath = '//input[@name="username"]'
    password_login_xpath = '//input[@name="password"]'
    submit_login_xpath = '//div[@id="content"]//input[@value="Login"]'
    bad_credentials_xpath = '//div[@class="error"]'

    username_after_login_xpath = '//span[@id="menu-right"]//li[@class="dropbtn"]/a/text()'

    posts_xpath = '//div[@id="posts"]/div[starts-with(@id, "post") and not(@class="post deleted_post_hidden")]'
    categories_xpath = '//div[@class="navigation"]/a/text()'
    title_xpath = '//div[@class="thread-header"]/h1/text()'

    creator_xpath = './/div[@class="author_information"]/span[@class="largetext"]//text()'
    content_xpath = './/div[@class="post_content"]/div[starts-with(@id, "pid")]/node()'
    signature_xpath = './/div[@class="signature scaleimages"]/node()'
    item_id_xpath = './@id'
    id_filter_re = "(\d+)$"

    date_xpath = 'concat(.//span[@class="post_date"]/span/text(), .//span[@class="post_date"]/text())'
    date_dmy_order = 'MDY'

    next_page_xpath = '//div[@class="pagination"]//a[@class="pagination_next"]/@href'

    item_numbers_xpath = '//tr/td[3]/*[@id="stats-count"]/text()'
    reply_numbers_xpath = '//tr/td[4]/*[@id="stats-count"]/text()'

    active_contribute = True
    wait_time = 30
    hidden_content_xpath = '//div[@class="hidden-content-body"][contains(text(), "You must reply to this thread")]'
    closed_post_xpath = '(//a[@href="Forum-Archive"] | ' \
                        '//a[@class="button closed_button"]/span[contains(text(), "Thread Closed")])'
    quick_reply_input_xpath = '//textarea[@id="message"]'
    quick_reply_submit_xpath = '//input[@id="quick_reply_submit"]'
    post_replies = [u'thanks bro its good',
                    u'you the man very nice',
                    u'its cool thank you',
                    u'very nice thanks keep sharin',
                    u'good I like it thanks',
                    u'I want this one its good thank you',
                    u'Thanks man its very nice!!!',
                    u'wow awesome very good',
                    u'bro you are great thanks',
                    u'thanks for sharin this my brother',
                    u'nice share you the man',
                    u'thanks buddy its good',
                    u'its helpin me very much thanks',
                    u'its great thank you bro!!',
                    u'wow very goodddd! thanks']

    def create_driver(self):
        return ChromeHeadlessDriver(logger=self.logger, proxy=self.force_tor)

    def _is_user_in_body(self, sel):
        username_selector = sel.xpath(self.username_after_login_xpath)
        user_in_page = self.username in username_selector.extract_first() if username_selector else False
        if not user_in_page:
            self.logger.info(u'User {} not found in page'.format(self.username))
        return user_in_page

    def start_requests(self, **kwargs):
        return super(ForumCrackedSpider, self).start_requests(
            self.login_url,
            [{'page_indicator': self.username_login_xpath,
              'items':
                  [
                      InputField(self.username_login_xpath, self.username),
                      InputField(self.password_login_xpath, self.password),
                      ClickField(self.submit_login_xpath),
                      BadCredentialsElement(self.bad_credentials_xpath, text_lookup='Login failed.')
                  ]
              }
             ]
        )

    def collect_item_details(self, item, item_selector, main_post_item=None, index=0):
        super(ForumCrackedSpider, self).collect_item_details(item, item_selector, main_post_item, index)
        item['id'] = md5(unicode(item['date']) + unicode(item['id'])).hexdigest()
