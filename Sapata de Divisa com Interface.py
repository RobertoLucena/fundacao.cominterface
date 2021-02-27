import PySimpleGUI as sg
import math

# Define the window's contents
layout = [[sg.Text("PROGRAMA DE OTIMIZAÇÃO DE SAPATAS DE DIVISA")],
          [sg.Text("Qual a Dimensão do Lado A (maior lado) em m?"), sg.Input(key='LadoA', size=(5, 1))],
          [sg.Text("Qual a Dimensão do Lado B (maior lado) em m?"), sg.Input(key='LadoB', size=(5, 1))],
          [sg.Text("O Valor calculado para o Lado A foi de: "), sg.Text(size=(5, 1), key='ResultadoA'), sg.Text("m", size=(2, 1))],
          [sg.Text("O Valor calculado para o Lado A foi de: "), sg.Text(size=(5, 1), key='ResultadoB'), sg.Text("m", size=(2, 1))],
          [sg.Button('CALCULAR'), sg.Button('SAIR')]]

# Create the window
window = sg.Window('PROGRAMA DE OTIMIZAÇÃO DE SAPATAS DE DIVISA', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'SAIR':
        break
    # Output a message to the window
    if event == 'CALCULAR':
        LadoA = float(values['LadoA'])
        LadoB = float(values['LadoB'])
        area = LadoB * LadoA
        ResA = math.sqrt(area/2)
        ResB = ResA*2
        RA = round(ResA, 3)
        RB = round(ResB, 3)
        window['ResultadoA'].update(RA)
        window['ResultadoB'].update(RB)

# Finish up by removing from the screen
window.close()