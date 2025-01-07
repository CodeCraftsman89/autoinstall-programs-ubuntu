from email.policy import default

from flathub import install_flathub, install_flathub_programs, remove_flathub_programs
from ubuntu import install_programs, remove_programs
from  snap import install_snap_programs, remove_snap_programs
import tkinter as tk
from tkinter import *
from tkinter import ttk

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        programs = [line.split() for line in lines]
    return programs


files = ['programs.txt', 'flathub.txt', 'snap.txt']
all_programs = read_file(files[0])
all_flathub_programs = read_file(files[1])
all_snap_programs = read_file(files[2])

window = Tk()
window.title ('Авноустановщик программ для Ubuntu')
window.geometry("300x300")
window.resizable(False, False)

label = Label(text='Выберете нужную опцию')
label.pack()

'''if __name__ == "__main__":
    while True:
        print('1. Install programs')
        print('2. Remove programs')
        print('3. Install flathub programs')
        print('4. Remove flathub programs')
        print('5. Install snap programs')
        print('6. Remove snap programs')
        print('7. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            install_programs(all_programs)
        elif choice == '2':
            remove_programs(all_programs)
        elif choice == '3':
            install_flathub()
        elif choice == '4':
            remove_flathub_programs(all_flathub_programs)
        elif choice == '5':
            install_snap_programs(all_snap_programs)
        elif choice == '6':
            remove_snap_programs(all_snap_programs)
        elif choice == '7':
            break
        else:
            print('Invalid choice')'''

def btn_repo_click():
    install_programs(all_programs)

def btn_repo_r_click():
    remove_programs(all_programs)

def btn_flathub_click():
    install_flathub()

def btn_flathub_i_click():
    install_flathub_programs(all_flathub_programs)

def btn_flathub_r_click():
    remove_flathub_programs(all_flathub_programs)

def btn_snap_click():
    install_snap_programs(all_snap_programs)

def btn_snap_r_click():
    remove_snap_programs(all_snap_programs)

btn_repo = ttk.Button(window, text='Установить программы', command=btn_repo_click)
btn_repo_r = ttk.Button(window, text='Удалить программы', command=btn_repo_r_click)
btn_flathub = ttk.Button(window, text='Установить flathub', command=btn_flathub_click)
btn_flathub_i = ttk.Button(window, text='Удалить flathub программы', command=btn_flathub_i_click)
btn_flathub_r = ttk.Button(window, text='Удалить flathub программы', command=btn_flathub_r_click)
btn_snap = ttk.Button(window, text='Установить snap', command=btn_snap_click)
btn_snap_r = ttk.Button(window, text='Удалить snap', command=btn_snap_r_click)

btn_repo.pack(expand=True, fill=X)
btn_repo_r.pack(expand=True, fill=X)
btn_flathub.pack(expand=True, fill=X)
btn_flathub_i.pack(expand=True, fill=X)
btn_flathub_r.pack(expand=True, fill=X)
btn_snap.pack(expand=True, fill=X)
btn_snap_r.pack(expand=True, fill=X)

window.mainloop()