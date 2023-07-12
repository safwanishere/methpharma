import tkinter as tk
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# ~ Home page window ~
mainwindow = Tk()
mainwindow.geometry("1350x670")
mainwindow.config()
mainwindow.title("Meth Pharma Home Page")
mainwindow.resizable(False, False)

mainbg = PhotoImage(file="Images\\home.png")
bg = Label(mainwindow, image=mainbg).place(x=0, y=0)


# ~ header widgets ~

#  ---  header button functions  ---

# Sign in Page
def signinopt():
    signinwindow = Toplevel(mainwindow)
    signinwindow.geometry("800x500")
    signinwindow.title("Sign in page")
    signinwindow.configure(bg="black")
    maintext = Label(signinwindow, text="Sign In", font=("Oswald",50), bg="black", fg="white")
    frame = Frame(signinwindow, bg="black")

    def loginpage():
        #loginwindow = Toplevel(signinwindow)
        signinwindow.destroy()
        loginwindow = Tk()
        loginwindow.geometry("800x500")
        loginwindow.title("Home Page")
        loginwindow.configure(background="black")

        def logcheck():
            name=str(logentry1.get())
            pas=str(logentry2.get())
            a = sql.connect(host="localhost", user="root", password="safwan", database="userdata")
            curs = a.cursor()
            curs.execute(f"select*from users;")
            b=curs.fetchall()
            a.commit()

            usernames=[]
            passwords=[]
            for i in b:
                x=i[1]
                y=i[0]
                usernames.append(y)
                passwords.append(x)
            if f'{name}' in usernames:
                if f'{pas}' in passwords:
                    for i in b:
                        for s in i[0]:
                            if i[1]==pas:
                                if name==i[0]:
                                    messagebox.showinfo(title="notification", message="Logged In successfully !")
                                    loginwindow.destroy()
                                    break
                                else:
                                    messagebox.showerror("error","Incorrect information")
                                    loginwindow.destroy()
                else:
                    messagebox.showerror("error","Incorrect password")
                    loginwindow.destroy()
            else:
                messagebox.showerror("error","Unknown username")
                loginwindow.destroy()


        label = Label(loginwindow, text="Login", font=("Arial",50), bg="black", fg="white").place(x=320, y=45)
        ulabel = Label(loginwindow, text="Username : ", font=("Arial",16), bg="black", fg="white").place(x=180, y=210)
        plabel = Label(loginwindow, text="Password : ", font=("Arial",16), bg="black", fg="white").place(x=180, y=240)
        logentry1 = Entry(loginwindow, bg="white", fg="black", width=50)
        logentry1.place(x=320, y=215)
        logentry2 = Entry(loginwindow, bg="white", fg="black", width=50)
        logentry2.place(x=320, y=245)
        logbut = Button(loginwindow, text="Done", bg="white", activeb="red", font=("Arial",12),
        activef="white",width=14, height=1, command=logcheck).place(x=330, y=335)



    def input():
        usernameval = str(entry1.get())
        passwordval = str(entry2.get())
        a = sql.connect(host="localhost", user="root", password="safwan", database="userdata")
        curs = a.cursor()
        curs.execute(f"insert into users values('{usernameval}','{passwordval}');")
        messagebox.showinfo("Notification", "Signed in your information successfully into the database!")
        signinwindow.destroy()
        a.commit()

    username = Label(frame, text=" Username  : ", font=("Arial",16), bg="black", fg="white")
    password = Label(frame, text="Password : ", font=("Arial",16), bg="black", fg="white")
    entry1 = Entry(frame, bg="white", fg="black", width=50)
    entry2 = Entry(frame, bg="white", fg="black", width=50)
    donebutton = Button(signinwindow, text="Done", bg="white", activeb="red", font=("Arial",12), activef="white",width=14, height=1, command=input)

    third = Frame(signinwindow, bg="black")
    logintext = Label(third, text="Already have an account? Try logging in ", font=("Arial", 16), bg="black", fg="white")
    loginbutton = Button(third, text="login", bg='black', fg="grey", activeb="black", font="Arial", activef="blue",
                         width=5, height=1, command=loginpage)

    maintext.pack(padx=40, pady=40)
    frame.pack(pady=50)
    username.grid(column=0, row=0)
    password.grid(column=0, row=1)
    entry1.grid(column=1,row=0)
    entry2.grid(column=1, row=1)
    donebutton.place(x=330, y=325)

    third.place(x=200, y=420)
    logintext.grid(column=0, row=0)
    loginbutton.grid(column=1, row=0)



