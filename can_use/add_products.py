#coding:utf-8
import SendKeys
from selenium import webdriver
import time
#这是个自动添加新商品的.py。
# 运行的时候不能做其他操作，因为涉及win弹窗的输入，用了sendkeys，不太稳定，但是简单啊
#cmd下{pip install SendKeys
#提示让你去下载VCForPython27（连网址都给你了，好贴心）}
#下面的因为每次都关掉，所以放在for循环里面了
address = raw_input('Enter location(报名页网址有id、mid、styleClassId、useDeposit的那种): ')
if len(address) < 1:
    print "error"

url = address
 # 配置文件里找登录信息
profile_dir = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\5cmfbcqp.default"
profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)
driver.get(url)
#要新建几个就输入数字
for i in range(10):
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='tableview']/div/div/a").click()
    time.sleep(2)
    # 填写一个商品信息
    driver.find_element_by_class_name("form-control").clear()
    driver.find_element_by_class_name("form-control").send_keys("hello-" + str(i+1))
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='centerPicker']/div[2]/label").click()
    time.sleep(2)
    # SendKeys
    SendKeys.SendKeys('D:\\dlpic\\xiaolongbao.jpg')
    SendKeys.SendKeys("{ENTER}")
    time.sleep(2)
    # 添加款式(如果是读取文件中数据，可以增加行数个分类，这里只加一个
    driver.find_element_by_id("addStyleButton").click()
    # 分类
    driver.find_element_by_xpath("//*[@id='styleContainer']/div/div[1]/input[2]").clear()
    driver.find_element_by_xpath("//*[@id='styleContainer']/div/div[1]/input[2]").send_keys(u"1,2.3。3,3，1")
    # 促销价
    driver.find_element_by_xpath("//*[@id='styleContainer']/div/div[2]/div/div[2]/input").clear()
    driver.find_element_by_xpath("//*[@id='styleContainer']/div/div[2]/div/div[2]/input").send_keys("1")
    # 原价
    driver.find_element_by_xpath("//*[@id='styleContainer']/div/div[2]/div/div[3]/input").clear()
    driver.find_element_by_xpath("//*[@id='styleContainer']/div/div[2]/div/div[3]/input").send_keys("2")
    # 剩余名额
    driver.find_element_by_xpath("//*[@id='styleContainer']/div/div[2]/div/div[4]/input").clear()
    driver.find_element_by_xpath("//*[@id='styleContainer']/div/div[2]/div/div[4]/input").send_keys("3")
    # 详细信息是个iframe
    print "enter iframe " + str(i + 1) + "time"
    driver.switch_to.frame("ueditor_0")
    driver.find_element_by_xpath("//body[@class='view']").clear()
    # driver.find_element_by_xpath("/html/body").click()
    time.sleep(1)
    driver.find_element_by_xpath("//body[@class='view']").send_keys("2163v1320123456" + str(i+1))
    time.sleep(1)
    driver.switch_to.parent_frame()
    print "out iframe " + str(i + 1) + "time"
    #仅仅保存，没有上架
    driver.find_element_by_id("submitButton3").click()
    #保存并上架
    # driver.find_element_by_id("submitButton").click()
    #保存并上架推首页
    # driver.find_element_by_id("submitButton2").click()

