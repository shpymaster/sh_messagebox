"""
module: sh_messagebox
version: 2.0.20191015

This module defines sh messageboxes as alternative to tk.messagebox
Extentions vs tk.messagebox:
- No need to preliminary create/destroy root window for non-GUI apps, 
  just set hasmaster to 0.
- sh_messageboxe is able to make an automatic decision 
  and to close after specified delay (msec)
- If calling application provides its icon, it will be shown in the
  title of sh messagebox
"""

import sys
import os
import winsound
import tkinter as tk
import importlib.util

SH_MESSAGE_ERROR = 1
SH_MESSAGE_INFO = 2
SH_MESSAGE_WARNING = 3
SH_MESSAGE_QUESTION = 4

def shShowMessage(hasmaster, title, messagetext, messagetype, delay=0, appIcon=None):
    """
    Shows messagebox with button OK.
    Message types: Error, Info, Warning.
    If delay >0, messagebox will auto-close after delay_milliseconds.
    If appIcon file is provided, this icon will be shown in the messagebox title.
    No need to preliminary create/destroy root window for non-GUI apps, just set hasmaster to 0.
    """

    icon_names = [None, "error.png", "info.png", "warning.png", "question.png"]
    icon_subdir = "\\images\\"

    root = tk.Toplevel() if hasmaster else tk.Tk()
    root.title(title)
    root.minsize(width=300, height=50)

    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))

    def onReturn(Event):
        root.destroy()

    frameButtons = tk.Frame(root)
    frameButtons.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH)
    lblFake = tk.Label(frameButtons, width=4)
    lblFake.pack(side=tk.RIGHT)
    buttonOK = tk.Button(frameButtons, text="OK", width=10, command=root.destroy)
    buttonOK.pack(side=tk.RIGHT, padx=5, pady=5)

    frameMessage = tk.Frame(root)
    frameMessage.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

    iconfilename = os.path.dirname(__file__) + icon_subdir + icon_names[messagetype]
    imgIcon = tk.PhotoImage(file=iconfilename)
    lblImage = tk.Label(frameMessage, image=imgIcon, compound=tk.CENTER)
    lblImage.pack(side=tk.LEFT, anchor="w", padx=20, pady=20) 
    lblMessage = tk.Label(frameMessage, text=messagetext, justify="left")
    lblMessage.pack(side=tk.LEFT, padx=10, anchor="w", fill=tk.X, expand=tk.YES, )
    
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    if delay: root.after(delay, root.destroy)
    root.bind('<Return>', onReturn)
    root.bind('<Escape>', onReturn)

    if appIcon: 
        root.iconbitmap(appIcon)
    else:
        root.iconbitmap(iconfilename[:-3] + "ico")

    #--- modal
    root.focus_set()
    root.grab_set()
    root.wait_window()


if __name__ == "__main__":
    #self-test
    shShowMessage(0, "ERROR Title", "My message is not so long as you could think", SH_MESSAGE_ERROR, 0000)
    shShowMessage(0, "INFO Title", "My message is not so long as you could think", SH_MESSAGE_INFO, 0000)
    shShowMessage(0, "WARNING Title", "My message is not so long as you could think", SH_MESSAGE_WARNING, 0000)
    shShowMessage(0, "QUESTION Title + warn", "!!!--- App Icon + \nAuto closing after 5 sec ---!!!", SH_MESSAGE_QUESTION, 5000, "./images/warning.ico")
    shShowMessage(1, "ERROR Title", "Mode NO ROOT", SH_MESSAGE_ERROR, 0000)