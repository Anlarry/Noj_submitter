import requests
from  bs4 import BeautifulSoup
import tkinter as tk

def show_data(sid, test):
    # url = "http://noj.cn/?a=w&sid=560750&test=0"
    url = "http://noj.cn/?a=w&sid="+sid+"&test="+test
    html = requests.get(url).text
    bs = BeautifulSoup(html, "lxml")
    s = bs.find("body").get_text()
    data = get_data(s)

    window = tk.Tk()
    window.geometry("400x400")
    fream1 = tk.Frame(window)
    fream2 = tk.Frame(window)
    fream1.pack()
    fream2.pack()
    tk.Label(fream1, text="Input").pack()
    input_text = tk.Text(fream1, width = 30, height=12)
    input_text.insert(1.0, data[2])
    input_text.pack()

    fream2_l = tk.Frame(fream2)
    fream2_r = tk.Frame(fream2)
    fream2_l.pack(side = "left")
    fream2_r.pack(side = "right")

    tk.Label(fream2_l, text="StandardOutput").pack()
    std_text = tk.Text(fream2_l, width=25, height=12)
    std_text.insert(1.0, data[1])
    std_text.pack()

    tk.Label(fream2_r, text="YourOutput").pack()
    out_text = tk.Text(fream2_r, width=25, height=12)
    out_text.insert(1.0, data[0])
    out_text.pack()
    window.mainloop()

def get_data(s):
    i, j = 0, len(s)-1
    while i < j and s[i] != '[':
        i+=1
    while i < j and s[j] != ']':
        j-=1
    ds = ""
    k = i+1
    while k < j:
        ds += s[k]
        k+=1
    data = ds.split(',')
    data = data[:3]
    data_list = [] 
    for x in data:
        ts = ""
        i, j = 0, len(x)-1
        while i < j and x[i] != "'": i+=1
        while i < j and x[j] != "'": j-=1
        k = i + 1
        while k < j : 
            ts += x[k]
            k+=1
        data_list.append(ts)
    return data_list

def get_data_info(url):
    html = requests.get(url).text
    bs = BeautifulSoup(html, "lxml")
    tag = bs.find_all("a", {"class":"vd"})
    info = []
    for each in tag:
        s = each.attrs["href"]
        sid = s[-9:-3]
        test = s[-2:-1]
        info.append([sid, test])    
    return info

# show_data("560750", "0")
