"""
This script provides three functions: install_flathub, install_flathub_programs, and remove_flathub_programs.

The install_flathub function installs Flatpak, adds the Flathub repository, and restarts the system.

The install_flathub_programs function takes a list of Flathub programs as input and installs each program using the 'flatpak install' command.

The remove_flathub_programs function takes a list of Flathub programs as input and removes each program using the 'flatpak remove' command.

All functions use the subprocess module to run shell commands.

Please ensure that the necessary permissions are set for the user running this script.
"""

import subprocess

def install_flathub():
    """
    Install Flatpak, add the Flathub repository, and restart the system.
    """
    cmds = [
        'sudo apt install flatpak',
        'sudo apt install gnome-software-plugin-flatpak',
        'flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    subprocess.run('shutdown -r now', shell=True)

def install_flathub_programs(flathub_programs):
    """
    Install a list of Flathub programs.

    Args:
        flathub_programs (list): A list of Flathub programs to install.
    """
    for program in flathub_programs:
        cmd = f"flatpak install flathub {program[0]}"
        subprocess.run(cmd, shell=True)

def remove_flathub_programs(programs):
    """
    Remove a list of Flathub programs.

    Args:
        programs (list): A list of Flathub programs to remove.
    """
    for program in programs:
        cmd = f"flatpak remove {program[0]}"
        subprocess.run(cmd, shell=True)
