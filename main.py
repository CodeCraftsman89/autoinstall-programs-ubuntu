from flathub import install_flathub, install_flathub_programs
from ubuntu import install_programs, remove_programs


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        programs = [line.split() for line in lines]
    return programs


files = ['programs.txt', 'flathub.txt']
all_programs = read_file('programs.txt')
all_flathub_programs = read_file('flathub.txt')


while True:
    print('1. Install programs')
    print('2. Remove programs')
    print('3. Install flathub')
    print('4. Install flathub programs')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        install_programs(all_programs)
    elif choice == '2':
        remove_programs(all_programs)
    elif choice == '3':
        install_flathub()
    elif choice == '4':
        install_flathub_programs(all_flathub_programs)
    elif choice == '5':
        break
    else:
        print('Invalid choice')
