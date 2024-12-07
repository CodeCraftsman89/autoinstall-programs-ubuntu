import subprocess

def install_snap_programs(snap_programs):
    for program in snap_programs:
        cmd = f"flatpak install flathub {program[0]}"
        subprocess.run(cmd, shell=True)


def remove_snap_programs(programs):
    for program in programs:
        cmd = f"flatpak remove {program[0]}"
        subprocess.run(cmd, shell=True)
