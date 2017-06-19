#coding:utf-8
from selenium import webdriver
import time
#后台管理皮肤页
address1 = raw_input('Enter location(后台管理皮肤页): ')
if len(address1) < 1:
    print "error"
url1=address1
#后台管理顶部页
address2 = raw_input('Enter location(后台管理顶部页): ')
if len(address2) < 1:
    print "error"

url2 = address2
#商品、向导页（短，能看到搜索框,活动用了那啥，还是商品好用
address3 = raw_input('Enter location(商品向导页): ')
if len(address3) < 1:
    print "error"

url3 = address3
# 这里是新皮肤id号，以后添加就再加,是盈动版
NewSkinId = ['187', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '271']

profile_dir = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\5cmfbcqp.default"
profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)
driver.get(url1)
driver.maximize_window()
#j进入到了电脑网页设置
#点击li，让hover出来
hov = driver.find_elements_by_css_selector("ul#collection-view>li")

#截图，就五个情况，放在D:\\screenshotnewskin2文件夹下
def screenshot(skinid, num,typenum):
    driver.get(url3)
    time.sleep(2)
    #活动搜索框
    if num == 1:
        driver.get_screenshot_as_file("D:\\screenshotnewskin2\\" + str(skinid) + "search_active" + ".png")

    #商品搜索框
    elif num == 2:
        driver.get_screenshot_as_file("D:\\screenshotnewskin2\\" + str(skinid) + "search_goods" + ".png")
    #客服
    elif num == 3:
        driver.get_screenshot_as_file("D:\\screenshotnewskin2\\" + str(skinid) + "service" + str(typenum) + ".png")
    #倒计时
    elif num == 4:
        driver.find_element_by_id("nav-countdown").click()
        time.sleep(4)
        driver.get_screenshot_as_file("D:\\screenshotnewskin2\\" + str(skinid) + "countdown" + str(typenum) + ".png")
    #没有模块
    else:
        driver.get_screenshot_as_file("D:\\screenshotnewskin2\\" + str(skinid) + "nomodel" + ".png")
    time.sleep(2)

