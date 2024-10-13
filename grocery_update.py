from tkinter import *
import mysql.connector
import tkinter.messagebox
db = mysql.connector.connect(host="localhost",user="root",password="Navee@03",db="grocery")
cursor = db.cursor()
cursor.execute("SELECT max(id) FROM hitnalli")
result = cursor.fetchall()
if result is not None:
    for r in result:
        id = r[0]
else:
    print("No results found")
class Database:
    def __init__(self ,master):
        self.master=master
        self.heading=Label(master,text="Update Stock",font=('arial 40 bold'),fg='steelblue')
        self.heading.place(x=500 , y=0)

        self.i=Label(master, text="ID Enter here: ",font=('arial 18 bold'))
        self.i.place(x=0,y=40)
        self.i_a=Entry(master,width=10,font=('arial 18 bold'))
        self.i_a.place(x=220,y=40)
        self.i_a.focus()
        

        self.btn_search=Button(master,text="Search",width=15,height=2,bg="orange",command=self.search)
        self.btn_search.place(x=350, y=40)

        
        self.name=Label(master,text="Enter Product Name",font=('arial 18 bold'))
        self.name.place(x=0,y=80)
        
        self.stock=Label(master,text="Enter Stocks",font=('arial 18 bold'))
        self.stock.place(x=0,y=120)

        self.cost_price=Label(master,text=" Enter Cost price",font=('arial 18 bold'))
        self.cost_price.place(x=0,y=160)

        self.sell_price=Label(master,text="Enter Selling price",font=('arial 18 bold'))
        self.sell_price.place(x=0,y=200)

        self.totalcostprice=Label(master,text=" totalcp ",font=('arial 18 bold'))
        self.totalcostprice.place(x=0,y=240)

        self.totalsellprice=Label(master,text=" totalsp ",font=('arial 18 bold'))
        self.totalsellprice.place(x=0,y=280)

        self.vendor=Label(master,text=" EnterVendor name ",font=('arial 18 bold'))
        self.vendor.place(x=0,y=320)

        self.vendor_mobile_number=Label(master,text=" EnterMobile number",font=('arial 18 bold'))
        self.vendor_mobile_number.place(x=0,y=360)

        

        self.name_a=Entry(master,width=30,font=('arial 18 bold'))
        self.name_a.place(x=250 ,y = 80)
         

        self.name_b=Entry(master,width=30,font=('arial 18 bold'))
        self.name_b.place(x=250 ,y = 120)

        self.name_c=Entry(master,width=30,font=('arial 18 bold'))
        self.name_c.place(x=250 ,y = 160)

        self.name_d=Entry(master,width=30,font=('arial 18 bold'))
        self.name_d.place(x=250 ,y = 200)

        self.name_g=Entry(master,width=30,font=('arial 18 bold'))
        self.name_g.place(x=250 ,y = 240)

        self.name_h=Entry(master,width=30,font=('arial 18 bold'))
        self.name_h.place(x=250 ,y = 280)

        self.name_e=Entry(master,width=30,font=('arial 18 bold'))
        self.name_e.place(x=250 ,y = 320)

        self.name_f=Entry(master,width=30,font=('arial 18 bold'))
        self.name_f.place(x=250 ,y = 360)
        

        

        self.button=Button(master,text="Update to Database",width=25,height=2,bg="steelblue",fg="pink",command=self.update)
        self.button.place(x=460,y=420)
        
        self.textbox=Text(master,width=80,height=18)
        self.textbox.place(x=650,y=80)
        self.textbox.insert(END,"Product has reached upto: " +str(id))
        
        self.master.bind("<Return>",self.search)
        self.master.bind("<Up>",self.update)
    def search(self,master=None,event=None):
        try:
            self.get_id = int(self.i_a.get())
        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter a valid product ID (integer only)")
        else:
    # If no exception is raised, execute this block
            pass
        
        sql="select * from hitnalli where id = %s "
        result1=cursor.execute(sql,(self.i_a.get(),))
        result1 = cursor.fetchall()
        for r in result1:
            self.n1=r[1] #name
            self.n2=r[2] #stock
            self.n3=r[3] #costprice
            self.n4=r[4] #stockprice
            self.n5=r[5] #totalcostprice
            self.n6=r[6] #totalsellprice
            self.n7=r[7] #assumeprofit
            self.n8=r[8] #vendor
            self.n9=r[9] #vendor_pho
        db.commit()
        self.name_a.delete(0,END)
        self.name_a.insert(0,str(self.n1))

        self.name_b.delete(0,END)
        self.name_b.insert(0,str(self.n2))

        self.name_c.delete(0,END)
        self.name_c.insert(0,str(self.n3))

        self.name_d.delete(0,END)
        self.name_d.insert(0,str(self.n4))

        self.name_g.delete(0,END)
        self.name_g.insert(0,str(self.n5))

        self.name_h.delete(0,END)
        self.name_h.insert(0,str(self.n6))

        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n8))
        

        self.name_f.delete(0,END)
        self.name_f.insert(0,str(self.n9))


    def update(self,master=None,event=None):
        self.name=self.name_a.get()
        self.stock=self.name_b.get()
        self.costprice=self.name_c.get()
        self.sellprice=self.name_d.get()
        self.totalcostprice=self.name_g.get()
        self.totalsellprice=self.name_h.get()
        self.vendor=self.name_e.get()
        self.vendor_phone=self.name_f.get()

        query="update hitnalli set sname = %s , stock= %s,costprice= %s, sellprice= %s, totalcostprice= %s, totalsellprice= %s, vendor= %s, vendor_phone_number= %s where id= %s"
        cursor.execute(query,(self.name,self.stock,self.costprice,self.sellprice,self.totalcostprice,self.totalsellprice,self.vendor,self.vendor_phone,self.i_a.get(),))
        db.commit()
        self.textbox.insert(END, "\n\n Product Updated  " + str(self.name) + " into the database.")

        tkinter.messagebox.showinfo("Success","Stock  updated  succesfully")
        self.name_a.delete(0,END)
        
        #self.name_a.insert(0,str(self.n1))

        self.name_b.delete(0,END)
        #self.name_b.insert(0,str(self.n2))

        self.name_c.delete(0,END)
        #self.name_c.insert(0,str(self.n3))

        self.name_d.delete(0,END)
        #self.name_d.insert(0,str(self.n4))

        self.name_g.delete(0,END)
        #self.name_g.insert(0,str(self.n5))

        self.name_h.delete(0,END)
        #self.name_h.insert(0,str(self.n6))

        self.name_e.delete(0,END)
        #self.name_e.insert(0,str(self.n8))
        

        self.name_f.delete(0,END)

        self.i_a.delete(0,END)
       
        #self.name_f.insert(0,str(self.n9))
        self.i_a.focus()


        

        
        
        
            
        
        
root = Tk()
b=Database(root)
root.geometry('1920x1080')
root.title("update the database")
root.mainloop()
