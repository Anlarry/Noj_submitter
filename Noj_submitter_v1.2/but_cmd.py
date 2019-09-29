import tkinter as tk
from bs4 import BeautifulSoup
import requests
from show_problem_window import pro_window
import tkinter.messagebox
import re
from show_model import show_model
import test_detail
from functools import partial


def show_pro(id):
    try:
        "search problem by id, then show in the new window"
        problem = [
            ["Description"],
            ["Input"],
            ["Output"],
            ["Sample Input"],
            ["Sample Output"]
        ]
        url = "http://noj.cn/?a=p&p="
        url += str(id)
        out_time = 2.0
        with open(".\out_time.txt", "r") as time_file:
            out_time = float(time_file.readline())
        html = requests.get(url, timeout=out_time).text
        # print(html)
        html = (html.replace("<br />", "\n")).replace("<br/>", "\n")
        html = html.replace("<BR>", "\n")
        # print(html)
        bs = BeautifulSoup(html, "lxml")

        pro_name = bs.find("h3").get_text()
        lim = bs.find("h4").get_text()
        pro_info = bs.find_all("div", {"class": "panel_content"})

        for i in range(5):
            # print(pro_info[i].get_text())
            problem[i].append(pro_info[i].get_text())

        img = bs.find("img")
        img_url = ""
        if img != None:
            img_url = img.attrs["src"]
        img_url = "http://noj.cn/"+img_url if img_url != "" else ""
        pro_window(pro_name, lim, problem, img_url)

    except requests.exceptions.Timeout:
        tk.messagebox.showinfo(title="Hi", message="connect time out")
    except AttributeError:
        # print("problem may not exist")
        tk.messagebox.showinfo(title="Hi", message="problem may not exist")


def view_algorithm_model():
    try:
        url = "http://noj.cn/?a=x&x=4"
        num_to_show = 0
        with open(".\\num_to_show_model.txt", "r") as F:
            num_to_show = int(F.readline())
        out_time = 2
        with open(".\out_time.txt", "r") as time_file:
            out_time = float(time_file.readline())
        html = requests.get(url, timeout=out_time).text
        bs = BeautifulSoup(html, "lxml")
        tag = bs.findAll("a", {"href": re.compile("javascript.+")})
        target_url = []
        for i in range(num_to_show):
            # print(tag[i])
            Id = tag[i].attrs["href"][-5:-2]
            t_url = "http://noj.cn/?a=x&t=t&x="+str(Id)
            target_url.append([tag[i].get_text(), t_url])

        # print(target_url)
        show_model(target_url)
    except requests.exceptions.Timeout:
        tk.messagebox.showinfo(title="Hi", message="connect time out")
    return


def show_detail(post_id, post_sta):
    url = ""
    data_list = []
    if "Compile Error" not in post_sta:
        url = "http://noj.cn/?a=y&sid="+str(post_id)
        data_list = test_detail.get_data_info(url)
    else:
        url = "http://noj.cn/ce.asp?sid="+str(post_id)
    resp = requests.get(url)
    html = resp.text
    # html = requests.get(url).text
    # head = resp.headers
    html = (html.replace("<br />", "\n")).replace("<br/>", "\n")
    html = html.replace("<BR>", "\n")
    bs = BeautifulSoup(html, "lxml")

    info = ""
    title = bs.find_all("title")
    if len(title) != 0:
        info = bs.find("pre").get_text()
    else:
        # info = list()
        # S = bs.findAll("", text=re.compile("测试点.+"))
        # print(S)
        # S = bs.find_all("a")
        # for each in S:
        #     info.append(each.get_text())
        S = bs.find("body")
        info = S.get_text()
        # info = list(info.split('\n'))
    print(info)

    window = tk.Tk()
    window.geometry("400x400")
    text = tk.Text(window)
    # if type(info) == str:
    text.insert(1.0, info)
    # else:
    #     for i in range(len(info)):
    #         text.insert(i+1, str(info[i]))
    text.pack()

    for sid, test in data_list:
        tk.Button(window, text="查看错误详情", command=partial(
            test_detail.show_data, sid, test)).pack()
    window.mainloop()


def change_lan(lan: tk.StringVar, lan_b):
    s_lan = lan.get()
    if s_lan == "C++":
        with open(".\language.txt", "w") as F:
            print(3, file=F)
        lan.set("G++")
    else:
        with open(".\language.txt", "w") as F:
            print(1, file=F)
        lan.set("C++")
    lan_b["text"] = lan.get()


# def debug():
#     # show_pro(1534)
#         # view_algorithm_model()
#     show_detail(553842, "正确Accepted")
# debug()
# show_detail(560752, "答案错误Wrong Answer")
