#sh_messagebox
Module sh_messagebox defines sh_messagebox as alternative to tk.messagebo for Python programs
Extentions vs tk.messagebox:

- No need to preliminary create/destroy root window for non-GUI apps, 
  just set hasmaster to 0.
- sh_messageboxe is able to make an automatic decision 
  and to close after specified delay (msec)
- If calling application provides its icon, it will be shown in the
  title of sh messagebox, otherwise internal icons will be used.