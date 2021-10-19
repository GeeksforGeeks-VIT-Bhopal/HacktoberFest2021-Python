from tkinter import *
import math
import tkinter.messagebox


#creating a window
root = Tk(className='Python Examples - Window Color')
pic=PhotoImage(file="onee.png")
root.iconphoto(False, pic)
root.configure(bg="black")
root.title("Scientific Calculator")

e=Entry(root,width=53,border=15,font="Verdana", bg="white", fg="black", justify=RIGHT, cursor="arrow")
e.grid(row=0,column=0, columnspan=6, padx=10, pady=20,ipady=18)
root.resizable(width=False, height=False)
photo = PhotoImage(file ="one.png")

class calculator:
    def _init_(self):
        pass
    
    def rad(self,num):
        try:
            p=num*(3.14/180)
            return p
        except:
            tkinter.messagebox.showerror("#Error", "Check Your values and operators")
    def butclick(self,numb):
        current=e.get()
        e.delete(0,END) 
        e.insert(0,str(current) + str(numb))

    def butclear(self):
        e.delete(0,END)

    def butequal(self):
        second=e.get()
        e.delete(0,END)
        if mathe == "Addition":
            try:
                e.insert(0,eval(second))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,second)
        if mathe == "Multiplication":
            try:
                e.insert(0,eval(second))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,(second))
        if mathe == "Subtraction":
            try:
                e.insert(0,eval(second))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,second)
        if mathe == "Division":
            try:
                e.insert(0,eval(second))
                    
            except ZeroDivisionError:
                tkinter.messagebox.showerror("#Error", "Number cannot be divided by 0")
                e.insert(0,second)
        if mathe=="Power":
            try:
                e.insert(0,(eval(second)))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,second)  
        if mathe=="Sqrt":
            try:
                e.insert(0,(eval(str(fnumb) + str(math.sqrt(eval(second))))))
            except:  
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnum)) 
        if mathe=="Factorization":
            try:
                e.insert(0,eval(str(fnumb) + str(math.factorial(eval(second)))))
            except:
                   
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb)) 
        if mathe=="Sin":
            second=eval(second)
            try:
                if second%90==0:
                        e.insert(0,eval(str(fnumb)+ str(int(math.sin(math.radians(second))))))
                else:
                        e.insert(0,eval(str(fnumb)+ str(math.sin(math.radians(second)))))
            except:    
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Cos":
            second=eval(second)
            try:
                if second%90==0:
                        e.insert(0,eval(str(fnumb)+ str(int(math.cos(math.radians(second)))))) 
                else:
                        e.insert(0,eval(str(fnumb)+ str(math.cos(math.radians(second)))))
            except:   
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Tan":
            second=eval(second)
            try:
                if second%90==0:
                        e.insert(0,eval(str(fnumb)+ str(tan(math.cos(math.radians(second))))))
                else:
                        e.insert(0,eval(str(fnumb)+ str(math.tan(math.radians(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Sinin":
            try:
                e.insert(0,eval(str(fnumb) + str(math.degrees(math.asin(eval(second))))))
            except:  
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Cosin":
            try:
                e.insert(0,eval(str(fnumb) + str(math.degrees(math.acos(eval(second))))))
            except:    
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Tanin":
            try:
                e.insert(0,eval(str(fnumb) + str(math.degrees(math.atan(eval(second))))))
            except:  
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Log":
            try :
                e.insert(0,eval(str(fnumb) + str(math.log10(eval(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Round":
            try:
                e.insert(0,eval(str(fnumb) + str(round(eval(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Rad":
            try:
                e.insert(0,eval(str(fnumb) + str(math.radians(eval(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Ln":
            try:
                e.insert(0,eval(str(fnumb) + str(math.log(eval(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(fnumb))
        if mathe=="Modulus":
            try:
                e.insert(0,eval(second))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0,str(second))
                    
        if mathe=="Remove":
            e.insert(0,math.degrees(math.atan(eval(second))))
                
    def butadd(self):
        
        fnumb=e.get()
        global fnum
        fnum=str(fnumb) + "+"
        e.delete(0,END)
        global mathe
        mathe="Addition"
        e.insert(0, str(fnum))
       
    def butsub(self):
        fnumb=e.get()
        global fnum
        fnum=str(fnumb) + "-"
        e.delete(0,END)
        global mathe
        mathe="Subtraction"    
        e.insert(0, str(fnum))

    def butmul(self):
        fnumb=e.get()
        global fnum
        fnum=str(fnumb) + "*"
        e.delete(0,END)
        global mathe
        mathe="Multiplication"    
        e.insert(0, str(fnum))
           
    def butdiv(self): 
        fnumb=e.get()
        global fnum
        fnum=str(fnumb) + "/"
        e.delete(0,END)
        global mathe
        mathe="Division"    
        e.insert(0, str(fnum))

    def butpow(self):
        fnumb=e.get()
        global fnum
        fnum=str(fnumb) + "**"
        e.delete(0,END)
        global mathe
        mathe="Power"    
        e.insert(0, str(fnum))

    def butsqrt(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Sqrt"

    def butfact(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Factorization"

    def butsin(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Sin"
        
        
    def butcos(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Cos"

    def buttan(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Tan"
        
    def butinsin(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Sinin"

    def butincos(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Cosin"
        
    def butintan(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Tanin"

    def butpi(self):
        fnumb=e.get()
        e.delete(0,END)
        e.insert(0,eval(str(fnumb) + str(math.pi)))

    def butlog(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Log"

    def butround(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Round"

    def butrad(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Rad"

    def butln(self):
        fnum=e.get() 
        global fnumb
        fnumb=str(fnum)
        e.delete(0,END)
        global mathe
        mathe="Ln"

    def butmod(self):
        fnumb=e.get()
        global fnum
        fnum=str(fnumb) + "%"
        e.delete(0,END)
        global mathe
        mathe="Modulus"
        e.insert(0, str(fnum))
        
    def bute(self):
        fnumb=e.get()
        e.delete(0,END)
        e.insert(0,eval(str(fnumb) + str(math.e)))

    def butrem(self): 
        leng = len(e.get())
        display = str(e.get())
        if display == '':
            e.insert(0, '')
        elif display == ' ':
            e.insert(0, '')
        elif display == '':
            pass
        else:
            e.delete(0, END)
            e.insert(0, display[0:leng-1])
cal=calculator()
    
But1=Button(root, text="1",padx=43,  pady=20, bg="black", fg="white", font="5",command=lambda: cal.butclick(1))
But2=Button(root, text="2",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(2))             
But3=Button(root, text="3",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(3))
But4=Button(root, text="4",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(4))
But5=Button(root, text="5",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(5))
But6=Button(root, text="6",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(6))
But7=Button(root, text="7",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(7))
But8=Button(root, text="8",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(8))
But9=Button(root, text="9",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(9))
But0=Button(root, text="0",padx=43,  pady=20, bg="black", fg="white",font="5",command=lambda: cal.butclick(0))
Butpoint=Button(root, text=".",padx=56,  pady=20, bg="black",font="10", fg="white",command=lambda: cal.butclick("."))
Butleftb=Button(root, text=")",padx=44,  pady=20, bg="brown",font="10", fg="white",command=lambda: cal.butclick(")"))
Butrightb=Button(root, text="(",padx=45,  pady=20, bg="brown",font="10", fg="white",command=lambda: cal.butclick("("))
Butadd=Button(root, text="+",padx =43,  pady=20, bg="black",font="5", fg="white",command=cal.butadd)
Butequal=Button(root, text="=",padx=54,  pady=20,font="5", bg="black", fg="white",command=cal.butequal)
Butclear=Button(root, text="C",padx=42,  pady=20,font="5", bg="black", fg="white",command=cal.butclear)

#simple math functions
Butsub=Button(root, text="- ",padx =43,  pady=20, bg="black", fg="white",font="5",command=cal.butsub)
Butmul=Button(root, text="*",padx =45,  pady=20, bg="black", fg="white",font="5",command=cal.butmul)
Butdiv=Button(root, text="/",padx =45,  pady=20, bg="black", fg="white",font="5",command=cal.butdiv)

Butpower=Button(root, text="x^y ",padx=36,  pady=20, bg="brown", fg="white",font="5",command=cal.butpow)
Butsqrt=Button(root, text=" √x",padx =37,  pady=20, bg="brown", fg="white",font="5",command=cal.butsqrt)
Butfact=Button(root, text="X!",padx =39,  pady=20,bg="brown", fg="white",font="5",command=cal.butfact)

#trignometry
Butsin=Button(root, text="Sin", padx=47,  pady=20, bg="black", fg="white",font="5", command=cal.butsin)
Butcos=Button(root, text="Cos", padx=44,  pady=20, bg="black", fg="white",font="5", command=cal.butcos)
Buttan=Button(root, text="Tan",padx=45,  pady=20, bg="black", fg="white",font="5", command=cal.buttan)
Butinsin=Button(root, text="Sin^-1",padx=36,  pady=20, bg="brown", fg="white",font="5", command=cal.butinsin)
Butincos=Button(root, text="Cos^-1",padx=40,  pady=20, bg="black", fg="white",font="5", command=cal.butincos)
Butintan=Button(root, text="Tan^-1",padx=41,  pady=20, bg="black", fg="white",font="5", command=cal.butintan)

#pi
Butpi=Button(root, text="π", padx=59, pady=20, fg="white", bg="black",font="5", command=cal.butpi)

#log
Butlog=Button(root, text=" Log", padx=49, pady=20, fg="white", bg="black",font="5", command=cal.butlog)

#round
Butround=Button(root, text="Round", padx=42, pady=20, fg="white", bg="black",font="5", command=cal.butround)

#rad
Butrad=Button(root, text="Rad", padx=49, pady=20, fg="white", bg="brown",font="5", command=cal.butrad)

#ln
Butln=Button(root, text="ln", padx=43, pady=20, fg="white", bg="brown",font="5", command=cal.butln)

#modulus
Butmod=Button(root, text="%", padx=41, pady=20, fg="white", bg="brown",font="5", command=cal.butmod)

#e
Bute=Button(root, text="e", padx=42, pady=20, fg="white", bg="brown",font="5", command=cal.bute)

#remove
Butrem=Button(root, text="⌫", padx=47, pady=20, fg="white", bg="brown",font="5", command=cal.butrem)

#image
pic = photo.subsample(6,9)
Butimage=Button(root,state=DISABLED,image=pic, height="63", width="136")
Buttext=Button(root,text="ABC Calculators",bg="black" ,state=DISABLED, padx=144, pady=22)


#row1
But7.grid(row=1, column=0)
But8.grid(row=1, column=1)
But9.grid(row=1, column=2)
Butequal.grid(row=1, column=3)
Butincos.grid(row=1, column=4)


#row2
But4.grid(row=2, column=0)
But5.grid(row=2, column=1)
But6.grid(row=2, column=2)
Butpoint.grid(row=2, column=3)
Butintan.grid(row=2, column=4)


#Row3
But1.grid(row=3, column=0)
But2.grid(row=3, column=1)
But3.grid(row=3, column=2)
Butsin.grid(row=3, column=3)
Butpi.grid(row=3, column=4)

#row4
Butclear.grid(row=4, column=0)
But0.grid(row=4, column=1)
Butadd.grid(row=4, column=2)
Butcos.grid(row=4, column=3)
Butlog.grid(row=4, column=4)

#row5
Butsub.grid(row=5, column=0)
Butmul.grid(row=5, column=1)
Butdiv.grid(row=5, column=2)
Buttan.grid(row=5, column=3)
Butround.grid(row=5, column=4)

#row6
Butpower.grid(row=6, column=0)
Butsqrt.grid(row=6, column=1)
Butfact.grid(row=6, column=2)
Butinsin.grid(row=6, column=3)
Butrad.grid(row=6, column=4)

#row7
Butln.grid(row=7, column=0)
Bute.grid(row=7, column=1)
Butmod.grid(row=7, column=2)
Butrem.grid(row=7, column=3)
Butimage.grid(row=7, column=4)

#row8
Butrightb.grid(row=8, column=0)
Butleftb.grid(row=8, column=1)
Buttext.grid(row=8, column=2, columnspan=4)
root.mainloop()
 
