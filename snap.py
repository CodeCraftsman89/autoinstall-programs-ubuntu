"""
This script provides two functions: install_snap_programs and remove_snap_programs.

The install_snap_programs function takes a list of snap programs as input and installs each program using the 'snap install' command.

The remove_snap_programs function takes a list of snap programs as input and removes each program using the 'snap remove' command.

Both functions use the subprocess module to run shell commands.

Please ensure that the necessary permissions are set for the user running this script.
"""

import subprocess

def install_snap_programs(snap_programs):
    """
    Install a list of snap programs.

    Args:
        snap_programs (list): A list of snap programs to install.
    """
    for program in snap_programs:
        cmd = f"sudo snap install {program[0]}"
        subprocess.run(cmd, shell=True)

def remove_snap_programs(programs):
    """
    Remove a list of snap programs.

    Args:
        programs (list): A list of snap programs to remove.
    """
    for program in programs:
        cmd = f"sudo snap remove{program[0]}"
        subprocess.run(cmd, shell=True)