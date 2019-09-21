import tkinter as tk
import requests
import tkinter.messagebox
from bs4 import BeautifulSoup

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

    l1 = tk.Label(window, text=pro_name, font = 14)
    l2 = tk.Label(window, text=lim, font=('Arial', 10), height = 2)
    l1.place(x=350-len(pro_name)*7, y=30)
    l2.place(x = 200, y = 60)

    for i in range(len(problem)):
        tk.Label(window, text=problem[i][0], font = 12, height=2).place(x = 30, y=100+120 * i)
        text = tk.Text(window, font=10, width=60, height=3)
        text.insert(1.0, problem[i][1])
        text.place(x=30, y=100+120*i+40)
    
    window.mainloop()
