import PySimpleGUI as sg

#create window with title w have a method like Window
#want to specify the layout

# sg.Window(title="hello world",layout=[[]],margins=(100,50)).read()

layout=[
    [sg.Text("Hello World!!!")],
    [sg.Button("click Here")]
]

# create window

window=sg.Window("frame",layout)

#if we click ClickHEre event(button take as event)
while True:
    event,values =window.read()
    if event == "click Here" or event == sg.WIN_CLOSED:
        break
    
window.close()
