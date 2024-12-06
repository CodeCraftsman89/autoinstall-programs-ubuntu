import subprocess

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