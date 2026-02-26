from tkinter import *
import time
# import keyboard


def set_labels():
    global hour,minutes,seconds
    
    container = Frame(master=window,bg='red')

    
    text = Label(master=container,bg='black',fg='#00ff00',height=1,width=200,font=('Arial',50,'bold'),padx='23px',pady='23px',text="TIME IS RUNNING OUT")
    hour = Label(master=container,bg='black',fg='white',height=1,width=200,font=('Arial',50,'bold'),padx='23px',pady='23px')
    minutes = Label(master=container,bg='#00ff00',fg='black',height=2,width=200,font=('Arial',50,'bold'),padx='23px',pady='50px')
    seconds = Label(master=container,bg='black',fg='white',height=1,width=200,font=('Arial',50,'bold'),padx='23px',pady='23px')
    container.pack()
    text.pack()
    hour.pack()
    minutes.pack()
    seconds.pack()

def change_label():
    global hour,minutes,seconds

    hour.configure(text=f"{time.ctime(time.time())[11:13]}")
    minutes.configure(text=f"{time.ctime(time.time())[14:16]}")
    seconds.configure(text=f"{time.ctime(time.time())[17:19]}")
    window.after(1000, change_label) # every 1000 milliseconds...

window = Tk()
window.config(bg='black')
window.attributes('-fullscreen',True)
set_labels()
change_label()

# key = 'f4'
# keyboard.block_key(key)
# keyboard.add_hotkey()
window.mainloop()

# while True:
#     time.sleep(1)
#     print(f"{time.ctime(time.time())[11:13]} : {time.ctime(time.time())[14:16]} : {time.ctime(time.time())[17:19]}")


