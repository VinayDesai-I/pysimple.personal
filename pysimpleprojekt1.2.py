import PySimpleGUI as gui

def gui_table():
    price2 = []
    infotable = []
    head = ['ID','Product Name','Quantity','Price']

    gui.theme("DarkAmber")

    layout = [[gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False)],
            [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False)],
            [gui.Button("Add")],
            [gui.Table(values =  infotable, headings = head, key = "tablebill", justification = "centre")],
            [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
            [gui.Exit()]
        ]
    
    window = gui.Window("KINDLY ENTER", layout)
    
    while True:
        event, values = window.read()
        
        if event == "Add":
            
            data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            price1 = int(values["QTY"]) * int(data[int(values["ID"])][2])
            price2.append(price1)
            infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],price1])
            window["tablebill"].update(values = infotable)

        price = 0
        for i in price2:
            price+=i
        window["p"].update(price)
        
        if event in (gui.WIN_CLOSED, "Exit"):
            break
    window.close()
 
gui_table()

import PySimpleGUI as gui
import time 
import mysql.connector as c
cnc = c.connect(user= "root", host="localhost", password="password", database="project")
if cnc.is_connected():
    print("Connected to DB")
cur = cnc.cursor()

def gui_propmt2():

    #MAIN THINGS
    # data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
    cur.execute("SELECT * FROM ITEMTEST ORDER BY ID;")
    data = cur.fetchall()
    price2 = []
    infotablegetinfo = []
    infotablebill = []
    infotablestockadd = []
    infotablestockupd = []
    infotablestockdel = []
    infotablelistitems = []
    head = ['ID','Item Name','Quantity','Price']
    head1 = ['ID','Item Name','Quantity','Price' 'Date']
    price1 = 0
    
    # Theme
    gui.theme("DarkAmber")
    
    # DIFFERENT LAYOUTS
    
    #MAIN MENU
    layout_menu = [ [gui.Text("!!Welcome To Mavika store!!", size = (20, 1), font = ("Cooper Black", 20), expand_x = True, justification = "centre")],
                    [gui.Image(filename = "cat.png", size = (150, 220),  expand_x = True, expand_y = True)],
                    [gui.Button("User"), gui.Button("Admin")]
    ]
    
    #ADMIN LOGIN
    layout_adminlogin = [ [gui.Text("Admin Login Window", expand_x = "True", justification = "centre")],
                          [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "admname", do_not_clear = False)],
                          [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "admpassword", do_not_clear = False)],
                          [gui.Button("Enter"), gui.Button("Back", key = "back_userlogin") ,gui.Button("Register (New User)")]
    ]
    
    #ADMIN REGISTRATION 
    layout_adminreg = [ [gui.Text("Admin Registration Window", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "admregname", do_not_clear = False)],
                        [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "admregpassword", do_not_clear = False)],
                        [gui.Text("Enter Code", size = (12,1)), gui.Input(key = "admregsec", do_not_clear = False)],
                        [gui.Button("Enter"), gui.Button("Back", key = "back_admreg")]
    ]

    #ADMIN MENU
    layout_menu = [ [gui.Table(values =  infotablelistitems, headings = head, key = "tableitems", justification = "centre")],
                    [gui.Button("Item Information"), gui.Button("Restock Items"), gui.Button("Bills"),gui.Button("Exit")]
    ]
    
    #USER GET INFORMATION 
    layout_getinfo = [ [gui.Text("Item Information Window", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "ITEMID", do_not_clear = False)],
                        [gui.Text("Enter Item Name", size = (12,1)), gui.Input(key = "ITEMNAME", do_not_clear = False)],
                        [gui.Button("Search")],
                        [gui.Table(values =  infotablegetinfo, headings = head1, key = "infotablegetinfo", justification = "centre")],
                        [gui.Button("Back", key = "back_getinfo")]
    ]

    #USER LOGIN
    layout_userlogin = [ [gui.Text("User Login Window", expand_x = "True", justification = "centre")],
                         [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "username", do_not_clear = False)],
                         [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "userpassword", do_not_clear = False)],
                         [gui.Button("Enter"), gui.Button("Back", key = "back_userlogin") ,gui.Button("Register (New User)")]
    ]

    #USER REGISTRATION 
    layout_userreg = [ [gui.Text("Welcome to User Registration", expand_x = "True", justification = "centre")],
                       [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "userregname", do_not_clear = False)],
                       [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "userregpassword", do_not_clear = False)],
                       [gui.Text("Enter Address", size = (12,1)), gui.Input(key = "useraddress", do_not_clear = False)],
                       [gui.Text("Enter Phone No.", size = (12,1)), gui.Input(key = "userno", do_not_clear = False)],
                       [gui.Button("Enter"), gui.Button("Back", key = "back_userreg")]
    ]

    #USER MENU 
    layout_usermenu = [ [gui.Text("!!Welcome To Mavika Store!!", size = (20, 1), font = ("Cooper Black", 20), expand_x = True, justification = "centre")],
                        [gui.Image(filename = "cat.png", size = (150, 220),  expand_x = True, expand_y = True)],
                        [gui.Button("List Of Items"), gui.Button("Get Information"), gui.Button("Self Check-Out"), gui.Button("Exit")]
    ]

    #USER GET INFORMATION 
    layout_getinfo1 = [ [gui.Text("Welcome to Get Information", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter either of them or both", size = (10,1), justification = "right")],
                        [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "ITEMID", do_not_clear = False)],
                        [gui.Text("Enter Item Name", size = (12,1)), gui.Input(key = "ITEMNAME", do_not_clear = False)],
                        [gui.Button("Search")],
                        [gui.Table(values =  infotablegetinfo, headings = head, key = "infotablegetinfo", justification = "centre")],
                        [gui.Button("Back", key = "back_getinfo1")]
    ]

    #USER LIST of ITEMS 
    layout_listitems = [ [gui.Text("Welcome to List of Items", expand_x = "True", justification = "centre")],
                         [gui.Table(values =  infotablelistitems, headings = head, key = "tableitems", justification = "centre")],
                         [gui.Button("Back", key = "back_listitems")]
    ]

    #USER SELF CHECKOUT 
    layout_selfcheckout = [ [gui.Text("Welcome to Self Check-Out", expand_x = "True", justification = "centre")],
                            [gui.Text("Enter ID", size = (10,1)), gui.Input(key = "id", do_not_clear = False, justification = "left")],
                            [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "qty", do_not_clear = False, justification = "left")],
                            [gui.Button("Add")],
                            [gui.Table(values =  infotablebill, headings = head, key = "tablebill", justification = "centre")],
                            [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
                            [gui.Button("Back", key = "back_selfcheckout"), gui.Button("Place Delivery", key = "delivery_selfcheckout")]
    ]  
