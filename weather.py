
from tkinter import  *
from tkinter import ttk
import requests
def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=484aba5bb432888a140ec7ea0c7b1f15").json()
    weather_label1.config(text=data["weather"][0]["main"])
    weather1_label2.config(text=data["weather"][0]["description"])
    weather2_label3.config(text=int(data["main"]["temp"]-273.15))
    weather3_label4.config(text=data["main"]["pressure"])




win = Tk()
win.title("Weather Information")
win.config(bg="lightblue")
win.geometry("600x600")
name_label=Label(win,text="Weather Information",
                 font=("Time New Roman",30,"bold"))
name_label.place(x=83,y=50,height=50,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Weather Information",values=list_name,
                 font=("Time New Roman",20,"bold"),textvariable=city_name)

com.place(x=83,y=120,height=50,width=450)

weather_label=Label(win,text="Weather Climate",
                 font=("Time New Roman",17 ))
weather_label.place(x=83,y=260,height=50,width=230)

weather_label1=Label(win,text="",
                 font=("Time New Roman",17 ))
weather_label1.place(x=330,y=260,height=50,width=200)


weather1_label=Label(win,text="Weather Description",
                 font=("Time New Roman",17))
weather1_label.place(x=83,y=330,height=50,width=230)

weather1_label2=Label(win,text="",
                 font=("Time New Roman",17))
weather1_label2.place(x=330,y=330,height=50,width=200)


weather2_label=Label(win,text="Temperature",
                 font=("Time New Roman",17))
weather2_label.place(x=83,y=400,height=50,width=230)

weather2_label3=Label(win,text="",
                 font=("Time New Roman",17))
weather2_label3.place(x=330,y=400,height=50,width=200)


weather3_label=Label(win,text="Pressure",
                 font=("Time New Roman",17))
weather3_label.place(x=83,y=470,height=50,width=230)

weather3_label4=Label(win,text="",
                 font=("Time New Roman",17))
weather3_label4.place(x=330,y=470,height=50,width=200)


done_button=Button(win,text="Done",
                 font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(x=250,y=190,height=50,width=100)

win.mainloop()