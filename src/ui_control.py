import  tkinter as tk
import tkinter.messagebox
import  main, password
from but_cmd import show_detail
from get_code import get_code
def get_entry_info(e:tk.Entry):
    return str(e.get())

def Submit(user, pd, pro, F):
    "user, password, problem, file(all Entry), return state list"
    user = get_entry_info(user)
    pd = get_entry_info(pd)
    pro = get_entry_info(pro)
    F = get_entry_info(F)

    # print(user, pd, pro, F)

    log_para = {
        "Password": pd,
        "User": user
    }
    src = get_code(F)
    submit_para = {
        'PID': pro,
        "language": "3", #c++ 1 G++ 3
        "Source": src
    }
    with open("language.txt", "r") as F:
        submit_para["language"] = int(F.readline())
    sta_list = main.log_submit(log_para, submit_para)
    if sta_list == main.SubmitError:
        print(main.SubmitError)

    # for each_sta in sta_list:
    #     print(each_sta[0], ": ", each_sta[1])
    # return 
    return sta_list

def Save(user, pd):
    "save user and password"
    user = get_entry_info(user)
    pd = get_entry_info(pd)
    sta = password.Insert(user, pd)   
    show(sta)

def show(info):
    if type(info) == str :
        tk.messagebox.showinfo(title="Hi", message = info)
        
    elif  type(info) is list :
        window = tk.Tk()
        window.geometry("400x400")
        window.title("Hi")

        frame = tk.Frame(window)
        frame.pack()

        frame_l = tk.Frame(frame)
        frame_r = tk.Frame(frame)
        frame_l.pack(side = "left")
        frame_r.pack(side = "right")

        for each_sta in info:
            tk.Label(frame_l, text = each_sta[0], font = 12, width = 12, height = 2).pack()
            tk.Label(frame_r, text=each_sta[1], font=12, width=12, height=2).pack()

        b = tk.Button(window, text = "Detail", command = lambda : show_detail(info[0][1], info[3][1]))
        b.pack()    

        window.mainloop()

    else:
        tk.messagebox.showinfo(title="Hi", message="type error, list or string")

    return 
