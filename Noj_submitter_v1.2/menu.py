import  tkinter as tk
import password, but_cmd
import  tkinter.messagebox
from  cur_contest import show_contest
from view_AcCode import view_ac_code

def creat_menu(window, user_var, pd_var):
    "window, user name Entry, password Entry"
    menubar = tk.Menu(window)
    user_menu = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "User", menu = user_menu)

    user_list = password.get_user() #dict
    for user, _ in user_list.items():
        user_menu.add_command(label=user, command=lambda: auto_fill(user, _, user_var, pd_var))
    user_menu.add_separator()
    user_menu.add_command(label="Clear user", command=lambda : clear(user_menu))

    # creat menu to view problem .. add algorithm model, cur_contest
    view_pro_menu(menubar, user_var, pd_var)
    # creat menu to view Ac code 
    view_code_menu(menubar, user_var, pd_var)
    #show menu
    window.config(menu = menubar)

def view_pro_menu(menubar, user_var, pd_var):
    pro_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Problem", menu=pro_menu)

    pro_menu.add_command(label="Algorithm", command=but_cmd.view_algorithm_model)

    # creat menu to view curent contest
    pro_menu.add_command(label="CurrentContest", command=lambda :show_contest(user_var, pd_var))
    # now_contest(menubar, user_var, pd_var)

    pro_menu.add_separator()
    pro_menu.add_command(label="Veiw by Id", command=view_pro)


# def now_contest(menubar, user_var, pd_var):
#     "menubar, user name Entry, password Entry"
#     contest_list = cur_contest.get_cur_contest()

#     return

def view_code_menu(menubar, user_var, pd_var):
    code_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Code", menu=code_menu)

    # user = str(user_var.get())
    # pd = str(pd_var.get())
    code_menu.add_command(label="Code", command=lambda : view_ac_code(user_var, pd_var))

def auto_fill(user_name, pd, user_var:tk.StringVar, pd_var:tk.StringVar):
    # e_user.insert("start", user_name)
    # e_pd.insert("start", pd)
    user_var.set(user_name)
    pd_var.set(pd)

def view_pro():
    window = tk.Tk()
    window.geometry("300x200")
    window.title("problem search")

    l = tk.Label(window, text = 'Input the problem Id', font = 12, height = 2)
    l.pack()

    pro_id = tk.StringVar()
    e_Id = tk.Entry(window, font = 12, text = pro_id)
    e_Id.pack()

    b = tk.Button(window, text = "Search", command = lambda:but_cmd.show_pro(e_Id.get()))
    b.pack()

def clear(user_menu:tk.Menu):
    try:
        user_menu.delete(0)
        F = open(".\password.txt", "a")
        F.seek(0)
        F.truncate()
        F.close()
    except IOError:
        tk.messagebox.showinfo(title="Hi", message="can not find password.txt")
