# -*- coding: utf-8 -*-
import regex
from sixgill.sixgill_spider import SixGillSpider


class MarineTrafficSpider(SixGillSpider):

    name = "marinetraffic"
    allowed_domains = [u'www.marinetraffic.com']
    main_url = u'https://www.marinetraffic.com/en/data/?asset_type=vessels'

    sub_forums_patterns = [u'forum-\d+-\d+\.html$']  
    deny_sub_forums_patterns = None  
    threads_patterns = [u'thread-\d+-1-\d+\.html$'] 
    deny_threads_patterns = None

    force_tor = False

    posts_xpath = u'//table[@id and @class="plhin"]'
    categories_xpath = u'//div[@id="pt"]/div/a/text()'
    title_xpath = u'//span[@id="thread_subject"]/text()'
    creator_xpath = u'.//div[@class="pi"]/div[@class="authi"]/a/text()'
    date_xpath = u'.//div[@class="authi"]/em[starts-with(@id, "authorposton")]/text()'
    date_recent_xpath = u'.//div[@class="authi"]/em[starts-with(@id, "authorposton")]/node()[2]'
    date_dmy_order = u'YMD'
    content_xpath = u'.//div[@class="pct"]/div[@class="pcb"]'
    next_page_xpath = u'//div[@id="pgt"]//a[@class="nxt"]/@href'

    item_numbers_xpath = u'//span[@class="xi2"]/text()'
    reply_numbers_xpath = u'//span[@class="xg1"]/text()'

    def start_requests(self, **kwargs):
        return super(MarineTrafficSpider, self).start_requests(
            self.main_url,
            [],
            ** kwargs
        )
    
    def _is_user_in_body(self, sel):
        return True

    def extract_categories(self, page_selector, index=1, subcategory_index=2):
        return super(MarineTrafficSpider, self).extract_categories(page_selector, index=2, subcategory_index=3)

    def extract_date(self, item_selector, date_str=None):
        date_str = " ".join(item_selector.xpath(self.date_xpath).extract()).strip()
        if date_str:
            try:
                date_str = ' '.join(regex.findall(r'\d+', date_str.split(' ')[1])) + ' ' + date_str.split(' ')[2]
            except IndexError:
                date_str = item_selector.xpath(self.date_recent_xpath).extract()[0].split('"')[1].replace('-', ' ')
        return super(MarineTrafficSpider, self).extract_date(item_selector, date_str)
