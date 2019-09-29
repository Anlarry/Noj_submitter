import tkinter as tk
import requests
import tkinter.messagebox
from bs4 import BeautifulSoup
from PIL import Image, ImageTk


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

        img = bs.find("img")
        img_url = ""
        if img != None:
            img_url = img.attrs["src"]
        img_url = "http://noj.cn/"+img_url if img_url != "" else ""
        pro_window(pro_name, lim, problem, img_url)
    except AttributeError:
        # print("problem may not exist")
        tk.messagebox.showinfo(title="Hi", message="problem may not exist")


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


def pro_window(pro_name, lim, problem, img_url=""):
    window = tk.Toplevel()
    window.geometry("700x700")
    window.title(pro_name)

    canvas = tk.Canvas(window, width=700, height=700)
    # canvas.pack()
    frame1 = tk.Frame(canvas)
    # frame1.pack()
    vbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=vbar.set)
    vbar.pack(side="right", fill="y")
    canvas.pack(fill="both", expand=True)
    canvas.create_window((5, 5), window=frame1, anchor="nw")
    frame1.bind("<Configure>", lambda event,
                canvas=canvas: onFrameConfigure(canvas))

    l1 = tk.Label(frame1, text=pro_name, font=14)
    l2 = tk.Label(frame1, text=lim, font=('Arial', 10), height=2)
    l1.pack()
    l2.pack()

    for i in range(len(problem)):
        frame = tk.Frame(frame1)
        frame.pack()
        frame_l = tk.Frame(frame)
        frame_r = tk.Frame(frame)
        frame_l.pack(side="left")
        frame_r.pack(side="right")
        tk.Label(frame_l, text="  ", width=5).pack()
        tk.Label(frame_r, text=problem[i][0], font=12,
                 height=2).pack(anchor="w")
        # frame = tk.Frame(canvas)
        # frame.pack()
        text = tk.Text(frame_r, font=10, width=60,
                       height=min(10, len(problem[i][1])//35+2))
        text.insert(1.0, problem[i][1])
        text.pack(anchor="w")
        if problem[i][0] == "Description" and img_url != "":
            with open(".\\tmp.jpg", "wb") as img_f:
                img_f.write(requests.get(img_url).content)
            img = Image.open(".\\tmp.jpg")
            img = ImageTk.PhotoImage(img)
            # print(img)
            tk.Label(frame_r, image=img).pack(anchor="center")
    tk.Label(frame1, text="", height=2).pack()
    # canvas.configure(yscrollcommand=vbar.set)
    # canvas.yview_moveto(0.0)
    window.mainloop()

# def pro_window(pro_name, lim, problem):
#     window = tk.Tk()
#     window.geometry("700x700")
#     window.title(pro_name)

#     l1 = tk.Label(window, text=pro_name, font = 14)
#     l2 = tk.Label(window, text=lim, font=('Arial', 10), height = 2)
#     l1.place(x=350-len(pro_name)*7, y=30)
#     l2.place(x = 200, y = 60)

#     for i in range(len(problem)):
#         tk.Label(window, text=problem[i][0], font = 12, height=2).place(x = 30, y=100+120 * i)
#         text = tk.Text(window, font=10, width=60, height=3)
#         text.insert(1.0, problem[i][1])
#         text.place(x=30, y=100+120*i+40)

#     window.mainloop()
