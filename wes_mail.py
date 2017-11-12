'''
Created on Sep 17, 2017

@author: wesle
'''

import tkinter, datetime, re
from tkinter import Button, Label

from sent_mail import Sent_MessageInfo, Forwardpopup



DEFAULT_FONT = ('Arial Black', 12)

#MAIN DRIVER

class WesMailApplication:
    def __init__(self):
        '''create a login page?'''
        self.history = {}
        self._root_window = tkinter.Tk()
        
#         self._root_window.
#         
#         
        login_button = Button(master = self._root_window, text = "Login",font = DEFAULT_FONT, bg = '#3498DB',
                                     command = self.on_login, default = tkinter.DISABLED )
#          state = DISABLED
        login_button.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tkinter.E+tkinter.W)
         
        email_label = Label(master = self._root_window, text = "Email",font = DEFAULT_FONT, bg = 'white')
         
        email_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.N)
        
        self.email_entry = tkinter.Entry(master = self._root_window,font = DEFAULT_FONT)
         
        self.email_entry.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.N)
        
        password_label = Label(master = self._root_window, text = "Password",font = DEFAULT_FONT, bg = 'white')
         
        password_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.N)
        
        self.password_entry = tkinter.Entry(master = self._root_window,font = DEFAULT_FONT)
         
        self.password_entry.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.N)
        
        
        self.password_entry.bind('<Return>', self.login)
        
#         login button diable
        
        
    def run(self):
        self._root_window.mainloop()
        

    def on_login(self):
        if self.check_login():
            self._root_window.destroy()
            email = EmailApplication()
            email.start()
        
        
    def login(self, event):
        if self.check_login():
            self._root_window.destroy()
            email = EmailApplication()
            email.start()
        
    
    def check_login(self):
        
#         print('test:', self.email_entry.get())
        
        if self.email_entry.get() =='':
            missing_label = Label(master = self._root_window, text = "Please enter in email",font = DEFAULT_FONT, fg = 'red') 
            missing_label.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.S+tkinter.E+tkinter.W) 
            return
                
        if self.password_entry.get() == '':
            missing_label = Label(master = self._root_window, text = "Please enter in password",font = DEFAULT_FONT, fg = 'red') 
            missing_label.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.S+tkinter.E+tkinter.W)  
            return
            
        correct_format = r'^.*@\w*(.com|.org|.edu)$'
        
        check = re.match(correct_format, self.email_entry.get())
        
        if check == None:
            invalid_label = Label(master = self._root_window, text = "Please enter in valid email",font = DEFAULT_FONT, fg = 'red') 
            invalid_label.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.S+tkinter.E+tkinter.W)
            return False
        
        return True

