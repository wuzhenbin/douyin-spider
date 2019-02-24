

'''
el1 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/ao6")
el1.click()
el2 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/af2")
el2.click()
el2.send_keys("h_kyung_176")
el3 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/af5")
el3.click()
el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout")
el4.click()
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils import *
import time
import re
import math


APPPACKAGE = "com.ss.android.ugc.aweme"
APPACTIVITY = "com.ss.android.ugc.aweme.main.MainActivity"


class douyinCls(appAction):
    def __init__(self):
        super(douyinCls, self).__init__(APPPACKAGE=APPPACKAGE, APPACTIVITY=APPACTIVITY)

    
    def getUserVideo(self):
    	keyword = "h_kyung_176"
    	time.sleep(1)
    	# 搜索按钮
    	search_btn = self.wait.until(
    	    EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/ao6'))
    	)
    	search_btn.click()

    	# 点击搜索框输入值
    	search_input = self.wait.until(
    	    EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/af2'))
    	)
    	search_input.send_keys(keyword)

    	# 搜索按钮
    	search_sure_btn = self.wait.until(
    	    EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/af5'))
    	)
    	search_sure_btn.click()

    	# 定位搜索结果
    	res_part = self.wait.until(
    	    EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/bkm'))
    	)
    	res_part.click()

    	time.sleep(2)

    	# 获取作品数量来决定下拉次数 下拉次数 = 作品数/10 向上取整
    	try:
    	    works = self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/title').get_attribute('text')
    	    print(works,"**")
    	    res =  re.search('.*?(\d+)',works)
    	    num = math.ceil(int(res[1])/10)
    	    for item in range(num):
    	    	self.swipe_up()
    	    	time.sleep(2)
    	    
    	except NoSuchElementException:
    	    pass
        

if __name__ == '__main__':
    douyin = douyinCls()
    douyin.getUserVideo()










