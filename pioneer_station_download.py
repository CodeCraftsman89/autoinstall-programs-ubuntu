"""
This script downloads a zip file from a URL, extracts it, and saves it to the current directory.

The script uses the requests and zipfile modules to download and extract the zip file.

The URL of the zip file is stored in the 'url' variable. The 'requests.get()' function is used to download the file, and the 'response.content' is written to a file named 'PioneerStationLinux.zip'.

The zipfile module is then used to open the zip file and extract all the contents to the current directory.

Please ensure that the necessary permissions are set for the user running this script.
"""

import requests, zipfile

# URL of the zip file
url = 'https://storage.yandexcloud.net/pioneer-doc.geoscan.ru-static/dwnlds/software/PioneerStation/PioneerStationLinux.zip'

# Download the file
response = requests.get(url)

# Save the file
with open('PioneerStationLinux.zip', 'wb') as file:
    file.write(response.content)

# Extract the zip file
with zipfile.ZipFile('PioneerStationLinux.zip', 'r') as zip_ref:
    zip_ref.extractall()