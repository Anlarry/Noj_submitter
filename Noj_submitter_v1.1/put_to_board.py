import win32clipboard as w
import win32con

#获取剪切板内容


def gettext():
    w.OpenClipboard()
    t = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return t

#写入剪切板内容


def settext(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()