# ---  Image imports  ---
headercolor="#4D4C4C"
backcolor="#323232"
teal="#03DAC5"
blue="#6200EE"
purple="#BB86FC"
sbar = PhotoImage(file="Images\\searchbar.png")
searchicon = PhotoImage(file="Images\\searchicon.png")
carticon = PhotoImage(file="Images\\carticon.png")
cartfont = PhotoImage(file="Images\\cartlabel.png")
usericon = PhotoImage(file="Images\\usericon.png")
userfont = PhotoImage(file="Images\\userlabel.png")
logoimg = PhotoImage(file="Images\\logo.png")
cartbg = PhotoImage(file="Images\\cartbg.png")

# ~ Cart Page ~
cart=[]
cartprices=[]

def cartclick():
    cartpage = Toplevel(mainwindow)
    cartpage.geometry("1000x550")
    cartpage.title("Your Cart")
    bg = Label(cartpage, image=cartbg).place(x=0, y=0)
    mainlabel = Label(cartpage, text=".                           Checkout                           .", fg="white", bg="black", font=("Arial",26))
    mainlabel.pack(padx=150, pady=35, anchor="n")

    for i in cart:
        lab = Label(cartpage, text=f"{i}", bg="black", fg="white", font=("Arial",12)).pack(padx=50, pady=10)

    space = Label(cartpage, text="--------------------------------------", bg="black", fg="white", font=("Arial",12)).pack(padx=50, pady=10)
    total = Label(cartpage, text=f"Total    -    {sum(cartprices)}", bg="black", fg="white", font=("Arial",12)).pack(padx=50, pady=10)
    def checkout():
        answer = messagebox.askyesno("Checkout", "would you like to place the order?")
        if answer:
            cartpage.destroy()
            cart.clear()
            cartprices.clear()
            messagebox.showinfo("notification","order placed, thanks for shopping!")
        else:
            cartpage.destroy()
            messagebox.showinfo("notification" ,"order cancelled")
    checkoutbutton = Button(cartpage, bg=blue, fg="white", text="Checkout", command=checkout, height=1, width=30).pack(padx=50, pady=30)


# ~ Search functionality ~


# def search():
#     query = str(searchbar.get())
#     for i in productsobj:
#         if query == str(i):
#             i.searchresult()


# ---  widget definitions ---
headerframe = Frame(mainwindow, bg="grey20").place(x=0, y=0)
searchbar = Entry(headerframe, font=("Arial",18), width=30, bg="#03DAC5")
searchbar.place(x=170, y=17)
searchbutton = Button(headerframe, borderwidth=0, bg="#4D4C4C", image=searchicon, activeb=headercolor).place(x=580, y=12)
cartlabel = Label(headerframe, image=cartfont, bg="#4D4C4C").place(x=950, y=12)
cartbutton = Button(headerframe, borderwidth=0, bg="#4D4C4C", image=carticon, activeb=headercolor, command=cartclick).place(x=1095, y=12)
userlabel = Label(headerframe, image=userfont, bg="#4D4C4C").place(x=1200, y=12)
userbutton = Button(headerframe, borderwidth=0, bg="#4D4C4C", image=usericon, command=signinopt, activeb=headercolor).place(x=1300, y=12)

# ~ Home Page items layout ~

# --- products image imports ---
medsimg = PhotoImage(file="Images\\meds.png")
oneimg = PhotoImage(file="Images\\one.png")
twoimg = PhotoImage(file="Images\\two.png")
threeimg = PhotoImage(file="Images\\three.png")
chemimg = PhotoImage(file="Images\\chem.png")
tylenolimg = PhotoImage(file="Images\\tylenol.png")
paracetamolimg = PhotoImage(file="Images\\paracetamol.png")
neosporinimg = PhotoImage(file="Images\\neosporin.png")
vaporubimg = PhotoImage(file="Images\\vaporub.png")
vicksimg = PhotoImage(file="Images\\vicks.png")
petimg = PhotoImage(file="Images\\pet.png")
benadrylimg = PhotoImage(file="Images\\benadryl.png")
aspirinimg = PhotoImage(file="Images\\aspirin.png")
isotineimg = PhotoImage(file="Images\\isotine.png")
dettolimg = PhotoImage(file="Images\\dettol.png")
constimg = PhotoImage(file="Images\\const.png")
enoimg = PhotoImage(file="Images\\eno.png")