class EmailApplication:
    
    def __init__(self):
        self._root_window = tkinter.Tk()
        self.recents = {}
        self.data_base ={} #stores all the sent messages data
        self.count = 0
        
        self.to = ''
        
        inbox_label = Label(master = self._root_window, text = "Inbox",font = DEFAULT_FONT)
        
        inbox_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.N)
        
        compose_button = Button(master = self._root_window, text = 'Compose', font = DEFAULT_FONT, bg ='green',
                                         command = self._on_compose)
        
        compose_button.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.S+tkinter.E+tkinter.W)
        
        sent_button = Button(master = self._root_window, text = 'Sent', font = DEFAULT_FONT, bg ='green',
                                         command = self._on_sent)
        
        sent_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.S+tkinter.E+tkinter.W)
        
        log_out_button = Button(master = self._root_window, text = 'Logout', font = DEFAULT_FONT, bg ='green',
                                         command = self._on_logout)
        
        log_out_button.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.S+tkinter.E+tkinter.W)
        
        
        self._confirmation_text = tkinter.StringVar()
        self._confirmation_text.set('')
        
        confirmation_label = Label(master = self._root_window, textvariable = self._confirmation_text, font = DEFAULT_FONT)
        
        confirmation_label.grid(row = 3, column = 0, padx = 10, pady = 10,
                            sticky = tkinter.N)
        
        self._root_window.rowconfigure(0, weight =1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        
        compose_button.bind('<Enter>', self.entered_compose)
#         compose_button.bind('<Leave>', self.left_compose)
    
        
    def start(self) -> None:
        self._root_window.mainloop()
        
#COMPOSE BUTTON
        
    def entered_compose(self,event):
        '''I cannot control where the pop up appears and sometimes it appears infront of the button
        which is inconvient'''
        pass
#         print('display recent')
#         self.recent = Recent_Reciepients()
        
    def left_compose(self, event):
        self.recent.exit()
#         
    def _on_compose(self) -> None:
        
        message = MessageInfo()
#         enter in the history to this one
#         message.recents_message = self.history
        message.to_graphic()
        message.show()
        
#         if message.was_sent_clicked():
#             self.to = message.get_to()
#             self.cc = message.get_cc()
#             self.recent_to = message.get_self_recent_message()
#             self._confirmation_text.set("sent") 
#             
#             self.recents['person1'] = self.to
#             
        if message.was_sent_clicked():
            
            self.count += 1
            
            self.data_base['email'+ str(self.count)] = {'to': message.get_all_info()[0], 'cc': message.get_all_info()[1], 'bcc': message.get_all_info()[2],
                                       'subject': message.get_all_info()[3], 'message' :  message.get_all_info()[4], 'attachments':  message.get_all_info()[5],
                                       'time': message.get_all_info()[6]}
  
        print(self.data_base)
#         print(self.recents)
#         recent = Recent_Reciepients()
#         self.data_base['email1']['to']
#         self.recents['recipient1'] = 
#         recent.recent_email.set(message.get_all_info()[0])
        
#         if count == 2:
#         recent.recent_email2.set(to)

    def _on_sent(self): 
        sent_messages = Sent_MessageInfo()
        sent_messages.database = self.data_base
#        
#         sent_messages.to = self.data_base['email1']['to']
        sent_messages.display() 
        
#          sent_messages.show()
        
#         print(sent_messages.to)
#         message.to_graphic()
#         message.show()

    def _on_logout(self):
        pass
        
class MessageInfo:
    def __init__(self):
        self.count = 0
        self.recent = False
        self.revealed = False
        self._sent_clicked = False
        self.attachment = '' 
        self.recents_message = {}
        self.recipient = tkinter.StringVar()
        self._to = ''
        self._cc = ''
        
        self._messasge_window = tkinter.Toplevel()
        
        title_label = Label(master = self._messasge_window, text = "Email", font = DEFAULT_FONT)
        
        title_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,sticky = tkinter.W)
        
        to_label = Label(master = self._messasge_window, text = 'To:',font = DEFAULT_FONT)
        
        to_label.grid(row = 1, column = 0 ,padx = 10, pady = 10,sticky = tkinter.W) 
        
        #possibly add an 'add recipient' button
            
        self._dropdown_button = Button(master = self._messasge_window, text = 'V', font = DEFAULT_FONT, bg = '#3498DB', 
                                               command = self.reveal_cc_bcc )
        
        self._dropdown_button.grid(row = 1, column = 2, padx = 10, pady = 1,
                                   sticky = tkinter.W +tkinter.E)
        
        subject_label = Label(master = self._messasge_window, text = 'Subject:', font = DEFAULT_FONT)
        
        subject_label.grid(row = 4, column = 0 ,padx = 10, pady = 10, sticky = tkinter.W)
        
        self._subject_entry = tkinter.Entry(master = self._messasge_window, width = 20, font = DEFAULT_FONT)

        self._subject_entry.grid(row = 4, column = 1, padx = 10, pady = 1,
                                 sticky = tkinter.W + tkinter.E)
        
#         This needs to be bigger
#         self._message_entry = tkinter.Entry( master = self._messasge_window, width = 50, font = DEFAULT_FONT)
# 
#         self._message_entry.grid(row = 5, column = 1, columnspan = 3, rowspan = 3, padx = 10, pady = 1,
#                                 sticky = tkinter.W + tkinter.E)
#         
        self._message_text = tkinter.Text( master = self._messasge_window, width = 50, height = 15, font = DEFAULT_FONT)

        self._message_text.grid(row = 5, column = 1, columnspan = 3, rowspan = 1, padx = 10, pady = 1,
                                sticky = tkinter.W + tkinter.E)
#         rowspan is not expanding it
        
