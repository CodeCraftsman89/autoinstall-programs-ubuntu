import os, subprocess

from pioneer_station_install import pioneer_dir

os.chdir(pioneer_dir)
subprocess.run("./run.sh")