#------------------------------------------------------------
#skin_top_search_active顶部搜索活动,新皮肤没有活动搜索
def skin_top_search_active(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，把5个都先弄出来以后要（发现顶部背景色也是两个radio-inline，那下表从2-6了,活动搜索是2
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[2].find_element_by_tag_name("input").click()
    print "into search_active model"
    # 活动搜索模块样式没有，不用
    driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
    time.sleep(3)
    # 转到加入我们页面去截图
    screenshot(skinid, 1, 0)

#-------------------------------------------
#skin_top_search_goods顶部搜索商品
def skin_top_search_goods(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，把5个都先弄出来以后要（发现顶部背景色也是两个radio-inline，那下表从2-6了,活动商品是3
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[3].find_element_by_tag_name("input").click()
    print "into search_goods model"
    # 商品搜索模块样式没有，不用
    driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
    time.sleep(3)
    # 转到加入我们页面去截图
    screenshot(skinid, 2, 0)

#新皮肤
def new_skin_top_search_goods(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，新皮肤只有4个
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[0].find_element_by_tag_name("input").click()
    print "into new search_goods model"
    # 商品搜索模块样式没有，不用
    driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
    time.sleep(3)
    screenshot(skinid, 2, 0)

#---------------------------------------------------
#skin_top_service顶部的客服样式
def skin_top_service(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，把5个都先弄出来以后要（发现顶部背景色也是两个radio-inline，那下表从2-6了,客服是5
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[5].find_element_by_tag_name("input").click()
    print "into top_service model"
    # 客服模块样式radio-inline，下表从13-17
    for typenum in range(13, 18):
        showservicetype = driver.find_elements_by_class_name("radio-inline")
        showservicetype[typenum].click()
        driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
        time.sleep(3)
        # 转到加入我们页面去截图
        screenshot(skinid, 3, typenum)
        print "have a service png", typenum
        driver.get(url2)

# new_skin_top_service新皮肤顶部的客服样式
def new_skin_top_service(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[2].find_element_by_tag_name("input").click()
    print "into new top_service model"
    # 客服模块样式radio-inline，下表从10-14
    for typenum in range(10, 15):
        showservicetype = driver.find_elements_by_class_name("radio-inline")
        showservicetype[typenum].click()
        driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
        time.sleep(3)
        # 转到加入我们页面去截图
        screenshot(skinid, 3, typenum)
        print "have a service png", typenum
        driver.get(url2)

# ---------------------------------------------------
#skin_top_countdown顶部的倒计时样式
def skin_top_countdown(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，把5个都先弄出来以后要（发现顶部背景色也是两个radio-inline，那下表从2-6了,倒计时是4
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[4].find_element_by_tag_name("input").click()
    print "into top_countdown model"
    # 倒计时模块样式居然也是radio-inline，下表从7-12
    for y in range(7, 13):
        showcountdowntype = driver.find_elements_by_class_name("radio-inline")
        showcountdowntype[y].click()
        driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
        time.sleep(3)
        # 转到加入我们页面去截图
        screenshot(skinid, 4, y)
        print "have a countdown png", y
        driver.get(url2)

# new_skin_top_countdown新皮肤顶部的倒计时样式
def new_skin_top_countdown(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[1].find_element_by_tag_name("input").click()
    print "into new top_countdown model"
    # 倒计时模块样式radio-inline，下表从5-10
    for y in range(4, 10):
        showcountdowntype = driver.find_elements_by_class_name("radio-inline")
        showcountdowntype[y].click()
        driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
        time.sleep(3)
        # 转到加入我们页面去截图
        screenshot(skinid, 4, y)
        print "have a countdown png", y
        driver.get(url2)
# ---------------------------------------------------
#skin_top_nomodel顶部搜索活动
def skin_top_nomodel(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，把5个都先弄出来以后要（发现顶部背景色也是两个radio-inline，那下表从2-6了,没有模块是6
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[6].find_element_by_tag_name("input").click()
    print "into top_nomodel model"
    # 活动搜索模块样式没有，不用

    driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
    time.sleep(3)
    # 转到加入我们页面去截图
    screenshot(skinid, 5, 0)
#new_skin_top_nomodel新皮肤顶部搜索活动
def new_skin_top_nomodel(skinid):
    driver.get(url2)
    time.sleep(2)
    # 显示模块，
    showmodel = driver.find_elements_by_class_name("radio-inline")
    showmodel[3].find_element_by_tag_name("input").click()
    print "into new top_nomodel model"
    # 活动搜索模块样式没有，不用

    driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
    time.sleep(3)
    # 转到加入我们页面去截图
    screenshot(skinid, 5, 0)

#one_page_skin是每一页8个皮肤,每个皮肤的顶部倒计时样式/我把他们剥离了，方便以后的客服模块
def one_page_skin(skin_page):
    # l = 0
    for l in range(0, 8):
        driver.get(url1)
        time.sleep(2)
        #不能加，要是第二页就又跳转到第一页了..所以加了下面四行
        #转到当前皮肤页面
        driver.find_element_by_class_name("form-control").clear()
        driver.find_element_by_class_name("form-control").send_keys(skin_page)
        driver.find_element_by_xpath("//*[@id='table-data-view']/form/button").click()
        time.sleep(2)
        hov = driver.find_elements_by_css_selector("ul#collection-view>li")
        hov[l].click()
        #IndexError: list index out of range 已解决，当时是没有跳回当前皮肤选择页，到顶部设置页去了
        skinid = hov[l].find_element_by_css_selector("div.item-action>button").get_attribute("id")
        #这里留个id，到时候可能会区分新老皮肤,想法是根据皮肤多传一个参数，传到截屏哪里，判断是新老，url4去（发现不用变，我试试）
        hov[l].find_element_by_css_selector("div.item-action>button").click()
        time.sleep(3)
        print "skinid=", skinid
        int(skinid)
        print NewSkinId
        if skinid in NewSkinId:
            print "lm"
            time.sleep(2)
            # 搜索商品
            new_skin_top_search_goods(skinid)
            time.sleep(2)
            # 倒计时
            new_skin_top_countdown(skinid)
            time.sleep(2)
            # 电话客服
            new_skin_top_service(skinid)
            time.sleep(2)
            # 没有模块
            new_skin_top_nomodel(skinid)
            time.sleep(2)
        else:
            # 进入顶部设置倒计时模块

            # 搜索活动
            skin_top_search_active(skinid)
            time.sleep(2)
            # 搜索商品
            skin_top_search_goods(skinid)
            time.sleep(2)
            # 倒计时
            skin_top_countdown(skinid)
            time.sleep(2)
            # 电话客服
            skin_top_service(skinid)
            time.sleep(2)
            # 没有模块
            skin_top_nomodel(skinid)
            time.sleep(2)


#前7页是老皮肤,易生意只有两页皮肤，那就设3
for skin_page in range(1, 12):
    #在函数外设置先到设置皮肤页
    driver.get(url1)
    #设置的skin_page是设置皮肤的页数，因为是ajax写的，每次刷新都不在了，所以有了以下
    if (skin_page != 1):
        driver.find_element_by_class_name("form-control").clear()
        driver.find_element_by_class_name("form-control").send_keys(skin_page)
        driver.find_element_by_xpath("//*[@id='table-data-view']/form/button").click()
    print 'page=',skin_page
    time.sleep(3)
    #调用函数，一次一个页数下8个皮肤的所有顶部样式
    one_page_skin(skin_page)
    time.sleep(3)
