import subprocess


def install_programs(programs):
    for program in programs:
        cmd = f"sudo apt install -y {program[0]}"
        subprocess.run(cmd, shell=True)

def remove_programs(programs):
    for program in programs:
        cmd = f"sudo remove -y {program[0]}"
        subprocess.run(cmd, shell=True)
