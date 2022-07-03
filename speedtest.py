from tkinter import *
import speedtest

def checkSpeed():
    sp= speedtest.Speedtest()
    sp.get_servers()
    down = str(round((sp.download()/(10**6)),3)) + " Mbps"
    up= str(round((sp.upload()/(10**6)),3))+ " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)
    
sp=Tk()
sp.title("Internet Speed Test")
sp.geometry("400x700")
sp.config(bg="Blue")

lab = Label(sp , text="Internet Speed Test", font=("Arial Black" , 20,"bold"),bg="white",fg="red")
lab.place(x=50,y=40,height = 50, width=380)
lab = Label(sp , text="Downloading Speed", font=("Arial Black" , 20,"bold"),bg="white",fg="red")
lab.place(x=50,y=130,height=50, width=380)
lab_down = Label(sp , text="00", font=("Arial Black" , 20,"bold"),bg="white",fg="red")
lab_down.place(x=50,y=200,height=50, width=380)
lab = Label(sp , text="Upload Speed", font=("Arial Black" , 20,"bold"),bg="white",fg="red")
lab.place(x=50,y=290,height=50, width=380)
lab_up = Label(sp , text="00", font=("Arial Black" , 20,"bold"),bg="white",fg="red")
lab_up.place(x=50,y=360,height=50, width=380)

button = Button(sp,text="CHECK INTERNET SPEED" , font=("Arial Black" , 20,"bold"),relief=RAISED,bg="Green",fg="Yellow",command=checkSpeed)
button.place(x=50,y=460,height=50, width=380)

sp.mainloop()
