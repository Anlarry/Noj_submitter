import requests
from bs4 import BeautifulSoup
import time
# url = "http://noj.cn/"
# url = "http://noj.cn/?a=p&v=1&r=0"
url = "http://noj.cn/Problem.asp?a=t" #submit url
log_url = "http://noj.cn/Problem.asp?a=i"
# url = "http://noj.cn/practise.asp?a=t"
# log_url = "http://noj.cn/practise.asp?a=i"
# sta_url = "http://noj.cn/?a=s"
# req = requests.get(url)
log_para = {
    "Password" : "654183Wang",
    "User": "2018302278",
    "CID":"375"
}
para = {
   'PID': '1234',
   "language": "1",
   "Source":
   '''
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    return 0;
}
   '''
   }
s = requests.Session()
log_req = s.post(log_url, data = log_para)
print(log_req.text)

req = requests.post(url, data=para) #submit
req.encoding = "gbk"
print(req.status_code)
time.sleep(1)
# print(para["Source"])

sta_req = requests.get(sta_url)
sta_req.encoding = "gbk"
html = sta_req.text
bs = BeautifulSoup(html, "lxml")
user_sta = bs.find("td", text = log_para["User"]).parent
# time.sleep(10)
# print(user_sta)
sta_list = [["提交号"],["学号"],["题目"],["测评结果"], ["语言"], ["时间"], ["内存"],["提交时间"]]
for (tag, sta) in zip(user_sta, sta_list):
    # print(sibling.get_text())
    sta.append(tag.get_text())
for each_sta in sta_list:
    print(each_sta[0],": ", each_sta[1])
