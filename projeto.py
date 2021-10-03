import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

sg.theme('DarkBlue12')

arr_valores = [0]

arr_comprados = []

pedidoAcomp = []

def front():
    flayout = [
        [sg.Text('Bem vindo')],
        [sg.Button('Entrar'), sg.Button('Sair')]

    ]

    window = sg.Window('Restaurante Píton', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()

    if button == 'Entrar':
        window.close()
    
    if button == 'Sair':
        window.exit()

def tela_massas():
    massas = ('Macarrão alho e óleo', 'Espaguete', 'Bolonhesa', 'Lasanha')

    layout = [
        [sg.Text('Escolha a Massa')],
        [sg.Text('Macarrão alho e óleo - R$ 15.00')],
        [sg.Text('Espaguete - R$ 25.00')],
        [sg.Text('Bolonhesa - R$ 23.00')],
        [sg.Text('Lasanha - R$ 16.00')],
        [sg.Listbox(massas, size=(20, len(massas)), key='-MASSA-')],
        [sg.Button('Adicionar'), sg.Button('Fechar')]
    ]

    window = sg.Window('Restaurante Píton', layout, element_justification='center')
    

    while True:
        button, values = window.read()
        if button == sg.WIN_CLOSED:
            break
        if button == 'Fechar':
            window.close()
        if button == 'Adicionar':
            if values['-MASSA-'][0] == 'Macarrão alho e óleo':
                arr_valores.append(15)
                arr_comprados.append('Macarrão alho e óleo')
                sg.popup('Você escolheu Macarrão alho e óleo')
            elif values['-MASSA-'][0] == 'Espaguete':
                arr_valores.append(25)
                arr_comprados.append('Espaguete')
                sg.popup('Você escolheu Espaguete')
            elif values['-MASSA-'][0] == 'Bolonhesa':
                arr_valores.append(23)
                arr_comprados.append('Bolonhesa')
                sg.popup('Você escolheu Bolonhesa')
            elif values['-MASSA-'][0] == 'Lasanha':
                arr_valores.append(16)
                arr_comprados.append('Lasanha')
                sg.popup('Você escolheu Lasanha')
            print(arr_valores)
   
def tela_carnes():
    carnes = ('Picanha', 'Contra Filé', 'Fígado', 'Filé de Frango', 'Picadinho')

    layout = [
        [sg.Text('Escolha a Carne')],
        [sg.Text('Picanha - R$ 32.00')],
        [sg.Text('Contra Filé - R$ 25.00')],
        [sg.Text('Fígado - R$ 23.00')],
        [sg.Text('Filé de Frango - R$ 24.00')],
        [sg.Text('Picadinho - R$ 24.00')],
        [sg.Listbox(carnes, size=(20, len(carnes)), key='-CARNE-')],
        [sg.Button('Adicionar'), sg.Button('Fechar')]
    ]

    window = sg.Window('Restaurante Píton', layout, element_justification='center')
    

    while True:
        button, values = window.read()
        if button == sg.WIN_CLOSED:
            break
        if button == 'Fechar':
            window.close()
            tela_acompanhamentos()
        if button == 'Adicionar':
            if values['-CARNE-'][0] == 'Picanha':
                arr_valores.append(32)
                arr_comprados.append('Picanha')
                sg.popup('Você escolheu Picanha')
            elif values['-CARNE-'][0] == 'Contra Filé':
                arr_valores.append(25)
                arr_comprados.append('Contra Filé')
                sg.popup('Você escolheu Contra Filé')
            elif values['-CARNE-'][0] == 'Fígado':
                arr_valores.append(23)
                arr_comprados.append('Fígado')
                sg.popup('Você escolheu Fígado')
            elif values['-CARNE-'][0] == 'Filé de Frango':
                arr_valores.append(24)
                arr_comprados.append('Filé de Frango')
                sg.popup('Você escolheu Filé de Frango')
            elif values['-CARNE-'][0] == 'Picadinho':
                arr_valores.append(24)
                arr_comprados.append('Picadinho')
                sg.popup('Você escolheu Picadinho')
            print(arr_valores)

def tela_acompanhamentos():
    acomp = ('Arroz', 'Feijão', 'Batatas', 'Salada Alface', 'Salada de Tomate', 'Salada de Maionese', 'Farofa')
    cont = 1
    layout = [
        [sg.Text('Escolha até 5 acompanhamentos')],
        [sg.Text('Arroz')],
        [sg.Text('Feijão')],
        [sg.Text('Batatas')],
        [sg.Text('Salada Alface')],
        [sg.Text('Salada de Tomate')],
        [sg.Text('Salada de Maionese')],
        [sg.Text('Farofa')],
        [sg.Listbox(acomp, size=(20, len(acomp)), key='-ACOMP-')],
        [sg.Button('Adicionar')]
    ]

    window = sg.Window('Restaurante Píton', layout, element_justification='center')
    

    while True:
        button, values = window.read()
        if button == sg.WIN_CLOSED:
            break
        if cont >= 5:
            sg.popup("Limite máximo de acompanhamentos atingido")
            window.close()
        if button == 'Adicionar':
            if values['-ACOMP-'][0] == 'Arroz':
                arr_comprados.append('Arroz')
                sg.popup('Você escolheu Arroz. Faltam ', 5-cont, ' acompanhamentos')
            elif values['-ACOMP-'][0] == 'Feijão':
                arr_comprados.append('Feijão')
                sg.popup('Você escolheu Feijão', '. Faltam ', 5-cont, ' acompanhamentos')
            elif values['-ACOMP-'][0] == 'Fígado':
                arr_comprados.append('Batatas')
                sg.popup('Você escolheu Batatas', '. Faltam ', 5-cont, ' acompanhamentos')
            elif values['-ACOMP-'][0] == 'Salada Alface':
                arr_comprados.append('Salada Alface')
                sg.popup('Você escolheu Salada Alface', '. Faltam ', 5-cont, ' acompanhamentos')
            elif values['-ACOMP-'][0] == 'Salada de Tomate':
                arr_comprados.append('Salada de Tomate')
                sg.popup('Você escolheu Salada de Tomate', '. Faltam ', 5-cont, ' acompanhamentos')
            elif values['-ACOMP-'][0] == 'Salada de Maionese':
                arr_comprados.append('Salada de Maionese')
                sg.popup('Você escolheu Salada de Maionese', '. Faltam ', 5-cont, ' acompanhamentos')
            elif values['-ACOMP-'][0] == 'Farofa':
                arr_comprados.append('Farofa')
                sg.popup('Você escolheu Farofa', '. Faltam ', 5-cont, ' acompanhamentos')
            print(arr_valores)
            cont += 1

def tela_bebidas():
    bebidas = ('Refrigerante', 'Cerveja', 'Drinques', 'Sucos', 'Agua')

    layout = [
        [sg.Text('Escolha a Bebida')],
        [sg.Text('Refrigerante - R$ 5.00')],
        [sg.Text('Cerveja - R$ 7.00')],
        [sg.Text('Drinques - R$ 15.00')],
        [sg.Text('Sucos - R$ 10.00')],
        [sg.Text('Agua - R$ 3.00')],
        [sg.Listbox(bebidas, size=(20, len(bebidas)), key='-BEBI-')],
        [sg.Button('Adicionar'), sg.Button('Fechar')]
    ]

    window = sg.Window('Restaurante Píton', layout, element_justification='center')
    

    while True:
        button, values = window.read()
        if button == sg.WIN_CLOSED:
            break
        if button == 'Fechar':
            window.close()
        if button == 'Adicionar':
            if values['-BEBI-'][0] == 'Refrigerante':
                arr_valores.append(5)
                arr_comprados.append('Refrigerante')
                sg.popup('Você escolheu Refrigerante')
            elif values['-BEBI-'][0] == 'Cerveja':
                arr_valores.append(7)
                arr_comprados.append('Cerveja')
                sg.popup('Você escolheu Cerveja')
            elif values['-BEBI-'][0] == 'Drinques':
                arr_valores.append(15)
                arr_comprados.append('Drinques')
                sg.popup('Você escolheu Drinques')
            elif values['-BEBI-'][0] == 'Sucos':
                arr_valores.append(10)
                arr_comprados.append('Sucos')
                sg.popup('Você escolheu Sucos')
            elif values['-BEBI-'][0] == 'Agua':
                arr_valores.append(3)
                arr_comprados.append('Agua')
                sg.popup('Você escolheu Agua')
            print(arr_valores)

def tela_sobremesas():
    sobremesa = ('Banoffe', 'Petit Gateau', 'Pudim', 'Torta Holandesa')

    layout = [
        [sg.Text('Escolha a Sobremesa')],
        [sg.Text('Banoffe - R$ 25.00')],
        [sg.Text('Petit Gateau - R$ 15.00')],
        [sg.Text('Pudim - R$ 10.00')],
        [sg.Text('Torta Holandesa - R$ 13.00')],
        [sg.Listbox(sobremesa, size=(20, len(sobremesa)), key='-SOBRE-')],
        [sg.Button('Adicionar'), sg.Button('Fechar')]
    ]

    window = sg.Window('Restaurante Píton', layout, element_justification='center')
    

    while True:
        button, values = window.read()
        if button == sg.WIN_CLOSED:
            break
        if button == 'Fechar':
            window.close()
        if button == 'Adicionar':
            if values['-SOBRE-'][0] == 'Banoffe':
                arr_valores.append(25)
                arr_comprados.append('Banoffe')
                sg.popup('Você escolheu Banoffe')
            elif values['-SOBRE-'][0] == 'Petit Gateau':
                arr_valores.append(15)
                arr_comprados.append('Petit Gateau')
                sg.popup('Você escolheu Petit Gateau')
            elif values['-SOBRE-'][0] == 'Pudim':
                arr_valores.append(10)
                arr_comprados.append('Pudim')
                sg.popup('Você escolheu Pudim')
            elif values['-SOBRE-'][0] == 'Torta Holandesa':
                arr_valores.append(13)
                arr_comprados.append('Torta Holandesa')
                sg.popup('Você escolheu Torta Holandesa')
            print(arr_valores)

# ==== FINALIZAR PEDIDOS ====

def calc_troco (n):

  arr = []

  while n-50 >= 0:
    
    n = n - 50
    arr.append(50)
   
  while n >= 20:
    n = n - 20
    arr.append(20)
    
  while n >= 10:
    n = n - 10
    arr.append(10)
    
  while n >= 5:
    n = n - 5
    arr.append(5)
    
  while n >= 2:
    n = n - 2
    arr.append(2)
    
  while n >= 1:
    n = n-1
    arr.append(1)
    
  return arr


def finalizar_compra():
    layout = [
        [sg.Text('Total a ser pago R$ ', sum(arr_valores))],
        [sg.InputText(key='-IN-')],      
        [sg.Submit()]
    ]

    window = sg.Window('Restaurante Píton', layout, element_justification='center')


    while True:
        button, values = window.read()
        if button == sg.WINDOW_CLOSED:
            break
        
        text_input = values['-IN-']

        sg.popup('Você vai pagar com: R$ ', text_input)
        
    

        text_input = int(text_input)

        if text_input >= sum(arr_valores):
            print(calc_troco(text_input - sum(arr_valores)))
            sg.popup("Seu troco será com as notas de: ", calc_troco(text_input - sum(arr_valores)))
            window.close()
        else:
            sg.popup("Valor insuficiente")

    
    

# =================================


layout = [

    [sg.Button('Menu de massas'), sg.Button('Menu de carnes')],
    [sg.Button('Menu de bebidas'), sg.Button('Menu de sobremesas')],
    [sg.Button('Finalizar pedidos')]
]

front()

window = sg.Window('Página principal', layout, size=(300, 300), element_justification='center')

while True:
    button, values = window.read()

    if button == sg.WIN_CLOSED:
        break
    if button == 'Menu de massas':
        tela_massas()
    if button == 'Menu de carnes':
        tela_carnes()
    if button == 'Menu de bebidas':
        tela_bebidas()
    if button == 'Menu de sobremesas':
        tela_sobremesas()
    if button == 'Finalizar pedidos':
        sg.popup('Seus pedidos foram: ', arr_comprados)
        sg.popup('O valor total de sua compra é: ', sum(arr_valores))
        finalizar_compra()