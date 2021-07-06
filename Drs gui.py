import tkinter
import cv2
import PIL
from tkinter import *
from PIL import Image,ImageTk
import imutils
from functools import partial
import time
import threading


#Width and Height of our root
Width=1280
Height=680

#Main Canvas Width and Height
c_width=800
c_height=450
curx=800
cury=450



#Clock Function
def clock():
    hour=time.strftime("%I")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    am_pm=time.strftime("%p")
    cur=(hour+":"+minute+":"+second+" "+ am_pm)
    label.config(text=cur)
    canvas.after(1000,clock)




#Pending Function
def Pending(char):
    print("Inside Pending")
    img=cv2.imread("Pending.jpg")
    img=imutils.resize(img,width=c_width,height=c_height)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    photo=ImageTk.PhotoImage(img)
    canvas_c.image=photo
    canvas_c.create_image(0,0,anchor="nw",image=photo)
    time.sleep(2.5)
    img=cv2.imread("Celeb.jpg")
    if(char=='not'):
        img=cv2.imread("Not final.jpg")
    img=imutils.resize(img,width=c_width,height=c_height)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    photo=ImageTk.PhotoImage(img)
    canvas_c.image=photo
    canvas_c.create_image(0,0,anchor="nw",image=photo)
    time.sleep(2.5)
    root.destroy()
    


def Out():
    thread=threading.Thread(target=Pending,args=("out",),daemon=True)
    thread.start()
def Not_Out():
    thread=threading.Thread(target=Pending,args=('not',),daemon=True)
    thread.start()
    
    
   



#Reading a Video
stream=cv2.VideoCapture("Symond direct.mp4")
#Play function
def play(speed):
    print('yes')
    print(f"Speed is{speed}.")
    cur=stream.get(1)
    stream.set(1,cur+speed)
    ret,frame=stream.read()
    if(ret==True):
        frame=imutils.resize(frame,width=c_width,height=c_height)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame=Image.fromarray(frame)
        photo=ImageTk.PhotoImage(frame)
        canvas_c.image=photo
        canvas_c.create_image(0,0,anchor=NW,image=photo)


#Zoom Function   
def Zoom_In():
    print("Zoom in")
    global curx,cury
    if(curx<1200 and cury<850):
        
        
        canvas_c.delete('all')
        cur=stream.get(1)
        stream.set(1,cur-1)
        ret,frame=stream.read()
        frame=imutils.resize(frame,width=curx+100,height=cury+50)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas_c.image=frame
        canvas_c.create_image(0,0,anchor=NW,image=frame)
        curx+=50
        cury+=50
        return

def Zoom_Out():
    print("Zoom out")
    global curx,cury
    if(curx>800 and cury>450):
        
        canvas_c.delete('all')
        cur=stream.get(1)
        stream.set(1,cur-1)
        ret,frame=stream.read()
        frame=imutils.resize(frame,width=800,height=450)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas_c.image=frame
        canvas_c.create_image(0,0,anchor=NW,image=frame)
        curx=800
        cury=450
        return
    else:
        return



#Here We Go
root=Tk()
root.title("3rd umpire")

root.geometry(f"{Width}x{Height}")

#Main Canvas -> canvas_c
canvas_c=Canvas(root,width=c_width,height=c_height,bg="green",relief="solid",borderwidth=1)
img=cv2.imread("Adelaide oval.jpg")
img=imutils.resize(img,width=c_width,height=c_height)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=Image.fromarray(img)
photo=ImageTk.PhotoImage(img)
canvas_c.create_image(0,0,anchor=NW,image=photo)
canvas_c.place(x=230,y=10)

#Canvas for Roll Back
canvas=Canvas(root,width=200,height=450,bg='red',relief="solid",borderwidth=1)
canvas.create_text(100,30,text="Roll Back",font="TimesNewRoman 25 bold")
b1=Button(canvas,text="< Roll Back",activebackground="medium spring green",font="Helevetica 19 bold",padx=3,pady=3,command=partial(play,-2),bg="light goldenrod")
canvas.create_window(100,150,window=b1)
b1=Button(canvas,text="<< Roll Back",font="Helevetica 19 bold",activebackground="medium spring green",pady=3,padx=3,command=partial(play,-15),bg="light goldenrod")
canvas.create_window(100,270,window=b1)
b1=Button(canvas,text="<<< Roll Back",font="Helevetica 19 bold",activebackground="medium spring green",padx=3,pady=3,command=partial(play,-25),bg="light goldenrod")
canvas.create_window(102,390,window=b1)
canvas.place(x=1050,y=10)
canvas.place(x=10,y=10)



#Canvas for Move Forward
canvas=Canvas(root,width=200,height=450,bg='red',relief="solid",borderwidth=1)
canvas.create_text(100,30,text="Forward",font="Helevetica 30 bold")
b1=Button(canvas,text="Forward >",font="Helevetica 20 bold",padx=3,activebackground="gold2",pady=3,command=partial(play,0.01),bg="SlateGray1")
canvas.create_window(100,150,window=b1)
b1=Button(canvas,text="Forward >>",font="Helevetica 20 bold",padx=3,activebackground="gold2",pady=3,command=partial(play,15),bg="SlateGray1")
canvas.create_window(100,270,window=b1)
b1=Button(canvas,text="Forward >>>",font="Helevetica 20 bold",padx=3,pady=3,activebackground="gold2",command=partial(play,25),bg="SlateGray1")
canvas.create_window(103,390,window=b1)
canvas.place(x=1050,y=10)




#Canvas for Zooming
canvas=Canvas(root,width=400,height=160,bg="tan1",relief="solid",borderwidth=1)
canvas.create_text(200,30,text="Zoom",font="Helevetica 30 bold")
b1=Button(canvas,text="Zoom In",font="Helevetica 20 bold",command=Zoom_In,activebackground="Lawn Green",bg="LightSteelBlue2",padx=2,pady=2)
canvas.create_window(90,100,window=b1)
b1=Button(canvas,text="Zoom Out",font="Helevetica 20 bold",command=Zoom_Out,activebackground="Lawn Green",bg="LightSteelBlue2",padx=2,pady=2)
canvas.create_window(300,100,window=b1)
canvas.place(x=10,y=500)




#Canvas for Decision
canvas=Canvas(root,width=450,height=160,relief="solid",borderwidth=1,bg="LightGoldenrod1")
canvas.create_text(220,30,text="Decision Box",font="TimesNewRoman 30 bold")
canvas.place(x=800,y=500)
b1=Button(canvas,text="OUT!",font="Helevetica 25 bold",command=Out,fg="Red",activebackground="red")
canvas.create_window(100,100,window=b1,width=170)
b1=Button(canvas,text="NOT OUT",font="Helvetica 25 bold",command=Not_Out,fg="green",pady=2,padx=3,activebackground="green")
canvas.create_window(350,100,window=b1,width=180)



#Start Button
b1=Button(root,text="START >",font="Helvetica 30 bold",bg='medium spring green',activebackground="Light Goldenrod2",width=12,relief="solid",borderwidth=1,height=1,comman=partial(play,0.01))
b1.place(x=475,y=585)



#Label for Clock
label=Label(root,borderwidth=1,relief="solid",font="Helevetica 35 bold",fg="maroon")
label.place(x=480,y=500)
clock()
root.mainloop()
