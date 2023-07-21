import PySimpleGUI as gui
# GUI
def gui_table():
    infotable = []
    head = ['ID','Product Name','Quantity','Price']
    gui.theme("HotDogStand")
    #WINDOW TO GET INPUT ID AND QUANTITY
    layout = [[gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False)],
            [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False)],
            [gui.Button("ADD"), gui.Exit()],
            [gui.Table(values = infotable, headings = head, key = "tablebill")]
        ]
    window = gui.Window("KINDLY ENTER", layout)
    while True:
        event, values = window.read()
        
        if event == "ADD":
            
            data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            price = int(values["QTY"]) * int(data[int(values["ID"])][2])
            infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],price])
            window["tablebill"].update(values = infotable)

        if event in (gui.WIN_CLOSED, "Exit"):
            break   
            # DATA IS table
            #layout = [
            #   [gui.Table(values = infotable, headings = head)],
            #    [gui.Button("Exit")]
            #    ]
            #window = gui.Window("BILL",layout)
            #while True:
            #   event , values = window.read()
            #    if event == "Exit" or event == gui.WIN_CLOSED:
            #        break
            #window.close()
    window.close()
 
gui_table()

