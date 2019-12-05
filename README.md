# sh_messagebox
Module sh_messagebox defines **sh_messagebox** as alternative to ***tk.messagebox*** for Python programs.

Extentions vs tk.messagebox:
* No need to preliminary create/destroy root window for non-GUI apps, 
  just set parameter *hasmaster* to 0.
* sh_messageboxe is able to auto-close after specified delay (msec)
* If calling application provides its icon, the icon will be shown in the
  title of sh_messagebox, otherwise internal icon will be used.