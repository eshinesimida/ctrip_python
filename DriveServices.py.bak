# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from datetime import datetime
import re
import time
import uuid
import random
from xiecheng import xiechengDAO

class XiechengDriverService(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        
        self.xiechengDao = xiechengDAO()
        self.listPageInfo = []
        self.commList = []
        #self.urls=['http://you.ctrip.com/sight/beijing1/234.html','http://you.ctrip.com/sight/beijing1/229.html','http://you.ctrip.com/sight/beijing1/231.html','http://you.ctrip.com/sight/yanqing770/230.html','http://you.ctrip.com/sight/beijing1/5174.html','http://you.ctrip.com/sight/beijing1/233.html','http://you.ctrip.com/sight/huairou120418/243.html']
        self.urls=[



'http://you.ctrip.com/sight/xinxing2919/136198.html',
            'http://you.ctrip.com/sight/yunfu836/73063.html',
            'http://you.ctrip.com/sight/yunfu836/1408555.html',
            'http://you.ctrip.com/sight/yunfu836/73062.html',
            'http://you.ctrip.com/sight/xinxing2919/136197.html'
        ]
        # 打开携程首页
    def start(self):
        for url1 in self.urls:
            self.driver.get(url1)
            # 将界面最大化
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.crawlxiecheng()




    def crawlxiecheng(self):
        # 单页循环次数
        loopNum = 0

        ifHandle = False

        self.driver.find_element_by_xpath('//*[@id="hrefyyDp"]/span').click()
        time.sleep(random.uniform(3, 6))

        self.driver.find_element_by_xpath('//*[@id="selectSort"]/span').click()
        time.sleep(random.uniform(3, 6))
        self.driver.find_element_by_xpath('//*[@id="selectSort"]/ul/li[3]/a').click()
        time.sleep(random.uniform(3, 6))

        #self.crawllianjie(self.driver.page_source)

        #获取总页面数
        pageNum = 2800
        while(pageNum>=1):
            # 循环次数加1
            loopNum = loopNum + 1
            target = self.driver.find_element_by_class_name(
                'pager_v1')
            y = target.location['y']
            # print y
            y = y - 100

            js = "var q=document.documentElement.scrollTop=" + str(y)
            self.driver.execute_script(js)

            time.sleep(3)


            response1 = HtmlResponse(url="my HTML string", body=self.driver.page_source, encoding="utf-8")
            num = response1.xpath('//b[@class = "numpage"]/text()').extract()[0]
            if u"有用" in self.driver.page_source:

                if ifHandle == False:
                    a = self.crawllianjie(self.driver.page_source)
                    if(a ==2):
                        break
                    ifHandle = True

                try:
                    #print u"下一页" in self.driver.page_source
                    if u"下一页" in self.driver.page_source:
                        pageNum = pageNum - 1
                      
                        self.driver.find_element_by_partial_link_text("下一页").click()
                        #self.driver.find_element_by_xpath("//div[@class='weiboitem active']/div[@class='comment_ctrip']/div[@class='ttd_pager cf']/div[@class='pager_v1']/a[@class='nextpage']").click()
                        ifHandle = False
                        loopNum = 0

                        time.sleep(3)
                        print "页数：" + str(pageNum)
                        print 'num =' + num, type(int(num))
                        num1 = 2800 - pageNum + 1
                        print 'num1 = ' + str(num1)

                        if ((num1 == int(num)) or (num1 == 100)):
                            break
                            num1 = 0
                            pageNum = 2800
                            a = response1.xpath('//*[ @ id = "weiboCom1"]/div[2]/ul/li').extract()
                            print a, len(a)
                            c = []
                            for b in a:
                                c.append(re.findall(ur'<li class="current">', b))
                            index = c.index([u'<li class="current">'])
                            index = index + 2
                            # // *[ @ id = "weiboCom1"] / div[2] / ul
                            self.driver.find_element_by_xpath(
                                '//*[@id="weiboCom1"]/div[2]/ul/li[' + str(index) + ']/a').click()
                except:
                    pageNum = pageNum + 1




        return False if pageNum > 1 else True

    def crawllianjie(self, page_sourse):
        #print page_sourse
        response = HtmlResponse(url="my HTML string", body=page_sourse, encoding="utf-8")
       
        #jingqu = response.xpath('//div[@class="content cf"]/div[@class="dest_toptitle detail_tt"]/div[@class="cf"]/div[@class="f_left"]/h1/a/text()').extract()[0]
        jingqu = response.xpath('//html/body/div[@class="content cf "]/div[2]/div/div[1]/h1/a/text()').extract()[0]
        province = response.xpath('//html/body/div[@class="content cf "]/div[1]/ul/li[4]/a/text()').extract()[0]
        A = response.xpath("//div[@class='weiboitem active']/div[@class='comment_ctrip']/div[@class='comment_single']")
        class1 = response.xpath('//html/body/div[4]/div/div[2]/div[1]/ul/li[2]/span[2]/text()').extract()
        class2 = []
        for j in class1:
            class2.append(j.strip())
        class2 = ''.join(class2)
        #/html/body/div[4]/div/div[2]/div[1]/ul/li[2]/span[2]
        #print A
        
        for B in A:
            url = B.xpath("ul/li[@class='pic_medal']/div[@class='hotel_pic']/a/@href").extract()
            author = B.xpath('div/span/a/text()').extract_first()
            jins = B.xpath('ul/li/span').extract_first()
            flag2 = re.findall(ur'\u666f\u8272\uff1a(.*?)\u2003', jins)
            flag3 = re.findall(ur'\u8da3\u5473\uff1a(.*?)\u2003', jins)
            flag4 = re.findall(ur'\u6027\u4ef7\u6bd4\uff1a(.*?)\u2003', jins)
            # print flag2,flag3,flag4
            if (len(flag2) > 0):
                jingse1 = flag2[0]
            else:
                jingse1 = ''
            if (len(flag3) > 0):
                quwei = flag3[0]
            else:
                quwei = ''
            if (len(flag4) > 0):
                xingjiabi = flag4[0]
            else:
                xingjiabi = ''

            comment = B.xpath('ul/li[2]/span/text()').extract_first()
            time = B.xpath('ul/li[@class="from_link"]/span/span/em/text()').extract_first()
            # if(time < '2017-10-12'):
            #     return(2)
            #     continue

            href = B.xpath('div/span/a[@href]').extract_first()
            href = href.split('"')[3]
            ID = B.xpath('ul/li[@class="from_link"]/span[@class="f_right"]/a[1]/@data-id').extract_first()
           

            href = 'http://you.ctrip.com' + href
            if(class2):
                class2 = class2
            else:
                class2 = ''

            self.listPageInfo.append({"jingqu":jingqu,"province":province,"url": href, "author": author, "ID": ID,"jingse":jingse1,"quwei":quwei,
                                      "xingjiabi":xingjiabi,"comment":comment,"time":time,'class':class2})
        xiechengService.saveListPageInfo()

        print len(self.listPageInfo)
        self.listPageInfo = []

	def saveListPageInfo(self):
        self.xiechengDao.savehotellink(self.listPageInfo)

    def depose(self):
        self.driver.close()

if __name__=="__main__":
    xiechengService = XiechengDriverService()
    xiechengService.start()
    xiechengService.depose()

