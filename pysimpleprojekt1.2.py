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
            price = int(values["QTY"]) * int(data[int(values["ID"])][2])
            price2.append(price1)
            infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],price])
            window["tablebill"].update(values = infotable)

        price = 0
        for i in price2:
            price+=i
        window["p"].update(price)
        
        if event in (gui.WIN_CLOSED, "Exit"):
            break
    window.close()
 
gui_table()

