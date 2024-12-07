import subprocess

def install_flathub_programs(flathub_programs):
    for program in flathub_programs:
        cmd = f"flatpak install flathub {program[0]}"
        subprocess.run(cmd, shell=True)


def remove_flathub_programs(programs):
    for program in programs:
        cmd = f"flatpak remove {program[0]}"
        subprocess.run(cmd, shell=True)
