#!/usr/bin/env python
"""from module import function2 as function1
from othermodule import function2


def main():
    print('hello from main!')
    function1()
    function2()


"""
import urllib.request
from urllib.error import HTTPError, URLError

def main():
    try:
        with urllib.request.urlopen('http://shadyshitsoftware.com') as response:
            html = response.read()
            print(str(html))
    #except Exception as x:
    #    print(x)
    #    print('all other generic errors')
    except HTTPError as e:
        print('There was an error during the request! HTTP Code: %d' % e.code)
        print(e.reason)
    except URLError as u:
        print('There was something wrong with the URL! Reason: %s' % u.reason)
    print('continuing on')

if __name__ == "__main__":
    main()