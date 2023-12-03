from tkinter import*
import random
root=Tk()
root.title("Random Background")
root.geometry("600x600")

colors=["orange","red","pink","yellow","blue","green","purple"]
random_color = {"color":colors}

def rand1_bg():
    random_no=random.randint(0,9)
    random_colo1r=random_color['color'][random_no]
    root.configure(background=random_colo1r)
   
    
btn=Button(root,text="Random Background",command=rand1_bg)
btn.pack()
    
root.mainloop()