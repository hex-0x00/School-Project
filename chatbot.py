#Karan Lalwani 
#Class 11 Commerce
Basic Chat Bot Design For School
"""
from tkinter import *
root = Tk()
root.title("School ChatBot By KaranLalwani")


def send():
    send = "Student-->>>  "+ e.get()
    text.insert(END,"\n" + send)
    if (e.get() == 'i am fine and what about you'): 
        text.insert(END, "\n" + 'Bot-->>>      I am also Fine; Thnx For asking and In Which Class You are?')
    elif (e.get() == '11 class'):
        text.insert(END, "\n" + 'Bot-->>>      Great; Your Class Teacher is Mehata Sir and Your Room Number is 6')
    elif (e.get() == "class time"):
        text.insert(END, "\n" + 'Bot-->>>      Your class Time is From 8:00 Am to 2:00 Pm')
    elif(e.get()=='hi'):
       text.insert(END, "\n" + 'Bot-->>>      Hello, How are you?')
    elif(e.get()=='*'):
       text.insert(END, "\n" + 'Bot-->>>      Welcome to the School ChatBot Design by karan \n  \t =>Information: About School Bot \n  \t =>To Start Chat With Bot Say= hi')
    elif(e.get()=='6 class'):
       text.insert(END, "\n" + 'Bot-->>>      Great; Your Class Teacher is Vijay Sir and Your Room Number is 1')
    elif(e.get()=='7 class'):
       text.insert(END, "\n" + 'Bot-->>>      Great; Your Class Teacher is Javed Sir and Your Room Number is 2')
    elif(e.get()=='8 class'):
       text.insert(END, "\n" + 'Bot-->>>      Great; Your Class Teacher is Happy Sir and Your Room Number is 3')
    elif(e.get()=='9 class'):
       text.insert(END, "\n" + 'Bot-->>>      Great; Your Class Teacher is Mahen Sir and Your Room Number is 4')
    elif(e.get()=='10 class'):
       text.insert(END, "\n" + 'Bot-->>>      Great; Your Class Teacher is Lokesh Sir and Your Room Number is 5')
    elif(e.get()=='12 class'):
       text.insert(END, "\n" + 'Bot-->>>      Great; Your Class Teacher is Rahul Sir and Your Room Number is 7')
    elif(e.get()=='subject info'):
       text.insert(END, "\n" + ' \n\t 1.Info \n\t 2.Accounts \n\t 3.Hindi \n\t 4.Englsih \n\t 5.Businees Studies')
    elif(e.get()=='info'):
       text.insert(END, "\n" + 'Bot-->>>      This School ChatBot Was Design By Karan Lalwani')
    elif(e.get()=='school info'):
       text.insert(END, "\n" + 'Bot-->>>      School Name:Govt. Fort Sr. Sec. School, Bikaner \n \t Address:Fort school, station road \n \t State:Rajasthan \n \t City:Bikaner \n \t Pincode:334001 \n \t Country:India \n \t Board: Rajasthan Board \n \t ')
    elif(e.get()=='thnx'):
       text.insert(END, "\n" + "Bot-->>>      Your's Welcome")
    elif(e.get()=='student details'):
       text.insert(END, "\n" + "Bot-->>>       \n\t 1.Rahul \n\t 2.Rohit \n\t 3.Ansh \n\t 4.Hemant \n\t 5.Tanshiq \n\t 6.Shyam \n\t 7.Ali \n\t 8.Jitendra \n\t 9.Kaushik \n\t 10.Kunal \n\t 11.Vansh \n\t 12.Nayan \n\t 13.Rajiv \n\t 14.Aditya \n\t 15.Vishal")
    elif(e.get()=='help'):
       text.insert(END, "\n" + "Bot-->>> 1.info (Who Design ChatBot)\n\t 2.* (Which Information You can Gain) \n\t 3.hi (To Start Bot) \n\t 4.__ class (Information about your Class Teacher and your Romm No.) \n\t 5.class time (What the Shcool opening and closing time)\n\t 6.subject info (Know about your classes Schedule and school teacher)\n\t 7.school info (Contact and Location Information) \n\t 8.student details (Your Class Mates Names) \n\t 9.thnx (For Helping)")

    else:
       text.insert(END, "\n" + 'Bot-->>>      Sorry I didnt get it.  \n \t Types- help (How to Use School Bot)')

text = Text(root,bg='orange')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=85)
send = Button(root,text='Send',bg='gray',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.mainloop()
