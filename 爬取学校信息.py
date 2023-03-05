import json
import keyword
import urllib
from urllib.request import urlopen
from lxml import etree
import pandas as pd


list_total = []
for page in range(1,13) :
    url = 'https://shanghai.eduour.cn/jianzhang/8-0-0-0-0/p'+str(page)+'/'
    headers = {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    url = urllib.request.Request(url,headers = headers)
    res = urllib.request.urlopen(url)
    res = res.read().decode('utf-8')

    ele = etree.HTML(res)


    for i in range(1,21) :
        list_page = []
        #专业方向
        major = ele.xpath("//div[@class='rules-ccon click-tt']/ul[" + str(i) +"]/li[1]/a/text()")
        #学校
        school = ele.xpath("//div[@class='rules-ccon click-tt']/ul[" + str(i) +"]/li[2]/a/text()")
        #所属专业
        majorBelone = ele.xpath("//div[@class='rules-ccon click-tt']/ul[" + str(i) +"]/li[3]/a/text()")
        #关注度
        #attention = ele.xpath("//div[@class='rules-ccon click-tt']/ul[" + str(i) + "]/li[4]/div/p[style]")
        #学制
        year = ele.xpath("//div[@class='rules-ccon click-tt']/ul[" + str(i) + "]/li[5]/text()")
        #学费
        cost = ele.xpath("//div[@class='rules-ccon click-tt']/ul[" + str(i) + "]/li[6]/text()")
        #授课方式
        classManner = ele.xpath("//div[@class='rules-ccon click-tt']/ul[" + str(i) + "]/li[7]/text()")

        list_page.append(major)
        list_page.append(school)
        list_page.append(majorBelone)
        #list_page.append(attention)
        list_page.append(year)
        list_page.append(cost)
        list_page.append(classManner)
        list_total.append(list_page)

data = pd.DataFrame(list_total, columns=['专业方向','学校','所属专业','学制','学费','授课方式'])
data.to_excel("data.xlsx")
