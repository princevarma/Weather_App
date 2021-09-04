from tkinter import *
import requests
#pip install pillow (used to deal with image files)
from PIL import Image,ImageTk
#Weather api file
import weatherApi
import wave

class Weather:
    def __init__(self,root):
        self.root=root
        self.root.title("My Weather App")
        self.root.geometry("350x400+450+100")
        #geometry(width x height +left to(distance) +top(distance))
        self.root.config(bg="silver")  #color of root window
        
        #---icon-----#
        self.search_icon=Image.open("icons/search.png")
        self.search_icon=self.search_icon.resize((20,20),Image.ANTIALIAS)
        self.search_icon=ImageTk.PhotoImage(self.search_icon)

        #---Variable------#
        self.var_search=StringVar()  #variable for entry box 
        
        
        #Title of the App (Label1)
        title=Label(self.root,text="Weather App", font=('poppins',30,"bold"),bg="#262626",fg="white").place(x=0,y=0,relwidth=1,height=60)
        #City Name (Label2)
        lbl_city=Label(self.root,text="City Name  :", font=('poppins',10,"italic"),bg="gray",fg="Black",anchor='w', padx=5).place(x=0,y=60,relwidth=1,height=40)
        #Entry box
        txt_city=Entry(self.root,textvariable=self.var_search, font=('poppins',10),bg="white",fg="#262626" ).place(x=100,y=68,width=200,height=25)
        #button
        btn_search=Button(self.root,cursor='hand2',image=self.search_icon,bg="gray",activebackground="gray",bd=0, command=self.get_weather).place(x=310,y=68,width=30,height=25)




        #-----------Result-------------------
        self.lbl_city=Label(self.root, font=('poppins',10,"italic"),bg="silver",fg="Black")
        self.lbl_city.place(x=0,y=120,relwidth=1,height=20)
        self.lbl_icons=Label(self.root, font=('poppins',10,"italic"),bg="silver")
        self.lbl_icons.place(x=0,y=143,relwidth=1,height=100)
        self.lbl_temp=Label(self.root, font=('poppins',10,"italic"),bg="silver",fg="Teal")
        self.lbl_temp.place(x=0,y=246,relwidth=1,height=20)
        self.lbl_wind=Label(self.root, font=('poppins',10,"italic"),bg="silver",fg="white")
        self.lbl_wind.place(x=0,y=269,relwidth=1,height=20)

        self.lbl_error=Label(self.root, font=('poppins',10,"italic"),bg="silver",fg="Maroon")
        self.lbl_error.place(x=0,y=289,relwidth=1,height=20)
        


    def get_weather(self):
        api_key=weatherApi.api_key
        complete_url =f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
        #cityname,counntry name,icons,temp_c,temp_f,wind
        if self.var_search.get()=="":
            self.lbl_city.config(text="")
            self.lbl_icons.config(image="")
            self.lbl_temp.config(text="")
            self.lbl_wind.config(text="")
            self.lbl_error.config(text="City Name Required")
            
        else:
            result=requests.get(complete_url)
            if result:
                json=result.json()
                city_name=json["name"]
                country=json["sys"]["country"]
                icons=json["weather"][0]["icon"]
                temp_c=json["main"]["temp"]-273.15
                temp_f=(json["main"]["temp"] -273.15) * 9/5+32
                wind=json["weather"][0]["main"]

                self.lbl_city.config(text=city_name+" , "+country)

                #---new_icon-----#
                self.search_icon2=Image.open(f"icons/{icons}.png")
                self.search_icon2=self.search_icon.resize((100,100),Image.ANTIALIAS)
                self.search_icon2=ImageTk.PhotoImage(self.search_icon2)
                self.lbl_icons.config(image=self.search_icon2)

                deg=u"\N{DEGREE SIGN}"
                self.lbl_temp.config(text=str(round(temp_c,2))+deg+" C | " +str(round(temp_f,2))+deg+" f")
                self.lbl_wind.config(text=wind)
                self.lbl_error.config(text="")
            else:
                self.lbl_city.config(text="")
                self.lbl_icons.config(image="")
                self.lbl_temp.config(text="")
                self.lbl_wind.config(text="")
                self.lbl_error.config(text="Invalid City Name")
            
        
            


root=Tk()
obj=Weather(root)
root.mainloop()