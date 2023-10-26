print("Hello Git! With changes")
print("Hola este es un curso de git & github")

import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='URL to download')
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists("subdominios.txt"):
            wordlist = open("subdominios.txt", "r")
            wordlist = wordlist.read().split('\n')
            for word in wordlist:
                print(word)
            print("hola")
        else:
            print("adios")
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    