acteoneimg = PhotoImage(file="Images\\acetone.png")
ammoniumchlorideimg = PhotoImage(file="Images\\ammonium chloride.png")
citricacidimg = PhotoImage(file="Images\\citric acid.png")
cupricsulphateimg = PhotoImage(file="Images\\cupric sulphate.png")
ethyllabsolimg = PhotoImage(file="Images\\ethyl labsol.png")
potassiumchromateimg = PhotoImage(file="Images\\potassium chromate.png")
galliumimg = PhotoImage(file="Images\\gallium.png")
indiumimg = PhotoImage(file="Images\\indium.png")
mercuryimg = PhotoImage(file="Images\\mercury.png")
tinimg = PhotoImage(file="Images\\tin.png")
titaniumimg = PhotoImage(file="Images\\titanium.png")
nickelimg = PhotoImage(file="Images\\nickel.png")
hclimg = PhotoImage(file="Images\\hcl.png")
isopropylalcoholimg = PhotoImage(file="Images\\isopropyl alcohol.png")
leadphosphateimg = PhotoImage(file="Images\\lead phosphate.png")
potasiumnitrateimg = PhotoImage(file="Images\\potassium nitrate.png")
potassiumpermanganateimg = PhotoImage(file="Images\\potassium permanganate.png")
calciumchlorideimg = PhotoImage(file="Images\\calcium chloride.png")

hometitleimg = PhotoImage(file="Images\\hometitle.png")
homeparaimg = PhotoImage(file="Images\\homepara.png")
devsimg = PhotoImage(file="Images\\devs.png")

# --- product class for cart and search functions ---

class products:

    def __init__(self, name, price, img):
        self.name = name
        self.price = price
        self.img = img

    def upload(self):
        cart.append(f"{self.name}    -   {self.price}")
        cartprices.append(int(self.price))
        messagebox.showinfo("notification", "Item added to cart successfully!")

    def getprice(self):
        print(self.price)

    def searchresult(self):
        searchframe = Frame(mainwindow, height=670, width=1290, bg=backcolor)
        medone.place(x=10000, y=10000)
        medtwo.place(x=10000, y=10000)
        chemtwo.place(x=10000, y=10000)
        chemthree.place(x=10000, y=10000)
        chemone.place(x=10000, y=10000)
        searchframe.place(x=72, y=66.5)
        selflimg = Label(mainwindow, image=self.img).place(x=100, y=80)
        selflabel = Label(mainwindow, text=self.name, bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=250)
        selfbutton = Button(mainwindow, text="ADD", bg=blue, fg="white", command=self.upload).place(x=380, y=250)


# --- Product pages widgets ---

homepage = Frame(mainwindow, height=670, width=1290, bg=backcolor)
homepage.place(x=72, y=66.5)
hometitle = Label(homepage, image=hometitleimg, bg=backcolor).place(x=480, y=40)
homepara = Label(homepage, image=homeparaimg, bg=backcolor).place(x=100, y=80)
devs = Label(homepage, image=devsimg, bg=backcolor).place(x=100, y=240)

def homeclick():
    medone.place(x=10000, y=10000)
    medtwo.place(x=10000, y=10000)
    chemone.place(x=10000, y=10000)
    chemtwo.place(x=10000, y=10000)
    chemthree.place(x=10000, y=10000)
    homepage.place(x=72, y=66.5)

logo = Button(headerframe, image=logoimg, bg=headercolor, command=homeclick, borderwidth=0, activeb=headercolor).place(x=15, y=10)


tylobj = products("Tylenol tablets", 350, tylenolimg)
parobj = products("Paracetamol tablets", 100, paracetamolimg)
neoobj = products("Neosporin Ointment", 50, neosporinimg)
aspobj = products("Aspirin tablets", 120, aspirinimg)
petobj = products("Pet Safa tablets", 289, petimg)
actobj = products("Vicks Action 500 tablets", 52, vicksimg)

medone = Frame(mainwindow, height=670, width=1290, bg=backcolor)
tylenol = Label(medone, image=tylenolimg).place(x=100, y=80)
tyllabel = Label(medone, text="20 tablets - Rs 350", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=250)
tylcart = Button(medone, text="ADD", bg=blue, fg="white", command=tylobj.upload).place(x=380, y=250)

