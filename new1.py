from tkinter import StringVar, Tk, BOTH, getint, messagebox
from tkinter.ttk import Frame, Button
from fuction import fuc_1
import tkinter as tk



class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.lis = []
        
        self.parent.geometry("400x400")
        
        self.text = tk.StringVar(parent, value="Cacalutor viet")
        self.label = tk.Label(parent, textvariable=self.text,font=('Timesnewroman', 40))
        self.label.pack()
        
        self.b1 = Button(self.parent, text = '+', command=self.onCong)
        self.b1.place(x = 130, y = 50)
        self.b2 = Button(self.parent, text = '-', command= self.onTru)
        self.b2.place(x = 210, y = 50)
        self.b3 = Button(self.parent, text = 'x', command= self.onNhan)
        self.b3.place(x = 290, y = 50)
        self.b4 = Button(self.parent, text = '/', command= self.onChia)
        self.b4.place(x = 290, y = 100)
        self.b4 = Button(self.parent, text = '%', command= self.onDu)
        self.b4.place(x = 290, y = 200)
        self.b4 = Button(self.parent, text = 'xoa', command= self.onXoa)
        self.b4.place(x = 290, y = 150)
        self.b4 = Button(self.parent, text = '=', command=self.onBang)
        self.b4.place(x = 210, y = 250)

        init_val = 50
        x = y = init_val
        so_nut = 9
        so_cot = 3
        space = 80
        for number in range(0,so_nut + 1):
            btn = Button(self.parent, text = number)
            btn.configure(command=lambda btn=btn: self.onClick(text=btn["text"]))
            btn.place(x = x ,y = y)
            self.lis.append(btn)
            x = x + space 
            if number % so_cot == 0:
                x = init_val
                y = y + space -30      
        self.place()

        self.value1 = ""
        self.value_2 = ""
        self.cacu_on = False
        self.show_text = ""

        
    def onClick(self, text):
        if not self.cacu_on:
            self.value1 = self.value1 + str(text)
            show_text = self.value1
        else:
            self.value_2 = self.value_2 + str(text)

        self.show_text = self.show_text + str(text)

        self.text.set(self.show_text)

 
    def onCong(self):
        self.cacu_on = True
        self.nhan_nut = 'cong'
        self.show_text = self.show_text + "+"
        self.text.set(self.show_text)

        
    def onTru(self):
        self.cacu_on = True
        self.nhan_nut = 'tru'
        self.show_text = self.show_text + "-"
        self.text.set(self.show_text)

    def onNhan(self):
        self.cacu_on = True
        self.nhan_nut = 'nhan'
        self.show_text = self.show_text + "*"
        self.text.set(self.show_text)

    def onChia(self):
        self.cacu_on = True
        self.nhan_nut = 'chia'
        self.show_text = self.show_text + "/"
        self.text.set(self.show_text)

    def onDu(self):
        self.cacu_on = True
        self.nhan_nut = 'du'
        self.show_text = self.show_text + "%"
        self.text.set(self.show_text)

    def onBang(self): 
        
        if self.nhan_nut == 'cong':    
            ket_qua =int(self.value1) + int(self.value_2)
            print(ket_qua)  
        elif self.nhan_nut == 'tru':    
            ket_qua =int(self.value1) - int(self.value_2)
            print(ket_qua)  
        elif self.nhan_nut == 'nhan':    
            ket_qua =int(self.value1) * int(self.value_2)
            print(ket_qua)
        elif self.nhan_nut == 'chia':    
            ket_qua =int(self.value1) / int(self.value_2)
            print(ket_qua)
        elif self.nhan_nut == 'du':    
            ket_qua =int(self.value1) % int(self.value_2)
            print(ket_qua)
        self.show_text = self.show_text + "=" + str(ket_qua)
        self.text.set(self.show_text)

    def onXoa(self):
        self.value1 = ""
        self.value_2 = ""
        self.cacu_on = False
        self.show_text = ""
        self.text.set(self.show_text)



#    def onTru
 #   def onNhan
  #  def onChia
   # def onBang

        

def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()