import re
from getopt import getopt
from sys import argv

import requests

from profiles import profiles

HELP = """
Usage:
    decoder.py <hash>
    decoder.py ["ENCODINGS","ENCODES","E","ENC"]
    decoder.py -e <encoding> <hash>
    decoder.py --encoding <encoding> <hash>

Options:
    Encoding: -e <encoding> | --encoding <encoding>

For more info look at:
 https://github.com/lacashitateam/HASHDecoder
 https://lacashita.com/projects/HASHDecoder
"""
INFO = """

[?] -> ENCODING
[*] -> ERROR
[-] -> NOT FOUND
[+] -> FOUND

"""


def Decryptor(URLS, METHOD):
    """
    :param URLS: PROFILES DICTIONARY
    :param METHOD: REQUEST METHOD
    :return: GENERATOR: [WEB, RESULT]
    """
    HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    for web, data in URLS.items():
        try:
            if METHOD.upper() == "GET":
                response = requests.get(web, params=data["parameters"], headers=HEADER, timeout=5)
            elif METHOD.upper() == "POST":
                response = requests.post(web, data=data["parameters"], headers=HEADER, timeout=5)
            else:
                raise ValueError("Invalid method")

            yield [web, re.search(data["regex"], response.text).group(1)] if data["success"] in response.text else [web, "N/A"]

        except:
            yield [web, "ERROR"]


if __name__ == "__main__":
    try:
        hash_ = getopt(argv[1:], "e:", ["encoding="])[1][0]  # MAIN HASH
        encoding_ = "ALL"  # MAIN ENCODING

        if hash_.upper() in ["ENCODINGS", "ENCODES", "E", "ENC"]:  # ENCODING LIST
            print(profiles(hash_)["*ENCODES"][1:])
            exit()

        for opt, arg in getopt(argv[1:], "e:", ["encoding="])[0]:  # OPTIONS
            if opt in ["-e", "--encoding"]:
                encoding_ = arg

        if encoding_ and hash_:  # MAIN FUNCTION
            if not encoding_.upper() in profiles(hash_)["*ENCODES"]:print('TYPE: decoder.py ["ENCODINGS","ENCODES","E","ENC"]\nfor encoding information!\n'); raise ValueError("Invalid Encoding")  # RAISE ERROR IF BAD ENCODING

            print(INFO)
            for ENCODING, METHODS in profiles(hash_).items():
                if not ENCODING.startswith("*"):
                    if encoding_.upper() in [ENCODING, "ALL"]:
                        print("[?] ", ENCODING, " (ENCODING)")
                        for METHOD, URLS in METHODS.items():
                            for web, result in Decryptor(URLS, METHOD):
                                print("[*] ", web, ": ", result) if result == "ERROR" else print("[-] ", web, ": ", result) if result == "N/A" else print("[+] ", web, ": ", result)
                        print()

    except Exception as Error:
        print("ERROR: ", Error)
        print(HELP)
