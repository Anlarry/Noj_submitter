import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import messagebox
from functools import partial
from show_problem_window import pro_window
from language_init import init_lan
from but_cmd import change_lan
from cur_contest_submit import submit


def show_contest(user_var, pd_var):
    cur_list = get_cur_contest()
    user = str(user_var.get())
    pd = str(pd_var.get())
    if cur_list == requests.exceptions.Timeout:
        tk.messagebox.showinfo(title="Hi", message="connext time out")
        return
    window = tk.Tk()
    height = str(len(cur_list)*75)
    window.geometry("500x"+height)
    for name, con_id in cur_list:
        tk.Label(window, text="").pack()
        tk.Button(window, text=name, font=3, height=1, command=partial(
            enter_contest, con_id, user, pd)).pack()
    window.mainloop()
    return


def get_cur_contest():
    cur_list = []  # [[name, id]]
    url = "http://noj.cn/practise.asp"
    try:
        out_time = 2.0
        with open(".\out_time.txt", "r") as time_file:
            out_time = float(time_file.readline())
        html = requests.get(url, timeout=out_time).text
        # print(html)
        bs = BeautifulSoup(html, "lxml")
        option = bs.find_all("option", value=re.compile("[1-9][0-9][0-9]"))
        for each in option:
            cur_list.append([each.get_text(), each.attrs["value"]])
        return cur_list
    except requests.exceptions.Timeout:
        return requests.exceptions.Timeout
    return


def enter_contest(con_id, user, pd):
    log_url = "http://noj.cn/practise.asp?a=i"
    pro_url = "http://noj.cn/Contest.asp?a=p"
    cid_para = "&cid="+str(con_id)
    s = requests.Session()
    log_para = {
        "Password": pd,
        "User": user,
        "CID": str(con_id),
    }
    Html = s.post(log_url, data=log_para).text
    pro_name_list = get_pro_name(Html)
    if len(pro_name_list) == 0:
        tk.messagebox.showinfo(title="Hi", message="may not enter user info")
        return
    pro_list = []
    for each in pro_name_list:
        pro_para = "&pid="+str(each[1])  # A-Z
        url = pro_url+pro_para+cid_para
        html = s.get(url).text
        html = (html.replace("<br />", "\n")).replace("<br/>", "\n")
        html = html.replace("<BR>", "\n")
        # print(html)
        bs = BeautifulSoup(html, "lxml")
        name, lim, pro_info = get_pro(bs)
        # print(pro_info)
        # print(name)
        name = each[0]+'_'+each[1]+'_'+each[2]
        if pro_info == []:
            break
        # print(pro_info)
        problem = Problem(pro_info)
        img = bs.find("img")
        img_url = ""
        if img != None:
            img_url = img.attrs["src"]
        img_url = "http://noj.cn/"+img_url if img_url != "" else ""
        pro_list.append([name, lim, problem, img_url])

    show_problems(s, con_id, pro_name_list, pro_list, user, pd)
    return

# print(get_cur_contest())


def get_pro(bs):
    try:
        names = bs.find_all("h3", limit=2)
        if names == []:
            return "", "", []
        name = names[0].get_text()+names[1].get_text()
        lim = bs.find("h4").get_text()
        tmp_info = bs.find_all("p", {"align": "left"})
        pro_info = []
        for i in range(5):
            pro_info.append(tmp_info[2 * i+1].get_text())
        return name, lim, pro_info
    except AttributeError:
        return "", "", []


def show_problems(s: requests.Session, CID, pro_name_list, pro_list, user, pd):
    window = tk.Tk()
    height = str(len(pro_list) * 75)
    window.geometry("500x"+height)

    frame1 = tk.Frame(window)
    frame2 = tk.Frame(window)
    frame3 = tk.Frame(window)
    frame1.pack()
    frame2.pack()
    frame3.pack()

    for name, lim, pro_info, img_url in pro_list:
        tk.Label(frame1, text="").pack()
        tk.Button(frame1, text=name, command=partial(
            pro_window, name, lim, pro_info, img_url), font=3, height=1).pack()
    frame2_l = tk.Frame(frame2)
    frame2_r = tk.Frame(frame2)
    frame2_l.pack(side="left")
    frame2_r.pack(side="right")
    frame3_l = tk.Frame(frame3)
    frame3_r = tk.Frame(frame3)
    frame3_l.pack(side="left")
    frame3_r.pack(side="right")

    l_pro = tk.Label(frame2_l, text="problem: ", font=12, height=1)
    l_pro.pack()
    l_file = tk.Label(frame2_l, text="file: ", font=12, height=1)
    l_file.pack()

    e_pro = tk.Entry(frame2_r, font=12)
    e_pro.pack()
    e_file = tk.Entry(frame2_r, font=12)
    e_file.pack()

    now_lan = tk.StringVar()
    init_lan(now_lan)
    lan_b = tk.Button(frame3_l, text=now_lan.get(),
                      command=lambda: change_lan(now_lan, lan_b))
    lan_b.pack()
    b = tk.Button(frame3_r, text="Submit", command=lambda: submit(
        s, CID, pro_name_list, user, pd, e_pro, e_file))
    b.pack()
    window.mainloop()
    return


def Problem(pro_info):
    problem = [
        ["Description"],
        ["Input"],
        ["Output"],
        ["Sample Input"],
        ["Sample Output"]
    ]
    for i in range(5):
        problem[i].append(pro_info[i])
    return problem


def get_pro_name(html):
    name_list = []  # [[p, cp, name]]
    bs = BeautifulSoup(html, "lxml")
    for each in bs.find_all('tr', {"class": "no"}):
        l = []
        for child in each.children:
            l.append(child.get_text())
        name_list.append(l[1:])
    return name_list
