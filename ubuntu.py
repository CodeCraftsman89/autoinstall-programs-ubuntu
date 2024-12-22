"""
This script provides two functions: install_programs and remove_programs.

The install_programs function takes a list of programs as input and installs each program using the 'sudo apt install -y' command.

The remove_programs function takes a list of programs as input and removes each program using the 'sudo remove -y' command.

Both functions use the subprocess module to run shell commands.

Please ensure that the necessary permissions are set for the user running this script.
"""

import subprocess

def install_programs(programs):
    """
    Install a list of programs.

    Args:
        programs (list): A list of programs to install.
    """
    for program in programs:
        cmd = f"sudo apt install -y {program[0]}"
        subprocess.run(cmd, shell=True)

def remove_programs(programs):
    """
    Remove a list of programs.

    Args:
        programs (list): A list of programs to remove.
    """
    for program in programs:
        cmd = f"sudo apt remove -y {program[0]}"
        subprocess.run(cmd, shell=True)
