# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from logging import getLogger


class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == 'get_stock' and \
                request.url == 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board':
            driver = webdriver.Firefox()
            driver.get(request.url)
            htmls = []
            for i in range(10):
                    WebDriverWait(driver, 100).until(
                        EC.presence_of_element_located((By.ID, "table_wrapper-table"))
                    )
                    next_page_btn = driver.find_element_by_xpath(
                        '//*[@id="main-table_paginate"]/a[@class="next paginate_button"]')
                    htmls.append(driver.page_source)
                    next_page_btn.click()
            driver.quit()
            return HtmlResponse(url=request.url, body=htmls, request=request, encoding='utf-8')
        return None

# def spider_opened(self, spider):
#     spider.logger.info('Eastmoney Spider opened: %s' % spider.name)
