from tkinter import*
from PIL import ImageTk, Image
from tkinter import font


root = Tk()
root.title("BikeBreeze")
root.geometry("1100x620")
root.resizable(FALSE, FALSE)
root.config(bg="orange1")

win = Label(root, text="LET'S UPLOAD THE IMAGE", fg="black", bg="orange1", font="Times 20 bold")
win.place(x=75, y=140)

#create a frame in Tk window()
frame = Frame(root, width=450, height=500, bg="white")
frame.place(x=600, y=80)

#pass a label in frame
label = Label(frame, text="Upload your Bikes", bg="White", fg="Blue", font="Times 22 bold")
label.place(x=80, y=20)

#image 
for_bike = Image.open('bike.png')
bike_height = 260
bike_width =350
resize_bike = for_bike.resize((bike_width, bike_height), Image.LANCZOS)
bikeImage = ImageTk.PhotoImage(resize_bike)
bike_label = Label(root, text="Bike", image=bikeImage)
bike_label.image = bikeImage
bike_label.place(x=80,y=200)

#button 
button = Button(root, text="Upload Image", bg="Skyblue", fg="black", width=15, borderwidth=2, font="Times 18 bold")
button.place(x=140, y=480)

#create a label and entry widget for bike name
bike=Label(frame, text="BikeName",bg="white", fg="black", font="Courier 14 bold")
bike.place(x=15, y=80)
bike_name = Entry(frame, width=20, borderwidth=3, font="Courier 14 bold")
bike_name.place(x=140, y=80)

#create a label and entry widget for Bike Number
bike1 = Label(frame, text="BikeNo", fg="black", bg="white", font="Courier 14 bold")
bike1.place(x=15, y=125)
bike1_no =  Entry(frame, width=20, borderwidth=3, font="Courier 14 bold")
bike1_no.place(x=140, y=125)

#create a label and entry widget for phone number
phone = Label(frame, text="PhoneNo", fg="black", bg="white", font="Courier 14 bold")
phone.place(x=15, y=170)
phone_no = Entry(frame, width=20, borderwidth=3, font="Courier 14 bold")
phone_no.place(x=140, y=170)

#create label and entry widget for Bike module
bike_mod = Label(frame, text="Module", fg="black", bg="white", font="Courier 14 bold")
bike_mod.place(x=15, y=215)
bike_module = Entry(frame, width=20, borderwidth=3, font="Courier 14 bold")
bike_module.place(x=140, y=215)

#create label and entry widget for Bike Price
bikeprice = Label(frame, text="Price", fg="black", bg="white", font="Courier 14 bold")
bikeprice.place(x=15, y=260)
bike_price = Entry(frame, width=20, borderwidth=3, font="Courier 14 bold")
bike_price.place(x=140, y=260)

#create label and entry widget for Bike Pickup Location
pickup_location = Label(frame, text="Location", fg="black", bg="white", font="Courier 14 bold")
pickup_location.place(x=15, y=305)
bike_pickup_location = Entry(frame, width=20, borderwidth=3, font="Courier 14 bold")
bike_pickup_location.place(x=140, y=305)

#create label and entry widget for Bike Conditon
conditon = Label(frame, text="Conditon", fg="black", bg="white", font="Courier 14 bold")
conditon.place(x=15, y=350)
bike_conditon = Entry(frame, width=20, borderwidth=3, font="Courier 14 bold")
bike_conditon.place(x=140, y=350)

btn = Button(frame, text="Post", fg="white", width=10, borderwidth=2, bg="Blue", font="Times 22 bold")
btn.place(x=160, y=420)

root.mainloop()