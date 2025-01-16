#Write a program that takes a URL as a command-line argument and reports whether or not there is a working website at that address.

import sys
import requests
# Program to check if a website is working
if len(sys.argv) > 1:
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} returned status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
else:
    print("Please provide a URL as a command-line argument.")


