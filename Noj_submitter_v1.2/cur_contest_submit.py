import requests
import tkinter as tk
import main
from ui_control import show
import time
from bs4 import BeautifulSoup
from get_code import get_code
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from put_to_board import settext, gettext
import selenium


def submit(s: requests.Session, CID, pro_name_list, user, pd, e_pro, e_file):
    "post请求出错，换selenium模拟"
    old_text = gettext()
    pro = str(e_pro.get())
    F = str(e_file.get())

    url = "http://noj.cn/practise.asp"
    driver = webdriver.Ie(executable_path='.\IEDriverServer.exe')
    driver.get(url)
    sel = driver.find_element_by_name("CID")
    Select(sel).select_by_value(str(CID))
    settext(user)
    driver.find_element_by_xpath(
        "//input[@name='User']").send_keys(Keys.CONTROL, 'v')
    # elem_user = driver.find_element_by_xpath("//input[@name='User']")
    # elem_user.send_keys(user)
    settext(pd)
    driver.find_element_by_xpath(
        "//input[@name='Password']").send_keys(Keys.CONTROL, 'v')
    elem_pd = driver.find_element_by_xpath("//input[@name='Password']")
    # elem_pd.send_keys(pd)
    elem_pd.send_keys(Keys.ENTER)

    name = ''
    for each in pro_name_list:
        if each[0] == pro:
            name = each[2]
            break
    xpath_para = "//*[text()="+"'"+name+"'"+"]"
    driver.find_element_by_xpath(xpath_para).send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//input[@value='提交']").send_keys(Keys.ENTER)
    sel = driver.find_element_by_name("language")
    lan = ""
    with open(".\language.txt", "r") as t_file:
        lan = int(t_file.readline())
    lan = str(lan)
    Select(sel).select_by_value(lan)
    src = get_code(F)
    settext(src)
    driver.find_element_by_name("Source").send_keys(Keys.CONTROL, 'v')
    # src = "3esdgdssgfsdfsdf"
    #慢
    # driver.find_element_by_name("Source").send_keys(src)
    # js = 'document.getElementById("Source").value="'+str(src)+'"'
    # driver.execute_script(js)

    driver.find_element_by_name("SB").send_keys(Keys.ENTER)

    try:
        dialog_box = driver.switch_to.alert
        dialog_box.accept()
        dialog_box = driver.switch_to.alert
        dialog_box.accept()
        #get state
    except selenium.common.exceptions.NoAlertPresentException:
        pass
    finally:
        settext(old_text)
        # driver.close()
        driver.quit()
        sta_list = get_submit_sta(user)
        show(sta_list)

    ''' 
    pro = str(e_pro.get())
    F = str(e_file.get())
    CP = ""
    for each in pro_name_list:
        if each[0] == pro:
            CP = each[1]
            break
    src = get_code(F)
    submit_para = {
        "CID":CID,
        "CP":CP,
        "language": "3",  # c++ 1 G++ 3
        "P":pro,
        "Source": src
    }
    with open(".\language.txt", "r") as F:
        submit_para["language"] = int(F.readline())

    sta_list = get_submit_sta(s, CID, submit_para, user)
    show(sta_list)
    return 
    '''


def get_submit_sta(user):
    try:
        '''
        # sb_url = "http://noj.cn/practise.asp?a=t"

        # sta_res = s.post(sb_url, data=sb_para)
        # print(sta_res.status_code)
        # time.sleep(2)
        '''
        sta_url = "http://noj.cn/?a=s"
        #get submit state
        sta_req = requests.get(sta_url)
        sta_req.encoding = "gbk"
        html = sta_req.text
        #html
        bs = BeautifulSoup(html, "lxml")
        user_sta = bs.find("td", text=str(user)).parent
        #
        sta_list = [["提交号"], ["学号"], ["题目"], [
            "测评结果"], ["语言"], ["时间"], ["内存"], ["提交时间"]]
        for (tag, sta) in zip(user_sta, sta_list):
                sta.append(tag.get_text())
        return sta_list
    except requests.exceptions.Timeout:
        return "connect time out"
