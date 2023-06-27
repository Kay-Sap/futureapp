from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import sleep
import random
class App(Tk):
    def __init__(self):
        super().__init__()
        self.page()
        

    def page(self):
       
        self.quest_list = {'ရည်းစားဘယ်ချိန်ရမလဲ?':
                           ["ဒီတစ်သက်ရမည် မဟုတ်ပါ။",'မကြာခင်ရမှာပါ,စောင့်ဖို့တော့လိုအပ်လိမ့်မယ်။',
                            "ဒီတစ်လအတွင်း အနာဂတ် ပါတနာနဲ့ တွေ့ဖို့ကိန်းရှိတယ်","နှစ်ကုန် လောက်မှာ တွေ့ရလိမ့်မယ်။"] ,
                            "ဘဝမှာအောင်မြင်မလား?":
                            ["အောင်မြင်ကိန်းရှိတယ်, ဒါ့ကြောင့် အပျင်းမထူနဲ့တော့။" ,'စိတ်တော့မကောင်းဘူး , မင်းအောင်မြင်ဖို့တော့မဖြစ်နိုင်ဘူး။',
                             'မင်းဟာလုံး၀အောင်မြင်လိမ့်မယ်, \n ခုလျှောက်နေတဲ့လမ်း ကို ဆက်လျှောက်နေဖို့တော့လို တယ်။',
                             'မင်းရည်မှန်းထားတဲ့ ပန်းတိုင်ကိုတော့ ရောက်လိမ့်မယ်။'],
                             "ကလေးဘယ်နယောက်ရမလဲ?":
                             ["အနည်းဆုံး ၄ ယောက်ရဖို့ကိန်းရှိတယ်။","ချစ်စရာလေး သားနဲ့သမီး ၂ယောက်ရမယ်။",
                              "မင်းမရနိုင်တာ မင်းအသိဆုံး။","၁ ယောက်ပဲရမယ်။"]}
        self.title('ဗေဒင် အက်ပလီကေးရှင်း')
        self.geometry('800x500')
        self.resizable(False,False)
        self.configure(bg = '#C2C2C2')

        self.box = Frame(self  , highlightbackground='black' ,
                    highlightthickness=1)
        self.box.place(x = 100 ,y=150)

        

        #first row
        self.Frame1 = Frame(self.box)
        self.Frame1.pack()

        self.name_var = StringVar()
                    
        self.name = Entry(self.Frame1 , 
                    textvariable = self.name_var,
                    font = 'airla 15 bold' , width = 15 ,
                        highlightbackground='black',
                        highlightthickness=1,borderwidth=0,
                        )
        self.name.insert(0,'အမည်')
        self.name.grid(row = 0 , column = 0,padx=20 , pady=20)
        self.name.bind('<FocusIn>',self.temp_txt)

        self.age_var = StringVar()
        self.age_value = ['၁၅','၁၆','၁၇','၁၈','၁၉','၂၀','၂၁','၂၂','၂၃','၂၄','၂၅','၂၆','၂၇',
                    '၂၈','၂၉','၃၀']
        self.age = ttk.Combobox(self.Frame1 , 
                        values=self.age_value,
                        font='airla 15 bold',
                        width=13 , textvariable=self.age_var)
        self.age.grid(row = 0 ,column=1 , pady = 20)
        self.age.set('အသက်')

        self.birth_date_var = StringVar()
        self.date_value = ['တနင်္ဂနွေ','တနင်္လာ','အင်္ဂါ','ဗုဒ္ဓဟူး','ကြာသပတေး','သောကြာ','စနေ']
        self.birth_date = ttk.Combobox(self.Frame1 , 
                        values=self.date_value,
                        font='airla 15 bold',
                        width=13,textvariable=self.birth_date_var)
        self.birth_date.grid(row = 0 ,column=2 , padx=20 , pady=20)
        self.birth_date.set('မွေးရက်')

        # second row
        self.Frame2 = Frame(self.box)
        self.Frame2.pack()
        self.month_var = StringVar()
        self.month_value = ["ဇန်နဝါရီလ","ဖေဖော်ဝါရီ",'မတ်လ','ဧပြီလ','မေလ','ဇွန်လ',
                    'ဇူလိုင်လ','သြဂုတ်လ','စက်တင်ဘာလ','အောက်တိုဘာလ','နိုဝင်ဘာလ','ဒီဇင်ဘာလ']
        self.birth_month = ttk.Combobox(self.Frame1 , 
                        values=self.month_value,
                        font='airla 15 bold',
                       width=13,textvariable=self.month_var)
        self.birth_month.grid(row = 1 , column=0)
        self.birth_month.set('မွေးလ')

        self.year_var = StringVar()
        self.year_value = ['၁၉၉၃','၁၉၉၄','၁၉၉၅','၁၉၉၆','၁၉၉၇','၁၉၉၈','၁၉၉၉',
                    '၂၀၀၀','၂၀၀၁','၂၀၀၂','၂၀၀၃','၂၀၀၄','၂၀၀၅','၂၀၀၆',
                    '၂၀၀၇','၂၀၀၈','၂၀၀၉','၂၀၁၀','၂၀၁၁']
        self.birth_year = ttk.Combobox(self.Frame1 , 
                        values=self.year_value,
                        font='airla 15 bold',
                        width=13,textvariable=self.year_var)
        self.birth_year.grid(row = 1 , column=1)
        self.birth_year.set('ခုနှစ်')

        self.gender_var = StringVar()
        self.gender_vlaue = ['ကျား','မ']
        self.gender = ttk.Combobox(self.Frame1 , 
                        values=self.gender_vlaue,
                        font='airla 15 bold',
                        width=13,textvariable=self.gender_var)

        self.gender.grid(row = 1 , column=2 , pady=10)
        self.gender.set('လိင်')
        # third row
        self.Frame2 = Frame(self.box)
        self.Frame2.pack()
        self.question_var = StringVar()
        self.quest = list(self.quest_list.keys())
        self.question = ttk.Combobox(self.Frame2 , 
                        values=self.quest,
                        font='airla 13',
                        width=58,
                        textvariable=self.question_var)

        self.question.grid( pady = 25)
        self.question.set('မေးခွန်း မေးရန်')

        # fourth row

        Frame3  = Frame(self.box)
        Frame3.pack()
        btn = Button(Frame3 , text = 'ဗေဒင်' , background='#FF9500' , width=57,
                    font = 'airla 12',borderwidth=0 ,command = self.predict)
        btn.grid()

    def temp_txt(self,e):
            if self.name_var.get() == 'အမည်':
                self.name.delete(0,END)

    def predict(self):
        
        l =self.name_var.get()
        if l != 'အမည်' and l!='':
            
            self.box.destroy()
            self.title('နတ်ပေါင်း များစွာ သို့ဒေတာပို့ နေပါသည်....')
            
            self.configure(bg = '#C2C2C2')
            
            self.bar = ttk.Progressbar(self , orient=HORIZONTAL , length= 500, )
            self.bar.place(x = 150,y=200)

            self.info = Label(self , text = 'နတ်ပေါင်း များစွာ သို့ဒေတာပို့ နေပါသည်.... ' ,
                            background='#C2C2C2')
            self.info.place(x = 250,y=230)

            x = 0
            task = 100
            while (x<task):
                self.bar['value']+=1
                sleep(0.01)
                x+=1
                self.update_idletasks()
            self.future()
        else:
            messagebox.showerror('အယ်ရာ','အချက်အလက်အပြည့်အစုံဖြည့်ပါ။')
        
            

    def future(self):
        self.bar.destroy()
        self.info.destroy()

        self.title(self.name_var.get())
        # self.geometry('800x500')
        
        self.configure(bg = '#c4f5e7')
        self.name = Label(self , text = self.name_var.get()+' အတွက် ဗေဒင်' ,
                font = 'comic 30 bold' ,
                    bg = '#c4f5e7',
                    fg = 'Black')
        self.name.pack()
        
        self.quest_lbl = Label(self , text = 'မေးခွန်း။။   ။။ '+  self.question_var.get(),font = 'com 15' , bg = '#c4f5e7')
        self.quest_lbl.place(x = 80 , y = 150)

        
        
        self.ans_lbl  = Label(self , text = 'ဗေဒင်။။   ။။ '+ self.get_data(), font = 'com 15', bg = '#c4f5e7',fg ='blue')
        self.ans_lbl.place(x = 93 , y = 200)
        
        self.btn = Button(self , text='<နောက်သို့' , borderwidth=0 ,
                           background='#c4f5e7',activebackground='#c4f5e7',
                           activeforeground='red',command = self.back)
        self.btn.place(x = 0 , y = 474)

    def get_data(self):
        if self.question_var.get() in list(self.quest_list.keys()):
            self.temp_quest = self.question_var.get()
            m = self.quest_list[self.temp_quest]
            size = len(m)
            self.output = self.quest_list[self.temp_quest][random.randint(0,size-1)]
            self.output = self.quest_list[self.temp_quest][0]
            return self.output
        
        else:
            messagebox.showerror('အယ်ရာ.','တစ်စုံတစ်ခု မှားနေပါသည်။')
            return '!!!!!!တစ်စုံတစ်ခု မှားနေပါသည်။!!!'
    def back(self):
        self.quest_lbl.destroy()
        self.ans_lbl.destroy()
        self.name.destroy()
        self.btn.destroy()

        self.page()    
if __name__ =='__main__':
    app = App()
    app.mainloop()