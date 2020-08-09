"""This program allows us to download data from webside and save it quite conviniently"""

import requests
import os
import functools

#Function download data from www websides
def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


save_url_to_dir = functools.partial(save_url_file, dir = 'c:/123/', msg = 'Please wait: {}')

url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url = url, file = file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'c:/123'
file = 'logo.png'

#this allows us to save the url to dir(I choosen c:/123) only by inputting the url of webside and file that we want
save_url_to_dir(url = url, file = file)