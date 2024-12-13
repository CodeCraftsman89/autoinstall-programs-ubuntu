"""
This script changes the current working directory to the PioneerStation directory and runs the 'run.sh' script.

The script uses the os and subprocess modules to change the current working directory and run the shell script.

The 'pioneer_station_install' module is expected to provide the 'pioneer_dir' variable which is the path to the PioneerStation directory.

Please ensure that the 'run.sh' script is executable and that the necessary permissions are set for the user running this script.
"""

import os
import subprocess

from pioneer_station_install import pioneer_dir

# Change the current working directory to the PioneerStation directory
os.chdir(pioneer_dir)

# Run the shell script 'run.sh'
subprocess.run("./run.sh")
