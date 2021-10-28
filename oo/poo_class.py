from os import name
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, Input, Text

saved =  dict()

class cellphone():
    def __init__(self):
        
        layout = [
        [sg.Radio('Samsung', 'cell',size=(10,5),key='samsung'), sg.Radio('LG', 'cell',size=(10,5),key='lg')],
        [sg.Radio('Motorola', 'cell',size=(10,5),key='motorola'), sg.Radio('Xiaomi', 'cell',size=(10,5),key='xiaomi')],
        [sg.Button('Send')], [sg.Button('Close')],
        ]
            
        self.window = sg.Window('Cellphone').layout(layout)
        
    
    def info(self):
        self.button, self.values = self.window.Read()
        if self.values['samsung'] == True:
            layout = [
                [sg.Text('Registration')],
                [sg.Text('Name',size=(5,0)), sg.Input(size=(25,0),key='name')],
                [sg.Text('Birth Date',size=(5,0)), sg.Input(size=(25,0),key='birth')],
                [sg.Text('Phone number',size=(5,0)), sg.Input(size=(25,0),key='number')],
                [sg.Text('E-mail',size=(5,0)), sg.Input(size=(25,0),key='email')],
                [sg.Checkbox('A01',size=(10,5),key='a01'), sg.Checkbox('A10S',size=(10,5),key='a10s')],
                [sg.Checkbox('Galaxy Z Flip3',size=(10,5),key='flip3'), sg.Checkbox('Galaxy Z Fold3',size=(17,5),key='fold3')],
                [sg.Button('Send')],
            ]
            self.window = sg.Window('Request').layout(layout)
            self.button, self.values = self.window.Read()
            
            name = self.values['name']
            birth_date = self.values['birth']
            phone_number = self.values['number']
            e_mail = self.values['email']
            a1 = self.values['a01']
            a10s = self.values['a10s']
            flip3 = self.values['flip3']
            fold3 = self.values['fold3']
            print(f'Name: {name}')
            print(f'Birth Date: {birth_date}')
            print(f'Phone number: {phone_number}')
            print(f'E-mail: {e_mail}')
            print(f'Samsung A01: {a1}')
            print(f'Samsung A10S: {a10s}')
            print(f'Samsung Galaxy Z Flip3: {flip3}')
            print(f'Samsung Galaxy Z Fold3: {fold3}')
            saved['SaMsUng'] = self.values
            print(saved)
            
        elif self.values['lg'] == True:
            layout = [
                [sg.Text('Registration')],
                [sg.Text('Name',size=(5,0)), sg.Input(size=(25,0),key='name')],
                [sg.Text('Birth Date',size=(5,0)), sg.Input(size=(25,0),key='birth')],
                [sg.Text('Phone number',size=(5,0)), sg.Input(size=(25,0),key='number')],
                [sg.Text('E-mail',size=(5,0)), sg.Input(size=(25,0),key='email')],
                [sg.Checkbox('LG K10',size=(10,5),key='k10'), sg.Checkbox('LG K71',size=(10,5),key='k71')],
                [sg.Checkbox('LG K41S',size=(10,5),key='k41s'), sg.Checkbox('LG K61',size=(17,5),key='k61')],
                [sg.Button('Send')],
            ]
            self.window = sg.Window('Request').layout(layout)
            self.button, self.values = self.window.Read()
            
            name = self.values['name']
            birth_date = self.values['birth']
            phone_number = self.values['number']
            e_mail = self.values['email']
            k10 = self.values['k10']
            k71 = self.values['k71']
            k41s = self.values['k41s']
            k61 = self.values['k61']
            print(f'Name: {name}')
            print(f'Birth Date: {birth_date}')
            print(f'Phone number: {phone_number}')
            print(f'E-mail: {e_mail}')
            print(f'LG K10: {k10}')
            print(f'LG K71: {k71}')
            print(f'LG K41S: {k41s}')
            print(f'LG K61: {k61}')
            saved['lG'] = self.values
            print(saved)
            
        elif self.values['motorola'] == True:
            layout = [
                [sg.Text('Registration')],
                [sg.Text('Name',size=(5,0)), sg.Input(size=(25,0),key='name')],
                [sg.Text('Birth Date',size=(5,0)), sg.Input(size=(25,0),key='birth')],
                [sg.Text('Phone number',size=(5,0)), sg.Input(size=(25,0),key='number')],
                [sg.Text('E-mail',size=(5,0)), sg.Input(size=(25,0),key='email')],
                [sg.Checkbox('Moto G10',size=(10,5),key='g10'), sg.Checkbox('Moto G20',size=(10,5),key='g20')],
                [sg.Checkbox('Moto G30',size=(10,5),key='g30'), sg.Checkbox('Moto e6s',size=(17,5),key='e6s')],
                [sg.Button('Send')],
            ]
            self.window = sg.Window('Request').layout(layout)
            self.button, self.values = self.window.Read()
            
            name = self.values['name']
            birth_date = self.values['birth']
            phone_number = self.values['number']
            e_mail = self.values['email']
            g10 = self.values['g10']
            g20 = self.values['g20']
            g30 = self.values['g30']
            e6s = self.values['e6s']
            print(f'Name: {name}')
            print(f'Birth Date: {birth_date}')
            print(f'Phone number: {phone_number}')
            print(f'E-mail: {e_mail}')
            print(f'Moto G10: {g10}')
            print(f'Moto G20: {g20}')
            print(f'Moto G30: {g30}')
            print(f'Moto e6s: {e6s}')
            saved['MoTorola'] = self.values
            print(saved)
            
        elif self.values['xiaomi'] == True:
            layout = [
                [sg.Text('Registration')],
                [sg.Text('Name',size=(5,0)), sg.Input(size=(25,0),key='name')],
                [sg.Text('Birth Date',size=(5,0)), sg.Input(size=(25,0),key='birth')],
                [sg.Text('Phone number',size=(5,0)), sg.Input(size=(25,0),key='number')],
                [sg.Text('E-mail',size=(5,0)), sg.Input(size=(25,0),key='email')],
                [sg.Checkbox('Redmi 9',size=(10,5),key='r9'), sg.Checkbox('Redmi 9A',size=(10,5),key='r9a')],
                [sg.Checkbox('Redmi 10',size=(10,5),key='r10'), sg.Checkbox('Poco M3',size=(17,5),key='m3')],
                [sg.Button('Send')],
            ]
            self.window = sg.Window('Request').layout(layout)
            self.button, self.values = self.window.Read()
            
            name = self.values['name']
            birth_date = self.values['birth']
            phone_number = self.values['number']
            e_mail = self.values['email']
            r9 = self.values['r9']
            r9a = self.values['r9a']
            r10 = self.values['r10']
            m3 = self.values['m3']
            print(f'Name: {name}')
            print(f'Birth Date: {birth_date}')
            print(f'Phone number: {phone_number}')
            print(f'E-mail: {e_mail}')
            print(f'Redmi 9: {r9}')
            print(f'Redmi 9A: {r9a}')
            print(f'Redmi 10: {r10}')
            print(f'Poco M3: {m3}')
            saved['XiaOMI'] = self.values
            print(saved)
            

'''class megadict():
        def S(txt):
            sam = txt
            return print(sam) 

        def Lg(txt):
            g = txt
            return print(g) 

        def MO(txt):
            MOto = txt
            return print(MOto) 

        def Xia(txt):
            XiAmoi = txt
            return print(XiAmoi) 
'''