paracetamol = Label(medone, image=paracetamolimg).place(x=510, y=80)
parlabel = Label(medone, text="12 tablets - Rs 100", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=250)
parcart = Button(medone, text="ADD", bg=blue, fg="white", command=parobj.upload).place(x=790, y=250)

neosporin = Label(medone, image=neosporinimg).place(x=920, y=80)
neolabel = Label(medone, text="Ointment - Rs 50", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=250)
neocart = Button(medone, text="ADD", bg=blue, fg="white", command=neoobj.upload).place(x=1200, y=250)

aspirin = Label(medone, image=aspirinimg).place(x=100, y=340)
asplabel = Label(medone, text="10 tablets - Rs 120", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=510)
aspcart = Button(medone, text="ADD", bg=blue, fg="white", command=aspobj.upload).place(x=380, y=510)

pet = Label(medone, image=petimg).place(x=510, y=340)
petlabel = Label(medone, text="pack of 3 - Rs 289", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=510)
petcart = Button(medone, text="ADD", bg=blue, fg="white", command=petobj.upload).place(x=790, y=510)

vicks = Label(medone, image=vicksimg).place(x=920, y=340)
actlabel = Label(medone, text="10 tablets - Rs 52", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=510)
actcart = Button(medone, text="ADD", bg=blue, fg="white", command=actobj.upload).place(x=1200, y=510)

def showmedone():
    medtwo.place(x=10000, y=10000)
    chemone.place(x=10000, y=10000)
    chemtwo.place(x=10000, y=10000)
    chemthree.place(x=10000, y=10000)
    medone.place(x=72, y=66.5)

benobj = products("Benadryl capsules", 90, benadrylimg)
vapobj = products("Vicks VapoRub", 75, vaporubimg)
conobj = products("Constipation relief syrup", 399, constimg)
detobj = products("Dettol hand sanitizer", 295, dettolimg)
isoobj = products("Isotine eyedrops", 60, isotineimg)
enoobj = products("Eno sachets", 105, enoimg)

medtwo = Frame(mainwindow, height=670, width=1290, bg=backcolor)
benadryl = Label(medtwo, image=benadrylimg).place(x=100, y=80)
benlabel = Label(medtwo, text="24 gels - Rs 90", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=250)
bencart = Button(medtwo, text="ADD", bg=blue, fg="white", command=benobj.upload).place(x=380, y=250)

vaporub = Label(medtwo, image=vaporubimg).place(x=510, y=80)
vaplabel = Label(medtwo, text="25 ml bottle - Rs 75", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=250)
vapcart = Button(medtwo, text="ADD", bg=blue, fg="white", command=vapobj.upload).place(x=790, y=250)

const = Label(medtwo, image=constimg).place(x=920, y=80)
conlabel = Label(medtwo, text="500 ml - Rs 399", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=250)
concart = Button(medtwo, text="ADD", bg=blue, fg="white", command=conobj.upload).place(x=1200, y=250)

dettol = Label(medtwo, image=dettolimg).place(x=100, y=340)
detlabel = Label(medtwo, text="pack of 3 - Rs 295", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=510)
detcart = Button(medtwo, text="ADD", bg=blue, fg="white", command=detobj.upload).place(x=380, y=510)

isotine = Label(medtwo, image=isotineimg).place(x=510, y=340)
isolabel = Label(medtwo, text="10 ml dropper - Rs 60", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=510)
isocart = Button(medtwo, text="ADD", bg=blue, fg="white", command=isoobj.upload).place(x=790, y=510)

eno = Label(medtwo, image=enoimg).place(x=920, y=340)
enolabel = Label(medtwo, text="box of 15 sachets - Rs 105", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=510)
enocart = Button(medtwo, text="ADD", bg=blue, fg="white", command=enoobj.upload).place(x=1200, y=510)

def showmedtwo():
    medone.place(x=10000, y=10000)
    chemone.place(x=10000, y=10000)
    chemtwo.place(x=10000, y=10000)
    chemthree.place(x=10000, y=10000)
    medtwo.place(x=72, y=66.5)

