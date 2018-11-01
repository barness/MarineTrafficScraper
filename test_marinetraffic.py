# coding=utf-8
import datetime

from sixgill.spiders.forum_kalilinux import ForumKaliLinuxSpider
from sixgill.unitests_spiders.test_sixgill_spider import TestSixgillSpider
from testfixtures import compare
from sixgill.items import ForumItem
from unitests_spiders.crawl_forum_pages_mixin import CrawlForumPagesMixin


class TestForumKaliLinux(CrawlForumPagesMixin, TestSixgillSpider):
    def setUp(self):
        self.create_spider(ForumKaliLinuxSpider)
        self.do_setUp(__file__)

    def test_parse_single_page(self):
        self.single_page_dummy_url = u'https://www.marinetraffic.com/en/ais/details/ships/shipid:442329/vessel:NORTHWESTERN'
        self.single_page_file_path = u"thread-20694.html"
        resp = self.generate_file_based_response(self.single_page_dummy_url, self.single_page_file_path)
        results = self.spider.parse_page(response=resp)
        item_dict = self.prepare_item_dict_for_comparison(results)
        compare(item_dict, self.single_page_dict, prefix=u'Comparison error')
        self.verify_no_next_page(results, item_type=ForumItem)


    single_page_dict = {}
    
