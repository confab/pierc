#!/usr/bin/env python
#   A simple python irc client

import Tkinter as tk

class IrcWindow(object):
    """Main window."""

    def __init__(self, parent, dict_settings):
        
        self.parent = parent
        self.settings = dict_settings

        # Call the server window.
        self.on_win_server()
        
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

    def on_win_server(self):
        """Server window."""

        # Create toplevel frame.
        win_server = tk.Toplevel()

        # One frame to rull them all!
        frm_sauron = tk.Frame(win_server)
        frm_sauron.pack(expand=tk.YES, fill=tk.BOTH, ipadx=5, ipady=5)

        # Create server label.
        tk.Label(frm_sauron, text='Server').pack(side=tk.TOP, anchor=tk.W)

        # Create server text entry.
        txt_server = tk.Text(frm_sauron, height=1, width=40)
        txt_server.focus_force()
        txt_server.pack(side=tk.TOP, anchor=tk.W)

        # Create port label.
        tk.Label(frm_sauron, text='Port').pack(side=tk.TOP, anchor=tk.W)

        # Create port text entry.
        txt_server = tk.Text(frm_sauron, height=1, width=40)
        txt_server.pack(side=tk.TOP, anchor=tk.W)

        # Create channel label.
        tk.Label(frm_sauron, text='Chan.').pack(side=tk.TOP, anchor=tk.W)

        # Create channel text entry.
        txt_channel = tk.Text(frm_sauron, height=1, width=40)
        txt_channel.pack(side=tk.TOP, anchor=tk.W)

        # Create Cancel button.
        btn_cancel = tk.Button(frm_sauron, text='Cancel', width=8)
        btn_cancel.bind('<Button-1>', lambda _ : win_server.destroy())
        btn_cancel.bind('<Return>', lambda _ : win_server.destroy())
        btn_cancel.pack(side=tk.RIGHT, anchor=tk.E)

        # Create Connect button.
        btn_connect = tk.Button(frm_sauron, text='Connect', width=8)
        btn_connect.bind('<Button-1>', lambda _ : win_server.destroy())
        btn_connect.bind('<Return>', lambda _ : win_server.destroy())
        btn_connect.pack(side=tk.RIGHT, anchor=tk.W)

# Create settings object
dict_settings = {}

# Now open the main window.
root = tk.Tk()
irc = IrcWindow(root, dict_settings)
root.mainloop()