tinobj = products("Tin nuggets", 3749, tinimg)
titobj = products("Titanium cube", 1200, titaniumimg)
nicobj = products("Nickel cube", 1499, nickelimg)
merobj = products("Liquid Mercury", 599, mercuryimg)
galobj = products("Gallium metal", 6999, galliumimg)
indobj = products("Indium metal", 799, indiumimg)

chemone = Frame(mainwindow, height=670, width=1290, bg=backcolor)
tin = Label(chemone, image=tinimg).place(x=100, y=80)
tinlabel = Label(chemone, text="500 gm - Rs 3749", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=250)
tincart = Button(chemone, text="ADD", bg=blue, fg="white", command=tinobj.upload).place(x=380, y=250)

titanium = Label(chemone, image=titaniumimg).place(x=510, y=80)
titlabel = Label(chemone, text="25 mm cube - Rs 1200", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=250)
titcart = Button(chemone, text="ADD", bg=blue, fg="white", command=titobj.upload).place(x=790, y=250)

nickel = Label(chemone, image=nickelimg).place(x=920, y=80)
niclabel = Label(chemone, text="25 mm cube - Rs 1499", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=250)
niccart = Button(chemone, text="ADD", bg=blue, fg="white", command=nicobj.upload).place(x=1200, y=250)

mercury = Label(chemone, image=mercuryimg).place(x=100, y=340)
merlabel = Label(chemone, text="25 gm - Rs 599", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=510)
mercart = Button(chemone, text="ADD", bg=blue, fg="white", command=merobj.upload).place(x=380, y=510)

gallium = Label(chemone, image=galliumimg).place(x=510, y=340)
gallabel = Label(chemone, text="50 gm - Rs 6999", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=510)
galcart = Button(chemone, text="ADD", bg=blue, fg="white", command=galobj.upload).place(x=790, y=510)

indium = Label(chemone, image=indiumimg).place(x=920, y=340)
indlabel = Label(chemone, text="50 gm - Rs 799", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=510)
indcart = Button(chemone, text="ADD", bg=blue, fg="white", command=indobj.upload).place(x=1200, y=510)

def showchemone():
    medone.place(x=10000, y=10000)
    medtwo.place(x=10000, y=10000)
    chemtwo.place(x=10000, y=10000)
    chemthree.place(x=10000, y=10000)
    chemone.place(x=72, y=66.5)

aceobj = products("Acetone", 300, acteoneimg)
citobj = products("Citric acid", 240, citricacidimg)
calobj = products("Calcium chloride", 314, calciumchlorideimg)
potcobj = products("Potassium chromate", 1125, potassiumchromateimg)
potnobj = products("Potassium nitrate", 169, potasiumnitrateimg)
potpobj = products("Potassium permanganate", 300, potassiumpermanganateimg)

chemtwo = Frame(mainwindow, height=670, width=1290, bg=backcolor)
acetone = Label(chemtwo, image=acteoneimg).place(x=100, y=80)
acelabel = Label(chemtwo, text="500 ml - Rs 300", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=250)
acecart = Button(chemtwo, text="ADD", bg=blue, fg="white", command=aceobj.upload).place(x=380, y=250)

citricacid = Label(chemtwo, image=citricacidimg).place(x=510, y=80)
citlabel = Label(chemtwo, text="1000 gm - Rs 240", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=250)
citcart = Button(chemtwo, text="ADD", bg=blue, fg="white", command=citobj.upload).place(x=790, y=250)

calciumchloride = Label(chemtwo, image=calciumchlorideimg).place(x=920, y=80)
callabel = Label(chemtwo, text="500 gm - Rs 314", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=250)
calcart = Button(chemtwo, text="ADD", bg=blue, fg="white", command=calobj.upload).place(x=1200, y=250)

potassiumchromate = Label(chemtwo, image=potassiumchromateimg).place(x=100, y=340)
potclabel = Label(chemtwo, text="500 gm - Rs 1125", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=510)
potccart = Button(chemtwo, text="ADD", bg=blue, fg="white", command=potcobj.upload).place(x=380, y=510)

potasiumnitrate = Label(chemtwo, image=potasiumnitrateimg).place(x=510, y=340)
potnlabel = Label(chemtwo, text="100 gm - Rs 169", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=510)
potncart = Button(chemtwo, text="ADD", bg=blue, fg="white", command=potnobj.upload).place(x=790, y=510)

