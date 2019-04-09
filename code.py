"""
grab data from Apache NiFi REST API
If you can find something that spits out JSON data, we can display it!
https://nifi.apache.org/docs/nifi-docs/rest-api/
"""
import time
import board
from adafruit_pyportal import PyPortal

# Set up where we'll be fetching data from
DATA_SOURCE = "http://hw13125.local:8080/nifi-api/flow/status"
DATA_LOCATION = ["controllerStatus", "flowFilesQueued"]

def text_transform(val):
    format_str = "FlowFilesQueued in NiFi = {:d}"
    return format_str.format(val)
    
# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE, json_path=DATA_LOCATION,
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/cloudera.bmp",
                    text_font=cwd+"/fonts/Arial-ItalicMT-17.bdf",
                    text_position=(20, 20),
                    text_color=0xFFFFFF,
                    text_transform=text_transform)
pyportal.preload_font(b'$012345789')  # preload numbers

while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)

    time.sleep(60)  # 
