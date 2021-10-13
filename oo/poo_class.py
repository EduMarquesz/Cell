from os import name
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input, Text


class cellphone():
    def __init__(self):
        layout = [
        [sg.Radio('Samsung', 'cell',size=(10,5),key='samsung'), sg.Radio('LG', 'cell',size=(10,5),key='lg')],
        [sg.Radio('Motorola', 'cell',size=(10,5),key='motorola'), sg.Radio('Xiaomi', 'cell',size=(10,5),key='xiaomi')],
        [sg.Button('Send')],
        ]
        
        self.window = sg.Window('Cellphone').layout(layout)
        
    
    def info(self):
        while True:
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
                self.window2 = sg.Window('Request').layout(layout)
                self.button2, self.values2 = self.window2.Read()
                
                name = self.values2['name']
                birth_date = self.values2['birth']
                phone_number = self.values2['number']
                e_mail = self.values2['email']
                a1 = self.values2['a01']
                a10s = self.values2['a10s']
                flip3 = self.values2['flip3']
                fold3 = self.values2['fold3']
                print(f'Name: {name}')
                print(f'Birth Date: {birth_date}')
                print(f'Phone number: {phone_number}')
                print(f'E-mail: {e_mail}')
                print(f'Samsung A01: {a1}')
                print(f'Samsung A10S: {a10s}')
                print(f'Samsung Galaxy Z Flip3: {flip3}')
                print(f'Samsung Galaxy Z Fold3: {fold3}')
                break
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
                self.window3 = sg.Window('Request').layout(layout)
                self.button3, self.values3 = self.window3.Read()
                
                name = self.values3['name']
                birth_date = self.values3['birth']
                phone_number = self.values3['number']
                e_mail = self.values3['email']
                k10 = self.values3['k10']
                k71 = self.values3['k71']
                k41s = self.values3['k41s']
                k61 = self.values3['k61']
                print(f'Name: {name}')
                print(f'Birth Date: {birth_date}')
                print(f'Phone number: {phone_number}')
                print(f'E-mail: {e_mail}')
                print(f'LG K10: {k10}')
                print(f'LG K71: {k71}')
                print(f'LG K41S: {k41s}')
                print(f'LG K61: {k61}')
                break
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
                self.window4 = sg.Window('Request').layout(layout)
                self.button4, self.values4 = self.window4.Read()
                
                name = self.values4['name']
                birth_date = self.values4['birth']
                phone_number = self.values4['number']
                e_mail = self.values4['email']
                g10 = self.values4['g10']
                g20 = self.values4['g20']
                g30 = self.values4['g30']
                e6s = self.values4['e6s']
                print(f'Name: {name}')
                print(f'Birth Date: {birth_date}')
                print(f'Phone number: {phone_number}')
                print(f'E-mail: {e_mail}')
                print(f'Moto G10: {g10}')
                print(f'Moto G20: {g20}')
                print(f'Moto G30: {g30}')
                print(f'Moto e6s: {e6s}')
                break
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
                self.window5 = sg.Window('Request').layout(layout)
                self.button5, self.values5 = self.window5.Read()
                
                name = self.values5['name']
                birth_date = self.values5['birth']
                phone_number = self.values5['number']
                e_mail = self.values5['email']
                r9 = self.values5['r9']
                r9a = self.values5['r9a']
                r10 = self.values5['r10']
                m3 = self.values5['m3']
                print(f'Name: {name}')
                print(f'Birth Date: {birth_date}')
                print(f'Phone number: {phone_number}')
                print(f'E-mail: {e_mail}')
                print(f'Redmi 9: {r9}')
                print(f'Redmi 9A: {r9a}')
                print(f'Redmi 10: {r10}')
                print(f'Poco M3: {m3}')
                break