#         BUTTONS
        
        button_frame = tkinter.Frame(master = self._messasge_window)
        
        button_frame.grid(row = 8, column = 1, columnspan = 5, padx = 10, pady = 10,
                          sticky = tkinter.E + tkinter.S)
        
        send_button = Button(master = button_frame, text = 'Send', font = DEFAULT_FONT,bg = '#3498DB',
                                     command = self._on_send_button )
 
        send_button.grid(row = 0, column = 0, padx = 5, pady = 5 )
        
        attach_button = Button(master = button_frame, text = 'Attach', font = DEFAULT_FONT,bg = 'white',
                                       command = self._on_attach_button )

        attach_button.grid(row = 0, column = 2, padx = 5, pady = 5 )
        
        bold_button = Button(master = button_frame, text = 'B', font = DEFAULT_FONT, bg = 'white',
                                     command = self._on_bold_button)

        bold_button.grid(row = 0, column = 3, padx = 5, pady = 5 )
        
        italic_button = Button(master = button_frame, text = 'I', font = DEFAULT_FONT, bg = 'white',
                                       command = self._on_send_button)

        italic_button.grid(row = 0, column = 4, padx = 5, pady = 5 )
        
        underline_button = Button(master = button_frame, text = 'U', font = DEFAULT_FONT, bg = 'white',
                                            command = self._on_underline_button)

        underline_button.grid(row = 0, column = 5, padx = 5, pady = 5 )
        
        
        self.font_selection = tkinter.Spinbox(master = button_frame,font = DEFAULT_FONT, width = 10, bg = 'white', 
                                              values = ('Calibri', 'Corbel', 'Verdana'))
        
        self.font_selection.grid(row = 0, column = 6, padx = 5, pady = 5 )
        
        font_size = tkinter.Spinbox(master = button_frame, values = (6,8,10,12),
                                    font = DEFAULT_FONT, width = 8)
        
        font_size.grid(row = 0, column = 7, padx = 5, pady = 5 )
        
        
#         cancel_button = Button(master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
#                                        command = self._on_cancel_button)
#          
                                   
        self._messasge_window.rowconfigure(3,weight = 1,pad = 5)
        
        self._messasge_window.columnconfigure(4, weight =1)
        
        
#        BUTTON BINDINGS
        
        bold_button.bind('<Enter>', self.entered_bold)
        bold_button.bind('<Leave>', self.left_bold)
        underline_button.bind('<Enter>', self.entered_underline)
        underline_button.bind('<Leave>', self.left_underline)
        
    def to_graphic(self):
        if self.recent == False:
        
            self._to_entry = tkinter.Entry(master = self._messasge_window, width = 20, font = DEFAULT_FONT )
            
#             idk if i can preset text in an 
#         text = 'w@gmai.com' can i set the entry widget?
            self._to_entry.grid(row = 1, column = 1, padx = 10, pady = 1,
                                sticky = tkinter.W +tkinter.E)
            
        if self.recent == True:
            self._to_label = Label(master = self._messasge_window, font = DEFAULT_FONT, textvariable = self.recipient, bg = 'white')
#
            self._to_label.grid(row = 1, column = 1, padx = 10, pady = 1,
                                sticky = tkinter.W +tkinter.E)
    
    def show(self) -> None:
        self._messasge_window.grab_set()
        self._messasge_window.wait_window()
#         
    def was_sent_clicked(self)-> bool:
        return self._sent_clicked
    
# GET FUNCTIONS
    
    def get_all_info(self) -> str:
        
#         try 
#         '''used to put info into the data_base'''
#             return self._to, self._cc, self._bcc, self.subject, self.message, self.attachment, self.data_time
#         
#         except: 
        return self._to, self._cc, self._bcc, self.subject, self.message, self.attachment, self.data_time
            
    
    
    def get_to(self):
        return self._to
     
    def get_cc(self) -> str:
        return self._cc
    
    def get_self_recent_message(self) -> dict:
        return self.recents_message
    
# BUTTON COMMANDSs
    
    def reveal_cc_bcc(self):
#         toggle

        if self.revealed == False:
        
        #if true we will collect the data
#         print('reveal')
            self.cc_label = Label(master = self._messasge_window, text = 'CC:', bg = 'white', font = DEFAULT_FONT)
            #state
            
            self.cc_label.grid(row = 2, column = 0 ,padx = 10, pady = 10, sticky = tkinter.W)
            
            self._cc_entry = tkinter.Entry(master = self._messasge_window, width = 20, font = DEFAULT_FONT,bg =  'white')
    
            self._cc_entry.grid(row = 2, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)
            
            self._bcc_label = Label(master = self._messasge_window, text = 'BCC:', bg = 'white',
                                      font = DEFAULT_FONT)
            
            self._bcc_label.grid(row = 3, column = 0 ,padx = 10, pady = 10,sticky = tkinter.W)
            
            self._bcc_entry = tkinter.Entry(master = self._messasge_window, width = 20, font = DEFAULT_FONT)
    
            self._bcc_entry.grid(row = 3, column = 1, padx = 10, pady = 1,sticky = tkinter.W + tkinter.E)
            
            self.revealed = True
            return
         
        self.cc_label.destroy()
        self._cc_entry.destroy()
        
        self._bcc_label.destroy()
        self._bcc_entry.destroy()
        self.revealed = False
        
    def _on_send_button(self) -> None:
        global DEFAULT_FONT 
        
        self._sent_clicked = True
        
        if self._to_entry.get() == '':
            
            error_label = Label(master = self._messasge_window, text = 'Error: Enter an Email', bg = 'white', font = DEFAULT_FONT, fg = 'red')
        
            error_label.grid(row = 0, column = 1 ,padx = 10, pady = 10, sticky = tkinter.W)
            
            return
            
        self._to = self._to_entry.get()
            
        self.count += 1
        self.data = datetime.datetime.today()
        self.data_time = str(self.data)[11:16]
