import subprocess

def read_file():
    with open('programs.txt', 'r') as file:
        lines = file.readlines()
        programs = [line.split() for line in lines]
    return programs

def install_programs(programs):
    for program in programs:
        cmd = f"sudo apt install -y {program[0]}"
        subprocess.run(cmd, shell=True)



all_programs = read_file()

while True:
    print("1. Install programs")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        install_programs(all_programs)
    elif choice == "2":
        break
    else:
        print("Invalid choice")
