import tkinter as tk
from bs4 import BeautifulSoup
import requests
import re
from functools import partial
# from show_problem_window import show_problem
# import show_problem_window


def show_model(url_list):
    window = tk.Tk()
    height = str(len(url_list) * 70)
    size = "500x"+height
    window.geometry(size)

    for name, url in url_list:
        tk.Label(window, text="").pack()
        b = tk.Button(window, text=name,
                      command=lambda: enter_model(url), font=3, height=1)
        # w1, w2 = window.winfo_screenwidth(), b.winfo_screenmmwidth()
        b.pack()

    window.mainloop()
    return


def enter_model(url):
    html = requests.get(url).text
    bs = BeautifulSoup(html, "lxml")
    tag = bs.findAll("a", href=re.compile("javascript.+"))
    pro_list = []
    for each in tag:
        pro_id = each.attrs["href"][-5:-1]
        pro_list.append([each.get_text(), pro_id])
    show_problems(pro_list)
    # window = tk.Tk()
    # height = str(len(pro_list) * 75)
    # window.geometry("500x"+height)
    # # print(pro_list)
    # for name, pro_id in pro_list:
    #     # print(name, pro_id)
    #     tk.Label(window, text="").pack()
    #     b = tk.Button(window, text=name, command=lambda:show_problem(pro_id),font =3,height=1)
    #     b.pack()
    # window.mainloop()
    # return


def show_problems(pro_list):
    window = tk.Tk()
    height = str(len(pro_list) * 75)
    window.geometry("500x"+height)
    # print(pro_list)
    for name, pro_id in pro_list:
        # print(name, pro_id)
        tk.Label(window, text="").pack()
        # url = "http://noj.cn/?a=p&p="+str(pro_id)
        tk.Button(window, text=name, command=partial(
            show_problem, pro_id), font=3, height=1).pack()
    window.mainloop()
    return

# def cmd(pro_id):
#     return lambda : show_model(pro_id)


def show_problem(id):
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

        html = requests.get(url).text
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

        pro_window(pro_name, lim, problem)
    except AttributeError:
        # print("problem may not exist")
        tk.messagebox.showinfo(title="Hi", message="problem may not exist")


def pro_window(pro_name, lim, problem):
    window = tk.Tk()
    window.geometry("700x700")
    window.title(pro_name)

    l1 = tk.Label(window, text=pro_name, font=14)
    l2 = tk.Label(window, text=lim, font=('Arial', 10), height=2)
    l1.place(x=290, y=30)
    l2.place(x=200, y=60)

    for i in range(len(problem)):
        tk.Label(window, text=problem[i][0], font=12,
                 height=2).place(x=30, y=100+120 * i)
        text = tk.Text(window, font=10, width=60, height=3)
        text.insert(1.0, problem[i][1])
        text.place(x=30, y=100+120*i+40)

    window.mainloop()