potassiumpermanganate = Label(chemtwo, image=potassiumpermanganateimg).place(x=920, y=340)
potplabel = Label(chemtwo, text="200 gm - Rs 300", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=510)
potpcart = Button(chemtwo, text="ADD", bg=blue, fg="white", command=potpobj.upload).place(x=1200, y=510)

def showchemtwo():
    medone.place(x=10000, y=10000)
    medtwo.place(x=10000, y=10000)
    chemone.place(x=10000, y=10000)
    chemthree.place(x=10000, y=10000)
    chemtwo.place(x=72, y=66.5)

ammobj = products("Ammonium chloride", 439, ammoniumchlorideimg)
cupobj = products("Cupric acid", 652, cupricsulphateimg)
ethobj = products("Ethyl labsol", 1111, ethyllabsolimg)
hclobj = products("Hydrchloric acid", 70, hclimg)
isoobj = products("Isopropyl alcohol", 462, isopropylalcoholimg)
leaobj = products("Lead phosphate", 1128, leadphosphateimg)

chemthree = Frame(mainwindow, height=670, width=1290, bg=backcolor)
ammoniumchloride = Label(chemthree, image=ammoniumchlorideimg).place(x=100, y=80)
ammlabel = Label(chemthree, text="500 gm - Rs 439", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=250)
ammcart = Button(chemthree, text="ADD", bg=blue, fg="white", command=ammobj.upload).place(x=380, y=250)

cupricsulphate = Label(chemthree, image=cupricsulphateimg).place(x=510, y=80)
cuplabel = Label(chemthree, text="500 gm - Rs 652", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=250)
cupcart = Button(chemthree, text="ADD", bg=blue, fg="white", command=cupobj.upload).place(x=790, y=250)

ethyllabsol = Label(chemthree, image=ethyllabsolimg).place(x=920, y=80)
ethlabel = Label(chemthree, text="5 lt - Rs 1111", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=250)
ethcart = Button(chemthree, text="ADD", bg=blue, fg="white", command=ethobj.upload).place(x=1200, y=250)

hcl = Label(chemthree, image=hclimg).place(x=100, y=340)
hcllabel = Label(chemthree, text="1000 gm - Rs 70", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=100, y=510)
hclcart = Button(chemthree, text="ADD", bg=blue, fg="white", command=hclobj.upload).place(x=380, y=510)

isopropylalcohol = Label(chemthree, image=isopropylalcoholimg).place(x=510, y=340)
isolabel = Label(chemthree, text="500 ml - Rs 462", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=510, y=510)
isocart = Button(chemthree, text="ADD", bg=blue, fg="white", command=isoobj.upload).place(x=790, y=510)

leadphosphate = Label(chemthree, image=leadphosphateimg).place(x=920, y=340)
lealabel = Label(chemthree, text="500 gm - Rs 1128", bg=backcolor, fg="white", font=("Oswald", 12)).place(x=920, y=510)
leacart = Button(chemthree, text="ADD", bg=blue, fg="white", command=leaobj.upload).place(x=1200, y=510)

def showchemthree():
    medone.place(x=10000, y=10000)
    medtwo.place(x=10000, y=10000)
    chemone.place(x=10000, y=10000)
    chemtwo.place(x=10000, y=10000)
    chemthree.place(x=72, y=66.5)

options = Frame(mainwindow, height=670, width=70, bg="grey15").place(x=2, y=66.5)
medsicon = Label(options, bg="grey15", image=medsimg).place(x=15, y=100)
medonebutton = Button(options, bg="grey15", image=oneimg, borderwidth=0, activeb="grey15", command=showmedone).place(x=17, y=160)
medtwobutton = Button(options, bg="grey15", image=twoimg, borderwidth=0, activeb="grey15", command=showmedtwo).place(x=17, y=210)
chemicon = Label(options, bg="grey15", image=chemimg).place(x=15, y=350)
chemonebutton = Button(options, bg="grey15", image=oneimg, borderwidth=0, activeb="grey15", command=showchemone).place(x=17, y=410)
chemtwobutton = Button(options, bg="grey15", image=twoimg, borderwidth=0, activeb="grey15", command=showchemtwo).place(x=17, y=460)
chemthreebutton = Button(options, bg="grey15", image=threeimg, borderwidth=0, activeb="grey15", command=showchemthree).place(x=17, y=510)


mainwindow.mainloop()
