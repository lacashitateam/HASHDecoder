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
            print(profiles(hash_)["ENCODES"][1:])
            exit()

        for opt, arg in getopt(argv[1:], "e:", ["encoding="])[0]:  # OPTIONS
            if opt in ["-e", "--encoding"]:
                encoding_ = arg

        if encoding_ and hash_:  # MAIN FUNCTION
            DECODERS = {
                "SHA1": {
                    "GET": profiles(hash_)["SHA1_GET"],
                    "POST": profiles(hash_)["SHA1_POST"]
                },
                "MD5": {
                    "GET": profiles(hash_)["MD5_GET"],
                    "POST": profiles(hash_)["MD5_POST"]
                }
            }  # DICTIONARY
            if not encoding_.upper() in profiles(hash_)["ENCODES"]: raise ValueError("Invalid Encoding")  # RAISE ERROR IF BAD ENCODING
            print(INFO)
            for ENCODING, DATA in DECODERS.items():  # PROCESSING DICTIONARIES
                if encoding_.upper() in [ENCODING, "ALL"]:
                    print("[?] ", ENCODING, " (ENCODING)")
                    for decode_method, decode_urls in DATA.items():
                        for web, result in Decryptor(decode_urls, decode_method):
                            print("[*] ", web, ": ", result) if result == "ERROR" else print("[-] ", web, ": ", result) if result == "N/A" else print("[+] ", web, ": ", result)
                print()

    except Exception as Error:
        print("ERROR: ", Error)
        print(HELP)
