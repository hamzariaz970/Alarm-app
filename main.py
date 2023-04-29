import tkinter
from tkinter import *
import tkinter.font as font
import customtkinter  # <- import the CustomTkinter module
import time
import sys
import pytz
import math
from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import tkinter as tk
from datetime import datetime
import os
import turtle


global running,main
global counter
global task_list
task_list = []
root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("1280x720")
root_tk.title("Alarm++")


def button_function():
    print("button pressed")


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

def worldClock():
    from datetime import datetime
    import pytz
    import time
    root = Toplevel(root_tk)
    root.title("World Clock")
    root.geometry("1280x720")
    boundary = 95

    def times():
        home = pytz.timezone('Asia/Karachi')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        clock.config(text=current_time)
        name.config(text="Karachi")

        home1 = pytz.timezone('America/Los_Angeles')
        local_time1 = datetime.now(home1)
        current_time1 = local_time1.strftime("%H:%M:%S")
        clock1.config(text=current_time1)
        name1.config(text="Los Angeles")

        home2 = pytz.timezone('Australia/Melbourne')
        local_time2 = datetime.now(home2)
        current_time2 = local_time2.strftime("%H:%M:%S")
        clock2.config(text=current_time2)
        name2.config(text="Melbourne")

        home3 = pytz.timezone('Europe/London')
        local_time3 = datetime.now(home3)
        current_time3 = local_time3.strftime("%H:%M:%S")
        clock3.config(text=current_time3)
        name3.config(text="London")

        home4 = pytz.timezone('Asia/Dhaka')
        local_time4 = datetime.now(home4)
        current_time4 = local_time4.strftime("%H:%M:%S")
        clock4.config(text=current_time4)
        name4.config(text="Dhaka")

        home5 = pytz.timezone('America/New_York')
        local_time5 = datetime.now(home5)
        current_time5 = local_time5.strftime("%H:%M:%S")
        clock5.config(text=current_time5)
        name5.config(text="New York")

        clock.after(500, times)

    clock = Label(root, fg='#270640', font=("montserrat", 25, "bold"))
    clock.place(x=45 + boundary, y=21 + 40 + boundary)
    name = Label(root, fg='#058D20', font=("montserrat", 17, "bold"))
    name.place(x=53 + boundary, y=40 + boundary)
    nota = Label(root, text="Hours : Minutes : Seconds",
                 font=("montserrat", 7, "bold"))
    nota.place(x=45 + boundary, y=66 + 40 + boundary)

    clock1 = Label(root, fg='#270640', font=("montserrat", 25, "bold"))
    clock1.place(x=40 + 5.3 * boundary, y=21 + 40 + boundary)
    name1 = Label(root, fg='#1A29C6', font=("montserrat", 17, "bold"))
    name1.place(x=33 + 5.3 * boundary, y=40 + boundary)
    nota1 = Label(root, text="Hours : Minutes : Seconds",
                  font=("montserrat", 7, "bold"))
    nota1.place(x=45 + 5.3 * boundary, y=66 + 40 + boundary)

    clock2 = Label(root, fg='#270640', font=("montserrat", 25, "bold"))
    clock2.place(x=43 + 9.5 * boundary, y=21 + 40 + boundary)
    name2 = Label(root, fg='#B9B911', font=("montserrat", 17, "bold"))
    name2.place(x=39 + 9.5 * boundary, y=40 + boundary)
    nota2 = Label(root, text="Hours : Minutes : Seconds",
                  font=("montserrat", 7, "bold"))
    nota2.place(x=45 + 9.5 * boundary, y=66 + 40 + boundary)

    clock3 = Label(root, fg='#270640', font=("montserrat", 25, "bold"))
    clock3.place(x=42 + boundary, y=21 + 40 + 4 * boundary)
    name3 = Label(root, fg='#CC6912', font=("montserrat", 17, "bold"))
    name3.place(x=58 + boundary, y=40 + 4 * boundary)
    nota3 = Label(root, text="Hours : Minutes : Seconds",
                  font=("montserrat", 7, "bold"))
    nota3.place(x=45 + boundary, y=66 + 40 + 4 * boundary)

    clock4 = Label(root, fg='#270640', font=("montserrat", 25, "bold"))
    clock4.place(x=42 + 5.3 * boundary, y=21 + 40 + 4 * boundary)
    name4 = Label(root, fg='#BD1712', font=("montserrat", 17, "bold"))
    name4.place(x=65 + 5.3 * boundary, y=40 + 4 * boundary)
    nota4 = Label(root, text="Hours : Minutes : Seconds",
                  font=("montserrat", 7, "bold"))
    nota4.place(x=45 + 5.3 * boundary, y=66 + 40 + 4 * boundary)

    clock5 = Label(root, fg='#270640', font=("montserrat", 25, "bold"))
    clock5.place(x=37 + 9.5 * boundary, y=21 + 40 + 4 * boundary)
    name5 = Label(root, fg='#058D20', font=("montserrat", 17, "bold"))
    name5.place(x=45 + 9.5 * boundary, y=40 + 4 * boundary)
    nota5 = Label(root, text="Hours : Minutes : Seconds",
                  font=("montserrat", 7, "bold"))
    nota5.place(x=45 + 9.5 * boundary, y=66 + 40 + 4 * boundary)

    times()

    root.mainloop()
    
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

