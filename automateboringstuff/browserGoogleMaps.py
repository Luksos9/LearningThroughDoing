
'https://www.google.com/maps/place/Stefana+Banacha,+Kraków

#! python3
# browserGoogleMaps.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.