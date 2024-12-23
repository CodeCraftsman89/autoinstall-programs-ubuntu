from flathub import install_flathub, install_flathub_programs, remove_flathub_programs
from ubuntu import install_programs, remove_programs
from  snap import install_snap_programs, remove_snap_programs


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        programs = [line.split() for line in lines]
    return programs


files = ['programs.txt', 'flathub.txt', 'snap.txt']
all_programs = read_file(files[0])
all_flathub_programs = read_file(files[1])
all_snap_programs = read_file(files[2])


if __name__ == "__main__":
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
            print('Invalid choice')