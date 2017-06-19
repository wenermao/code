#-*- coding=utf-8 -*-
#coding:utf-8
#coding:windows-1252
import codecs
import chardet
#提交订单但是不付款
#本脚本不适合地址、血型的活动，因为我不会读取中文，2.28最新，我再改改应该能
import xlrd, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


address = raw_input('Enter location(报名页网址有id、mid、styleClassId、useDeposit的那种): ')
if len(address) < 1:
    print "error"

url = address
print 'Retrieving', url
profile_dir = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\5cmfbcqp.default"
profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)

def open_excel(file ='sign_up.xlsx'):
    try:
        # data = xlrd.codecs.open_workbook(file, "r", "utf-8")
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print (str(e))
def excel_table_byindex(file='sign_up.xlsx',colnameindex = 0,by_index= 0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    #行
    colnames = table.row_values(colnameindex)
    #列内容
    list=[]
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                s = row[i]
                if isinstance(s, unicode):
                    s = row[i].encode("utf-8")
                # 打印内容
                # print s
                app[colnames[i]] = s
            list.append(app)
    #打印内容
    # print (list)
    return list
#通过css判断是否存在
def judgewithcss(css):
    try:
        driver.find_element_by_css_selector(css)
    except:
        return False
    return True

# print chardet.detect(listdata[i][是为了先查看他的原字符编码，万一报错就改变decode和encode里的编码
def Signup():
    listdata=excel_table_byindex("E:\py\can_use\sign_up.xlsx",0)
    if(len(listdata)<0):
        assert 0,u"数据异常"
    #临时修改了5开始，应该是1
    for i in range(0, len(listdata)):

        #因为手动输入，所以这里注释掉了
        driver.get(url)
        #昵称
        if judgewithcss("#id_101_0") == True:
            nickname = driver.find_element_by_id("id_101_0")
            nickname.clear()
            #这是打印出类型，都可以注释掉，打印出来出错的时候方便看
            print chardet.detect(listdata[i]['nickname'])
            nickname.send_keys(listdata[i]['nickname'].decode("utf-8"))

        # 真实姓名
        if judgewithcss("#id_104_0") == True:
            realname = driver.find_element_by_id("id_104_0")
            realname.clear()
            print chardet.detect(listdata[i]['realname'])
            realname.send_keys(listdata[i]['realname'].decode("utf-8"))
        # 国籍
        if judgewithcss("#id_107_0") == True:
            country = driver.find_element_by_id("id_107_0")
            country.clear()

            country.send_keys(listdata[i]['country'].decode('utf-8'))
        # 用select模块找到性别女
        if judgewithcss("#id_110_0") == True:
            gender = driver.find_element_by_id("id_110_0")
            print chardet.detect(listdata[i]['gender'])
            Select(gender).select_by_value(listdata[i]['gender'])
        # 找到O型血
        if judgewithcss("#id_113_0") == True:
            blood = driver.find_element_by_id("id_113_0")
            print chardet.detect(listdata[i]['blood'])
            Select(blood).select_by_value(listdata[i]['blood'].decode("windows-1252").encode("windows-1252"))
        # 身高
        if judgewithcss("#id_116_0") == True:
            height = driver.find_element_by_id("id_116_0")
            height.clear()
            height.send_keys(int(listdata[i]['height']))
        # 体重
        if judgewithcss("#id_119_0") == True:
            weight = driver.find_element_by_id("id_119_0")
            weight.clear()
            weight.send_keys(int(listdata[i]['weight']))
        # 生日
        if judgewithcss("#id_122_0") == True:
            birthday = driver.find_element_by_id("id_122_0")
            birthday.clear()
            birthday.send_keys(listdata[i]['birthday'])
        # 年龄
        if judgewithcss("#id_125_0") == True:
            age = driver.find_element_by_id("id_125_0")
            age.clear()
            age.send_keys(int(listdata[i]['age']))

        # 手机号码
        if judgewithcss("#id_128_0") == True:
            phone = driver.find_element_by_id("id_128_0")
            phone.clear()
            phone.send_keys(int(listdata[i]['phone']))

        # 固定电话
        if judgewithcss("#id_131_0") == True:
            landline = driver.find_element_by_id("id_131_0")
            landline.clear()
            landline.send_keys(int(listdata[i]['landline']))

        # 电子邮箱
        if judgewithcss("#id_134_0") == True:
            email = driver.find_element_by_id("id_134_0")
            email.clear()
            print chardet.detect(listdata[i]['email'])
            email.send_keys(listdata[i]['email'])

        # 证件信息
        if judgewithcss("#id_137_0") == True:
            identity = driver.find_element_by_xpath("//select[@id='id_137_0']")
            identityNumber = driver.find_element_by_xpath("//input[@id='id_137_0']")
            print chardet.detect(listdata[i]['identity'])
            Select(identity).select_by_value(listdata[i]['identity'])
            identityNumber.clear()
            print chardet.detect(listdata[i]['identityNumber'])
            identityNumber.send_keys(listdata[i]['identityNumber'])

        # 紧急联系人
        if judgewithcss("#id_140_0") == True:
            contact = driver.find_element_by_id("id_140_0")
            contactNumber = driver.find_element_by_xpath("//input[@name='emergencyContactPersonPhone']")
            contact.clear()
            print chardet.detect(listdata[i]['contact'])
            contact.send_keys(listdata[i]['contact'].decode("utf-8"))
            contactNumber.clear()
            contactNumber.send_keys(int(listdata[i]['contactNumber']))

        # 学历
        if judgewithcss("#id_143_0") == True:
            education = driver.find_element_by_id("id_143_0")
            print chardet.detect(listdata[i]['education'])
            Select(education).select_by_value(listdata[i]['education'].decode("utf-8").encode("utf-8"))
        # 居住地
        if judgewithcss("#id_146_0") == True:
            houseaddress = driver.find_element_by_id("id_146_0")
            houseaddressprovince = driver.find_element_by_xpath("//select[@name='houseAddressProvince']")
            print chardet.detect(listdata[i]['houseaddressprovince'])
            Select(houseaddressprovince).select_by_value(listdata[i]['houseaddressprovince'].decode("utf-8").encode("utf-8"))
            houseaddresscity = driver.find_element_by_xpath("//select[@name='houseAddressCity']")
            print chardet.detect(listdata[i]['houseaddresscity'])
            Select(houseaddresscity).select_by_value(listdata[i]['houseaddresscity'].decode("utf-8").encode("utf-8"))
            # 可不填具体地址
            houseaddress.clear()
            print chardet.detect(listdata[i]['houseaddress'])
            houseaddress.send_keys(listdata[i]['houseaddress'].decode("utf-8"))
        # 通信地址
        if judgewithcss("#id_149_0") == True:
            mailaddress = driver.find_element_by_id("id_149_0")
            mailaddressprovince = driver.find_element_by_xpath("//select[@name='mailAddressProvince']")
            print chardet.detect(listdata[i]['mailaddressprovince'])
            Select(mailaddressprovince).select_by_value(listdata[i]['mailaddressprovince'].decode("utf-8").encode("utf-8"))
            mailaddresscity = driver.find_element_by_xpath("//select[@name='mailAddressCity']")
            print chardet.detect(listdata[i]['mailaddresscity'])
            Select(mailaddresscity).select_by_value(listdata[i]['mailaddresscity'].decode("utf-8").encode("utf-8"))
            # 可不填具体地址
            mailaddress.clear()
            print chardet.detect(listdata[i]['mailaddress'])
            mailaddress.send_keys(listdata[i]['mailaddress'].decode("utf-8"))

        # 职业
        if judgewithcss("#id_152_0") == True:
            job = driver.find_element_by_id("id_152_0")
            job.clear()
            print chardet.detect(listdata[i]['job'])
            job.send_keys(listdata[i]['job'].decode("utf-8"))

        # 月收入
        if judgewithcss("#id_155_0") == True:
            income = driver.find_element_by_id("id_155_0")
            income.clear()
            income.send_keys(int(listdata[i]['income']))
        # 工作单位
        if judgewithcss("#id_158_0") == True:
            company = driver.find_element_by_id("id_158_0")
            company.clear()
            print chardet.detect(listdata[i]['company'])
            company.send_keys(listdata[i]['company'].decode("utf-8"))
        # 服装尺寸
        if judgewithcss("#id_161_0") == True:
            size = driver.find_element_by_id("id_161_0")
            print chardet.detect(listdata[i]['size'])
            Select(size).select_by_value(listdata[i]['size'])

        # 订单备注
        driver.find_element_by_id("remark").clear()
        print chardet.detect(listdata[i]['tips'])
        driver.find_element_by_id("remark").send_keys(listdata[i]['tips'].decode("utf-8"))

        # 将滚动条滚下来
        # js = "var q=document.documentElement.scrollTop=800"
        # driver.execute_script(js)
        # ----------------
        target = driver.find_element_by_id("remark")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        # 加购物车
        # driver.find_element_by_id("addToCart").click()
        # 提交订单
        driver.find_element_by_id("submitButton").click()

        time.sleep(2)
if __name__ == '__main__':
    Signup()