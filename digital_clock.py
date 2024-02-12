from  tkinter import *
import time


window = Tk()
window.title('Digital Clock')
window.geometry("600x300")


def myTime():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm= time.strftime('%p')
    day = time.strftime('%A')
    zone = time.strftime('%Z')
    myText= hour+':'+minute+ ':'+second +" " +am_pm
    myText2 = day + ', ' + zone
    my_label.config(text=myText)
    my_label2.config(text=myText2)
    my_label.after(1000,myTime)

my_label = Label(window, text='',font=('Arial,120'),fg='black',bg='yellow', )
my_label.pack( padx=100 ,pady=20)
my_label2 = Label(window, text='',font=('Arial,24'),fg='black',bg='yellow', )
my_label2.pack(padx=100, pady=20)
myTime()
window.mainloop()