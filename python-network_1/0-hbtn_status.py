#!/usr/bin/python3
"""
A Python script that fetches https://alu-intranet.hbtn.io/status
using urllib package and displays specific details about the response.
"""

import urllib.request
import urllib.error

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
            utf8_content = html_content.decode('utf-8')

            print("Body response:")
            print("\t- type: {}".format(type(html_content)))
            print("\t- content: {}".format(html_content))
            print("\t- utf8 content: {}".format(utf8_content))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