#         print(self.data_time)
        #set the time stamp 
        
        if not self.recent:
            #should i use the databas here?
            self.recents_message[self.count] = self._to_entry.get()
            
    
        if self.revealed:
            self._cc = self._cc_entry.get()
            self._bcc = self._bcc_entry.get()
            
        else:
            self._cc = ''
            self._bcc = ''
            
        self.subject = self._subject_entry.get()
        self.message = self._message_text.get("1.0", "end-1c")
            
        DEFAULT_FONT = self.font_selection.get()
        
        self._messasge_window.destroy()
        
#         test = self._to_entry.get()
#         the get can only be used once
        recent = Recent_Reciepients()
        
#         is this working
#         i may change things to the database
        if self.count > 1:
            recent.recent_email.set(self.recents_message[self.count-1])
            recent.recent_email2.set(self.recents_message[self.count])
            
        else:
            recent.recent_email.set(self.recents_message[self.count])
            
        
    def _on_attach_button(self) -> None:
        self._on_attach = True
        
        attachwin = AttachWindow()
        attachwin.show()
#         self.attachment reset
        self.attachment = attachwin.attached_files[0]
        
        attachment_button1 = Button(self._messasge_window, text = self.attachment, font = DEFAULT_FONT, bg = 'white',
                                            command = self._show_attachment1)

        attachment_button1.grid(row = 7, column = 1, padx = 5, pady = 5 )
    
        
#     BOLD BUTTON     
    def entered_bold(self, event):

        self.bpop = Boldpopup()
#         self.bpop.show()
        
    def left_bold(self, event):
        self.bpop.exit()
#         print('left')
    
    def _on_bold_button(self) -> None:
        self._on_bold = True
        
#     UNDERLINE BUTTON 

    def entered_underline(self, event):
#         print('entered')
        self.und = Underlinepopup()
#         self.bpop.show()
        
    def left_underline(self, event):
        self.und.exit()
#         print('left')
    
    def _on_underline_button(self) -> None:
        self._on_underline = True

    
    def _show_attachment1(self):
        
        count = 0
        
        self.attachment1_win =  tkinter.Toplevel()
        
#         print(self.attachment)
        for line in open(self.attachment, 'r'):
            
#             print(line)
            
            words = Label(self.attachment1_win, text = line, bg = 'white')
            words.grid(row = count, column = 0, sticky = tkinter.W + tkinter.E)
            count += 1
        

class Underlinepopup:
    
    def __init__(self):
        self._root_window = tkinter.Toplevel()
        
        underline_label = Label(master = self._root_window, text = "Underline", font = DEFAULT_FONT, bg =  'white')
        
        underline_label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tkinter.W)

    def exit(self):
        self._root_window.destroy()
    

class Boldpopup:
    
    def __init__(self):
        self._root_window = tkinter.Toplevel()
        
        bold_label = Label(master = self._root_window, text = "Bold",font = DEFAULT_FONT, bg =  'white')
        
        bold_label.grid(row = 0, column = 0, padx = 10, pady = 10,
                       sticky = tkinter.W)
#     
    def exit(self):
        self._root_window.destroy()
        
                
class Recent_Reciepients:
    
    def __init__(self):
        self._root_window = tkinter.Toplevel()
        
        self.recent_email = tkinter.StringVar()
        self.recent_email.set('email1')
        
        self.recent_email2 = tkinter.StringVar()
        self.recent_email2.set('email2')
        
        recent1_button = Button(master = self._root_window, textvariable = self.recent_email, font = DEFAULT_FONT, bg = '#AF7AC5',
                                        command = self._choose_recent1 )
        
        recent1_button.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        
        recent2_button = Button(master = self._root_window, textvariable = self.recent_email2,font = DEFAULT_FONT, bg = '#AF7AC5',
                                        command = self._choose_recent1 )
        
        recent2_button.grid(row = 1, column = 0, padx = 10, pady = 10,
                            sticky = tkinter.W)
        
        
    def exit(self):
            self._root_window.destroy()
            
    def _choose_recent1(self):
