import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import ui_control, main, menu
from language_init import init_lan
from but_cmd import change_lan
# init window
window = tk.Tk()
window.geometry("700x500")
window.title("tkinter GUI -- NOJ Submitter")

#creat canvas
canvas = tk.Canvas(window, height = 200, width = 700)
img_file = tk.PhotoImage(file=".\\img.gif")
img = canvas.create_image(350, 0, anchor="n", image=img_file)
canvas.pack()

#frame
# frame = tk.Frame(window)
# frame.pack()

# frame_l = tk.Frame(frame)
# frame_r = tk.Frame(frame)
# frame_l.pack(side = "left")
# frame_r.pack(side = "right")

#label
l_user = tk.Label(window, text = "user: ", font = 12, width = 12, height = 2)
# l_user.pack()
l_user.place(x = 200, y = 200)
l_pass = tk.Label(window, text="pass_word: ", font=12, width=12, height=2)
# l_pass.pack()
l_pass.place(x = 200, y = 250)
l_pro = tk.Label(window, text="problem: ", font=12, width=12, height=2)
# l_pro.pack()
l_pro.place(x = 200, y = 300)
l_file = tk.Label(window, text="file: ", font=12, width=12, height=2)
# l_file.pack()
l_file.place(x = 200, y = 350)

#entry
user_var = tk.StringVar()
pd_var = tk.StringVar()
e_use = tk.Entry(window, font=12, text = user_var)
e_pass = tk.Entry(window, show="*", font=12, text = pd_var)
e_pro = tk.Entry(window, font=12)
e_file = tk.Entry(window, font=12)
e_use.place(x = 350, y = 210)
e_pass.place(x = 350, y = 260)
e_pro.place(x = 350, y = 310)
e_file.place(x = 350, y = 360)

#button
def submit():
    sta_list = ui_control.Submit(e_use, e_pass, e_pro, e_file)
    # print(sta_list)
    # print(type(sta_list))
    ui_control.show(sta_list)

def sava():
    ui_control.Save(e_use, e_pass)


b = tk.Button(window, text="Submit", command=submit)
b_save = tk.Button(window, text = 'Remember me', command = sava)
b_save.place(x = 275, y = 400)
b.place(x = 415, y = 400)

menu.creat_menu(window, user_var, pd_var)

now_lan = tk.StringVar()
init_lan(now_lan)
# now_lan.set("Lan")

lan_b = tk.Button(window, text= now_lan.get(),command=lambda : change_lan(now_lan, lan_b))
lan_b.place(x=375, y = 400)

window.mainloop()
