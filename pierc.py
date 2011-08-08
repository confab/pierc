#!/usr/bin/env python
#   A simple python irc client

import Tkinter as tk

class IrcWindow(object):
    """Main window."""

    def __init__(self, parent):
        
        self.parent = parent

        # One frame to rule them all!
        self.frm_sauron = tk.Frame(self.parent)
        self.frm_sauron.pack(expand=tk.YES, fill=tk.BOTH)

        # Create frame to deal with server messages.
        self.frm_server = tk.Frame(self.frm_sauron, bg='red') # remove bg color
        self.frm_server.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        # Create frame to deal with client messages.
        self.frm_client = tk.Frame(self.frm_sauron, bg='blue') # remove bg color
        self.frm_client.pack(side=tk.BOTTOM, fill=tk.X)

        # Create message widget to display user names.
        self.msg_user = tk.Message(self.frm_server, bg='tan') # remove bg color
        self.msg_user.pack(side=tk.LEFT, fill=tk.Y)

        # Create message widget to display chat messages.
        self.msg_chat = tk.Message(self.frm_server, bg='cyan') # remove bg color
        self.msg_chat.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

        # Create text widget for chat entry.
        self.txt_entry = tk.Text(self.frm_client, height=1,
                                 bg='purple') # remove bg color
        self.txt_entry.pack(side=tk.BOTTOM, fill=tk.X)

class ServerWindow(object):
    """Server window."""

    def __init__(self, parent):

        self.parent = parent

        # One frame to rull them all!
        self.frm_sauron = tk.Frame(self.parent)
        self.frm_sauron.pack(expand=tk.YES, fill=tk.BOTH)

        # Create server label.
        tk.Label(self.frm_sauron, text='Server').pack(side=tk.TOP, anchor=tk.W)

        # Create server text entry.
        self.txt_server = tk.Text(self.frm_sauron, height=1, width=40)
        self.txt_server.pack(side=tk.TOP, anchor=tk.W)

        # Create port label.
        tk.Label(self.frm_sauron, text='Port').pack(side=tk.TOP, anchor=tk.W)

        # Create port text entry.
        self.txt_server = tk.Text(self.frm_sauron, height=1, width=40)
        self.txt_server.pack(side=tk.TOP, anchor=tk.W)


# Open the server window first.
win_server = tk.Tk()
irc = ServerWindow(win_server)
win_server.mainloop()

# Now open the main window.
root = tk.Tk()
irc = IrcWindow(root)
root.mainloop()