#             print('chosen')
            message_to_recent = MessageInfo()
            message_to_recent.recent = True
            message_to_recent.to_graphic()
            message_to_recent.recipient.set(self.recent_email.get())
#             message_to_recent.show()
            
    def _choose_recent2(self):
#             print('chosen')
            message_to_recent = MessageInfo()
            message_to_recent.show()
            message_to_recent.to_graphic()
            message_to_recent.recipient.set(self.recent_email2.get())
#             message_to_recent.show()
            
        
class AttachWindow:
    def __init__(self):
        
        self.attached_files = []
        #use the len of this list 
        
        self._attach_window = tkinter.Toplevel()
        
        select_label = Label(master = self._attach_window, text = "Select File", font = DEFAULT_FONT, bg = 'white')
        
        select_label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        
        self.select_file_entry = tkinter.Entry(self._attach_window, width = 30)
        
        self.select_file_entry.grid (row = 0 , column = 1)
        
        recent1_button = Button(master = self._attach_window, text = 'Select', font = DEFAULT_FONT, bg = '#AF7AC5',
                                        command = self._on_select )
        
        recent1_button.grid(row = 0, column = 2, padx = 10, pady = 10,sticky = tkinter.W)
        
        self.select_file_entry.bind('<Return>', self._find_file)
        
    def _find_file(self, event) -> None:
        '''may add file path'''
        file = self.select_file_entry.get()
        
        try:
            file_path = open(file , 'r')
            
            self.attached_files.append(file)
            accepted_label = Label(self._attach_window, text ='Attachment has been added', bg = 'white')
            accepted_label.grid(row = 2, column = 0, sticky = tkinter.W+tkinter.E)
            
            #self.attached_files go up to the message windown
#                 lines_in_file = count_lines_in_file(file_path)
#                 print('{} line(s) in {}'.format(lines_in_file, file_path))
        except OSError:
            fail_label = Label(self._attach_window, text ='Failed to open the file successfully', fg = 'red', bg = 'white')
            fail_label.grid(row = 2, column = 0, sticky = tkinter.W+tkinter.E)
            raise Exception
        except ValueError:
            fail_label2 = Label(self._attach_window, text = 'Failed to read from the file successfully; it is not a text file')
            fail_label2.grid(row = 2, column = 0, sticky = tkinter.W+tkinter.E)    
        
    def _on_select(self) -> None:
        '''may add file path'''
        file = self.select_file_entry.get()
        
        try:
            file_path = open(file , 'r')
            
            self.attached_files.append(file)
            
            accepted_label = Label(self._attach_window, text ='Attachment has been added')
            accepted_label.grid(row = 2, column = 0)
            #self.attached_files go up to the message window
#                 lines_in_file = count_lines_in_file(file_path)
#                 print('{} line(s) in {}'.format(lines_in_file, file_path))
        except OSError:
            fail_label = Label(self._attach_window, text ='Failed to open the file successfully', fg = 'red', bg = 'white')
            fail_label.grid(row = 2, column = 0, sticky = tkinter.W+tkinter.E)
            raise Exception
        except ValueError:
            fail_label2 = Label(self._attach_window, text = 'Failed to read from the file successfully; it is not a text file', bg = 'white')
            fail_label2.grid(row = 2, column = 0, sticky = tkinter.W+tkinter.E)

        
    def show(self) -> None:
#         This is how we turn control over to our dialog box and make that dialog box modal
        self._attach_window.grab_set()
        self._attach_window.wait_window()   
        
        
def generate_label(master, name, ro, col):
    
#     name = name+"label"
#     
    name = Label(master, text = name, font = DEFAULT_FONT)
    name.grid(row = ro, column = col, padx = 5, pady = 5, bg = 'white')
    pass

def generate_button(name, ro, col, command):
    pass
                        
        
if __name__ == '__main__':
        
#     file_path = open(file_path, 'r')
    WesMailApplication().run()
    
#     tkinter.Listbox(relief = 2, fg = 'purple', highlightcolor = 'green', bd = 3)
#     
# bd = border
# cursor = cursor that appears
# font 
# selectbackground = the background color to display selected text 
    
    
# once you hit sent it needs to store the to into a dictionary. Then MessageInfo is terminated and all the info that was in it. Create a get function like
# how the professor did it that got all the info. 
