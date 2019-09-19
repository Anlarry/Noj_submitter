import  requests
from bs4 import  BeautifulSoup
import time
from selenium import  webdriver

SubmitError = "connect time out"

def log_submit(log_para, sb_para):
    "log info, submit info, return submit state"
    sb_url = "http://noj.cn/Problem.asp?a=t"  # submit url
    log_url = "http://noj.cn/Problem.asp?a=i"
    sta_url = "http://noj.cn/?a=s"

    s = requests.Session()
    try:
        log_req = s.post(log_url, data=log_para, timeout = 2.0)

        #submit
        req = s.post(sb_url, data = sb_para)
        req.encoding = 'gbk'
        print(req.status_code)
        time.sleep(2)
        #get submit state
        sta_req = requests.get(sta_url)
        sta_req.encoding = "gbk"
        html = sta_req.text
        # html
        bs = BeautifulSoup(html, "lxml")
        user_sta = bs.find("td", text = log_para["User"]).parent
        # 
        sta_list = [["提交号"],["学号"],["题目"],["测评结果"], ["语言"], ["时间"], ["内存"],["提交时间"]]
        for (tag, sta) in zip(user_sta, sta_list):
            sta.append(tag.get_text())

        # print(sta_list)

        return sta_list
    except requests.exceptions.Timeout:
        return "connect time out"
    except AttributeError:
        return "problem may not exist"