def timer():
    distance = 10
    #Create an instance of tkinter frame
    win = Toplevel(root_tk)
    win.geometry('600x600')
    win.resizable(False,False)
    #Configure the background
    win.config(bg='#585759')
    #Create Entry Widgets for HH MM SS
    sec = StringVar()
    Entry(win, textvariable=sec, width = 2, font = 'Bahnschrift 33').place(x=220-10, y=120+130+distance)
    sec.set('00')
    mins= StringVar()
    Entry(win, textvariable = mins, width =2, font = 'Bahnschrift 33').place(x=180-10+10*distance, y=120+130+distance)
    mins.set('00')
    hrs= StringVar()
    Entry(win, textvariable = hrs, width =2, font = 'Bahnschrift 33').place(x=142-10+20*distance, y=120+130+distance)
    hrs.set('00')
    hour=Label(win, text = "SEC  :  MIN  :  HOUR", font = ' 8', bg='#585759').place(x=195,y=125+150+5*distance)


    icon=PhotoImage(file="ico.png")
    image_label=Label(win, image=icon, bg='#585759')
    image_label.place(x=185,y=0)

    #Define the function for the timer
    def countdowntimer():
        times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
        while times > -1:
            minute,second = (times // 60 , times % 60)
            hour =0
            if minute > 60:
                hour , minute = (minute // 60 , minute % 60)
            sec.set(second)
            mins.set(minute)
            hrs.set(hour)
            #Update the time
            win.update()
            time.sleep(1)
            if(times == 0):
                sec.set('00')
                mins.set('00')
                hrs.set('00')
                return
            times -= 1

    Label(win, font =('Bahnschrift bold',50), text = 'TIMER', bg='#585759').place(x=200,y=120+30)
    Button(win, text='START', bd ='2', bg = '#958F8F',font =('Bahnschrift',27), command = countdowntimer).place(x=230, y=120+220+(2*distance))
    win.mainloop()

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
def notifier():
    os.system("python notifier.py")
    # t = Toplevel(root_tk)
    # t.title('Notifier')
    # t.geometry("500x300")
    # img = Image.open("notify-label.png")
    # tkimage = ImageTk.PhotoImage(img)


    # # get details
    # def get_details():
    #     get_title = title.get()
    #     get_msg = msg.get()
    #     get_time = time1.get()
    #     # print(get_title,get_msg, tt)

    #     if get_title == "" or get_msg == "" or get_time == "":
    #         messagebox.showerror("Alert", "All fields are required!")
    #     else:
    #         int_time = int(float(get_time))
    #         min_to_sec = int_time * 60
    #         messagebox.showinfo("notifier set", "set notification ?")
    #         t.destroy()
    #         time.sleep(min_to_sec)

    #         notification.notify(title=get_title,
    #                             message=get_msg,
    #                             app_name="Notifier",
    #                             app_icon="ico.ico",
    #                             toast=True,
    #                             timeout=10)


    # img_label = Label(t, image=tkimage).grid()

    # # Label - Title
    # t_label = Label(t, text="Title to Notify", font=("poppins", 10))
    # t_label.place(x=12, y=70)

    # # ENTRY - Title
    # title = Entry(t, width="25", font=("poppins", 13))
    # title.place(x=123, y=70)

    # # Label - Message
    # m_label = Label(t, text="Display Message", font=("poppins", 10))
    # m_label.place(x=12, y=120)

    # # ENTRY - Message
    # msg = Entry(t, width="40", font=("poppins", 13))
    # msg.place(x=123, height=30, y=120)

    # # Label - Time
    # time_label = Label(t, text="Set Time", font=("poppins", 10))
    # time_label.place(x=12, y=175)

    # # ENTRY - Time
    # time1 = Entry(t, width="5", font=("poppins", 13))
    # time1.place(x=123, y=175)

    # # Label - min
    # time_min_label = Label(t, text="min", font=("poppins", 10))
    # time_min_label.place(x=175, y=180)

    # # Button
    # but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
    #             relief="raised",
    #             command=get_details)
    # but.place(x=170, y=230)

    # t.resizable(0, 0)
    # t.mainloop()

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

def to_do_list():
    root = Toplevel(root_tk)
    root.title("To-Do-List")
    root.geometry("1280x720")

    #task_list = []

    def addTask():
        task = task_entry.get()
        task_entry.delete(0, END)

        if task:
            with open("tasklist.txt", "a") as taskfile:
                taskfile.write(f"\n{task}")
            
            task_list.append(task)
            listbox.insert(END, task)    

    def deleteTask():
        #global task_list
        task = str(listbox.get(ANCHOR))
        if task in task_list:
            task_list.remove(task)
            with open("tasklist.txt", "w") as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")
            listbox.delete(ANCHOR)                   

    def openTaskFile():
        try:
            global task_list
            with open("tasklist.txt", "r") as taskfile:
                tasks = taskfile.readlines()

            for task in tasks:
                if task != '\n':
                    task_list.append(task)
                    listbox.insert(END, task)
        except:
            file = open("tasklist.txt", 'w')
            file.close()




    heading = Label(root, text = "TO-DO LIST", font = 'Helvetica 50 bold', fg = "white", bg = "#3D59AB")
    heading.place(relx = 0.35 , y = 0.30)
    # Main frame for task entry
    frame = customtkinter.CTkFrame(master = root, width = 1220, height = 60, fg_color = "white")
    frame.place(relx = 0.02, rely = 0.2)

    # Field to enter text 
    task = StringVar()
    task_entry = Entry(frame, width = 60, font = 'Helvetica 20', bd = 0, text = "Enter task")
    task_entry.place(relx = 0, rely = 0.3)
    task_entry.focus()

    # ADD task button
    add_task_button = customtkinter.CTkButton(master = frame, text = "ADD", font = ('Helvetica', 30), width = 100, height = 58, fg_color = "#3D59AB", command = addTask)
    add_task_button.place(relx=0.958, rely=0.50, anchor=tkinter.CENTER)

    # listbox
    sub_frame = Frame(root, bd = 3, width = 00, height = 00, bg = "#3D59AB")
    sub_frame.pack(pady = (270, 50))

    listbox = Listbox(sub_frame, font = ('Helvetica', 20), width = 78, height = 10, bg = "#3D59AB", cursor = "hand2", selectbackground = "#5a95ff", fg = "white")
    listbox.pack(side = LEFT, fill = BOTH, padx = 2)
    scrollbar = Scrollbar(sub_frame)
    scrollbar.pack(side = RIGHT, fill = BOTH)

    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)

    # DELETE button
    Delete_icon = PhotoImage(file = "delete.png")
    Button(root, image = Delete_icon, bd = 0, command = deleteTask).pack(side = BOTTOM, pady = 0)

    openTaskFile()

    root.mainloop()




# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------




def runStopwatch():
    os.system("python stopwatch.py")
    # counter = 0
    # running = False


    # def counter_label(label):
    #     def count():
    #         if running:
    #             global counter 
    #             if counter == 0:
    #                 display = 'Ready!'
    #             else:
    #                 tt = datetime.utcfromtimestamp(counter)
    #                 string = tt.strftime('%H:%M:%S')
    #                 display = string
        
    #             label['text'] = display
    #             label.after(1000, count)
    #             counter += 1 
    #     count()
        
    # def Start(label):
    #     global running
    #     running = True
    #     counter_label(label)
    #     start['state'] = 'disabled'
    #     stop['state'] = 'normal'
    #     reset['state'] = 'normal'
        
    # def Stop():
    #     global running
    #     start['state'] = 'normal'
    #     stop['state'] = 'disabled'
    #     reset['state'] = 'normal'
    #     running = False
        

    # def Reset(label):
    #     global counter
    #     counter = 0
    #     if not running:
    #         reset['state'] = 'disabled'
    #         label['text'] = '00:00:00'
    #     else:
    #         label['text'] = '00:00:00'


    # root = Toplevel(root_tk)
    # root.title("Stopwatch")

    # root.minsize(width=250, height=70)
    # label = Label(root, text='Ready!', fg='black', font='Verdana 30 bold')
    # label.pack()
    # f = Frame(root)
    # start = Button(f, text='Start', width=6, command=lambda: Start(label))
    # stop = Button(f, text='Stop', width=6, state='disabled', command=Stop)
    # reset = Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
    # f.pack(anchor='center', pady=5)
    # start.pack(side='left')
    # stop.pack(side='left')
    # reset.pack(side='left')
    # root.mainloop()

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

def alarm():
    os.system("python alarmclock.py")



def analogClock():
    os.system("python analog_clock.py")

def Exit():
    quit()


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# Heading of program
label = customtkinter.CTkLabel(master=root_tk, text="ALARM++", width=120, height=250,
                               corner_radius=8, text_color="DodgerBlue3", font=('Calibri italic', 65))
label.place(relx=0.55, rely=0.2, anchor=tkinter.CENTER)


# Side frame
frame = customtkinter.CTkFrame(master=root_tk,
                               width=540,
                               height=1450,
                               corner_radius=10,
                               fg_color="light grey")
# Button to view analog clock
button7 = customtkinter.CTkButton(master = root_tk, corner_radius=12, command = analogClock,
                                  width=120, height=50, text="View Analog Clock", font=('Helvetica', 20))
button7.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

#BUtton to exit program

button8 = customtkinter.CTkButton(master = root_tk, corner_radius=12, command = Exit,
                                  width=120, height=50, text="Exit", font=('Helvetica', 20))
button8.place(relx=0.1, rely=0.85, anchor=tkinter.CENTER)

frame.place(relx=0.0, rely=0, anchor=tkinter.CENTER)




# StopWatch button
button1 = customtkinter.CTkButton(master=root_tk, corner_radius=12, command = runStopwatch,
                                  width=120, height=50, text="Stopwatch", font=('Helvetica', 30))
button1.place(relx=0.35, rely=0.45, anchor=tkinter.CENTER)

# Timer button
button2 = customtkinter.CTkButton(master=root_tk, corner_radius=12, command = timer,
                                  width=200, height=50, text="Timer", font=('Helvetica', 30))
button2.place(relx=0.55, rely=0.45, anchor=tkinter.CENTER)


# World Clock button
button3 = customtkinter.CTkButton(master=root_tk, corner_radius=12, command=worldClock,
                                  width=120, height=50, text="World Clock", font=('Helvetica', 30))
button3.place(relx=0.75, rely=0.45, anchor=tkinter.CENTER)


# Reminders button
button4 = customtkinter.CTkButton(master=root_tk, corner_radius=12, command=notifier,
                                  width=120, height=50, text="Reminders", font=('Helvetica', 30))
button4.place(relx=0.35, rely=0.65, anchor=tkinter.CENTER)


button5 = customtkinter.CTkButton(master=root_tk, corner_radius=12, command=alarm,
                                  width=200, height=50, text="Alarm", font=('Helvetica', 30))
button5.place(relx=0.55, rely=0.65, anchor=tkinter.CENTER)

button6 = customtkinter.CTkButton(master=root_tk, corner_radius=12, command=to_do_list,
                                  width=200, height=50, text="To-Do List", font=('Helvetica', 30))
button6.place(relx=0.75, rely=0.65, anchor=tkinter.CENTER)




root_tk.mainloop()
