import tkinter as tk
import numpy as np

##Generate Number
c=np.random.randint(0,10,(1,4))
print(c)
tries=1
frame=""
correct=[False,False,False,False]
def start():
 global tries
 def check():
  nonlocal label,button,lbl
  global tries,frame,label2,label1,label3
  N=inp.get()
  inp.delete(0,tk.END)
  ##check if input is a string
  try:
   int(N)
   lbl.place_forget()
   lbl1.place_forget()
  ##Check if input is correct guess
   if len(N)<4:
     lbl1.place(x="265",y="260")
     return
   for i in range(4):
    correct[i]=True if c[0][i].astype(str)==N[i] else False
  ##runs if the guess is correct

   if all(correct):
    label.destroy()
    inp.destroy()
    if frame and label2:
     frame.destroy()
     label2.destroy()
    button.config(command=window.destroy)
    window.geometry("800x100")
    label3=tk.Label(window,text=f"Correct Guess!, the number was {N}",font=("Arial",10,"bold"),fg="green")
    label3.pack()
   else:
   ##runs if out of turns
    if tries>3:
     for widget in window.winfo_children():
      if widget==button:
       continue
      else:
       widget.destroy()
     window.geometry("800x100")  
     label5=tk.Label(text="You're out of tries, the number was:",font=("arial",10),fg="red")
     label5.pack(side="left")
     frame1=tk.Frame(window) 
     for i in range(4):
      label6=tk.Label(frame1,text=c[0][i].astype(str),fg="red")
      label6.pack(side="left")
     frame1.pack(after=label5,side="bottom") 
     button.config(command=window.destroy)
     button.pack(side="bottom",anchor="n")
   ##runs if guess is NOT correct
    else:
     if frame and label2:
      frame.destroy()
      label2.destroy()
     frame=tk.Frame(window)
     frame.pack(side="right",anchor="e")
     label2=tk.Label(window,text="Previous Guess :")
     label2.pack(side="left",anchor="w",before=frame)
     for i in range(4):
     ##Display which digits are correct

      col="green" if correct[i] else "yellow" if int(N[i]) in c else "red"
      label1=tk.Label(frame,text=N[i],fg=col) 
      label1.pack(side="left")
     tries=tries+1
     label.config(text=f"Guess number {tries}")
     return
  except ValueError: 
   lbl.place(x="350",y="250")
   
 ##Make Window!

 window=tk.Tk()
 window.geometry("800x300")
 window.title("Number Guesser Game") 
 ##Setup input

 label=tk.Label(window,text=f"Guess number {tries}",font=("Ariel",16))
 label.pack(side="left",anchor='nw')
 inp=tk.Entry(window,font=("Arial",16))
 inp.pack(after=label)
 button=tk.Button(window,text="Done",command=check)
 button.pack()
 lbl1=tk.Label(window,text="Size of input must be at least 4 characters!", fg="red")
 lbl1.place(x="350",y="280")
 lbl1.place_forget()
 lbl=tk.Label(window,text="Input must be an integer!",fg="red")
 lbl.place(x="350",y="250")
 lbl.place_forget()
 window.mainloop()
start() 
