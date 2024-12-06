import subprocess

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        programs = [line.split() for line in lines]
    return programs

def install_programs(programs):
    for program in programs:
        cmd = f"sudo apt install -y {program[0]}"
        subprocess.run(cmd, shell=True)

def remove_programs(programs):
    for program in programs:
        cmd = f"sudo remove -y {program[0]}"
        subprocess.run(cmd, shell=True)


def install_flathub():
    cmds = [
        'sudo apt install flatpak',
        'sudo apt install gnome-software-plugin-flatpak',
        'flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
        subprocess.run('shutdown -r now', shell=True)

def install_flathub_programs(flathub_programs):
    for program in flathub_programs:
        cmd = f"flatpak install flathub {program[0]}"
        subprocess.run(cmd, shell=True)

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