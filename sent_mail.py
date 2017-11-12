'''
Created on Sep 21, 2017

@author: wesle


'''
print('hello there')
import tkinter

DEFAULT_FONT = ('Arial Black', 12)

class Sent_MessageInfo():
    def __init__(self):
        self.to = ''
        self._sent_window = tkinter.Toplevel()
        self.collapse = False
        print('hi')
        
    def display(self):
        print('dispaly ')
#         self.collapse = False
        
        print(self.database)
            
        title_label = tkinter.Label(master = self._sent_window, text = "Today", font = DEFAULT_FONT, bg ='white')
            
        title_label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        
#         for email in self.database.keys().sort(reverse = True)
#             print(email)
#         is there a more efficent way?
        count = len(list(self.database.keys()))
        data = list(self.database.keys())[::-1]
        
        for email_count in range(count):
            
        
            self.recentemail_button = tkinter.Button(master = self._sent_window, text = 'me                '+ self.database[data[email_count]]['to'], font = DEFAULT_FONT, bg ='white',
                                                     command = self._view_email)
            
            self.recentemail_button.grid(row = email_count+1, column = 0, columnspan = 3, padx = 10, pady = 10,sticky = tkinter.W)
        
            self.delete_button = tkinter.Button(master = self._sent_window, text = 'X', font = DEFAULT_FONT, bg ='white',
                                                command = self._delete_email)
        
            self.delete_button.grid(row = email_count+1, column = 3, padx = 10, pady = 10,sticky = tkinter.W)
        
        
    def _view_email(self):
        
        print(self.collapse)
        
        if not self.collapse:
            self.email_subject = tkinter.Label(master = self._sent_window, text = self.database['email1']['subject'], font = DEFAULT_FONT)
            
            self.email_subject.grid(row = 2, column = 0, pady = 3)
            
            self.message_label = tkinter.Label(master = self._sent_window, text =  self.database['email1']['message'],  font = DEFAULT_FONT, bg ='white')
            self.message_label.grid(row = 3, column = 0)
            
            self.reply_label = tkinter.Label(master = self._sent_window, text = 'Reply ', font = DEFAULT_FONT, bg ='white')
            self.reply_label.grid(row = 4, column = 0)
            
            self.reply_text = tkinter.Text(master = self._sent_window, font = DEFAULT_FONT, bg ='white', height = 10.)
                                            
            self.reply_text.grid(row = 5, column = 1, pady = 3)
            
            self.time_label = tkinter.Label(master = self._sent_window, text = self.database['email1']['time'], font = DEFAULT_FONT, bg ='white')
            self.time_label.grid(row = 1, column = 2)
            
            
            self.forward_button = tkinter.Button(master = self._sent_window, text = '->', font = DEFAULT_FONT, bg ='white',
                                            command = self._forward)
            
            self.forward_button.grid(row =5, column = 2)
            
            self.send_button = tkinter.Button(master = self._sent_window, text = 'Send', font = DEFAULT_FONT, bg ='white',
                                         command = self._send_reply)
            
            self.send_button.grid(row =7, column = 1)
            
            self.forward_button.bind('<Enter>', self.entered_forward)
            self.forward_button.bind('<Leave>', self.left_forward)
            
            
            self.collapse = True
            
            print(self.collapse)
            
            return
        
#         print('destory')
        
        self.email_subject.destroy()
        self.message_label.destroy()
        
        self.reply_label.destroy()
        self.reply_text.destroy()
        
        self.time_label.destroy()
        
        self.forward_button.destroy()
        self.send_button.destroy()
        
        self.collapse = False
        
    def _delete_email(self):
        self.recentemail_button.destroy()
        self.delete_button.destroy()
        
    def _send_reply(self):
        pass
        
    def _reply(self):
        
        pass
        
    def _forward(self):
        pass
    
    def show(self) -> None:
#         This is how we turn control over to our dialog box and make that dialog box modal
        self._sent_window.grab_set()
        self._sent_window.wait_window()
        
    def entered_forward(self,event):
        
        self.forward_win = Forwardpopup()
         
    def left_forward(self, event):
        self.forward_win.exit()
        
        
class Forwardpopup:
    
    def __init__(self):
        self._root_window = tkinter.Toplevel()
        
        bold_label = tkinter.Label(master = self._root_window, text = "Forward",font = DEFAULT_FONT)
        
        bold_label.grid(row = 0, column = 0, padx = 10, pady = 10,
                       sticky = tkinter.W)
#     
    def exit(self):
        self._root_window.destroy()
        
