"""
This script installs dependencies and adds the current user to the 'dialout' group in the PioneerStation directory.

Dependencies:
- libcanberra-gtk-module
- libcanberra-gtk3-module

The script uses the subprocess module to run shell commands and the os module to change the current working directory.

The script assumes that the 'pioneer_station_install' module provides the 'pioneer_dir' variable which is the path to the PioneerStation directory.

Please ensure that the necessary permissions are set for the user running this script.
"""

import subprocess
import os

# List of dependencies to be installed
dependencies = ["libcanberra-gtk-module", "libcanberra-gtk3-module"]

# Path to the PioneerStation directory
pioneer_dir = "PioneerStation"

# Install dependencies
for i in dependencies:
    subprocess.run(f"sudo apt-get install -y {i}", shell=True)

# Change the current working directory to the PioneerStation directory
os.chdir(pioneer_dir)

# Add the current user to the 'dialout' group
subprocess.run(f"sudo adduser $USER dialout", shell=True)
