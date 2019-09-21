import tkinter as tk
import requests
from bs4 import BeautifulSoup
import re
import tkinter.messagebox

def view_ac_code(user_var, pd_var):
    # if user == "" and pd == ""
    window = tk.Tk()
    window.geometry("300x200")
    window.title("Code search")
    l = tk.Label(window, text='Input the problem Id', font=12, height=2)
    l.pack()
    pro_id = tk.StringVar()
    e_Id = tk.Entry(window, font=12, text=pro_id)
    e_Id.pack()

    # user = str(user_var.get())
    # pd = str(pd_var.get())
    b = tk.Button(window, text="View AC Code",command=lambda:show_code(user_var, pd_var, str(e_Id.get())))
    b.pack()
    window.mainloop()
    return

def show_code(user_var, pd_var, pro_id):
    user = str(user_var.get())
    pd = str(pd_var.get())
    log_url = "http://noj.cn/Problem.asp?a=i"
    sta_url = "http://noj.cn/?a=a&t=s&s="
    log_para = {
        "Password": pd,
        "User": user
    }
    s = requests.Session()
    try:
        out_time = 2.0
        with open(".\out_time.txt", "r") as time_file:
            out_time = float(time_file.readline())
        log_req = s.post(log_url, data=log_para, timeout=out_time)
        print(log_req.status_code)
        print(log_req.text)
        if "错误" in log_req.text:
            tk.messagebox.showinfo(title="Hi", message="user info may not correct")
            return 
        sta_num = get_ac_sta_num(user, pd, pro_id)
        url = sta_url+sta_num
        html = s.get(url).text
        html = (html.replace("<br />", "\n")).replace("<br/>", "\n")
        html = html.replace("<BR>", "\n")

        bs = BeautifulSoup(html, "lxml")
        src = bs.find("pre").get_text()
        show_src(src)

    except requests.exceptions.Timeout:
        tk.messagebox.showinfo(title="Hi", message="connect time out")
    except AttributeError:
        tk.messagebox.showinfo(title="Hi", message="may not AC")
    return 
    # print(fir_num.td.get_text())
    
def get_ac_sta_num(user, pd, pro_id):
    # sta_url = "http://noj.cn/?a=s&p=559464&d=1&u=2018302278"
    sta0_url = "http://noj.cn/?a=s"
    # sta_url = "http://noj.cn/?a=s&p="

    html = requests.get(sta0_url).text
    # html.find("tr", {"class":"odd"})
    bs = BeautifulSoup(html, "lxml")
    fir_num = bs.find("tr", {"class": "odd"}).td.get_text()

    # sta_url += str(fir_num) + "&d=1&u="+user
    cnt = 1
    while True:
        print("%d%c"%(cnt, '\r'), end = "")
        cnt += 1
        url = get_next_url(fir_num, user)
        html = requests.get(url).text
        bs = BeautifulSoup(html, "lxml")
        # sta_list = bs.find_all("", text=user)
        sta_list = bs.find_all("tr", {"class":re.compile("odd|even")})
        if sta_list == []:
            break
        for each in sta_list:
            # if pro_id in each.get_text():
            tmp_id = each.td.next_sibling.next_sibling
            tmp_sta = tmp_id.next_sibling
            # print(tmp_id.get_text(), tmp_sta.get_text())
            if pro_id == tmp_id.get_text() and "Accept" in tmp_sta.get_text():
                return each.td.get_text()
                # print(each.td.get_text())
        fir_num = sta_list[-1].td.get_text()
    return ""
    
def get_next_url(fir_num, user):
    sta_url = "http://noj.cn/?a=s&p="
    return sta_url + str(fir_num) + "&d=1&u="+user

def show_src(src):
    window = tk.Tk()
    window.geometry("400x400")
    text = tk.Text(window)
    text.insert(1.0, src)
    text.pack()
    window.mainloop()

# print(get_ac_sta_num("2018302278", "wesd", "1611"))
