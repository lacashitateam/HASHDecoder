import re
from getopt import getopt
from sys import argv

import requests

HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
HELP = """
Usage:
    decoder.py <hash>
    decoder.py -e <encoding> <hash>
    decoder.py --encoding <encoding> <hash>

Options:
    Encoding: -e <encoding> | --encoding <encoding>

For more info look at:
 https://github.com/lacashitateam/HASHDecoder
 https://lacashita.com/projects/HASHDecoder
"""


class SHA1:
    class SHA1_GET:
        def __init__(self, sha1):
            self.URL = {
                "https://sha1.gromweb.com/": {
                    "parameters": {"hash": sha1},
                    "regex": r'string">(.*?)</em></p>',
                    "success": "succesfully"
                },
                "https://hashtoolkit.com/decrypt-hash/": {
                    "parameters": {"hash": sha1},
                    "regex": r'<span title="decrypted sha1 hash"><a href="/generate-hash/\?text=(.*?)">',
                    "success": "Hash Results"
                }
            }
            global HEADER

        def decriptor(self):
            for web, data in self.URL.items():
                try:
                    response = requests.get(web, params=data["parameters"], headers=HEADER, timeout=5)

                    yield [web, re.search(data["regex"], response.text).group(1)] if data["success"] in response.text else [web, "N/A"]

                except:
                    yield [web, "ERROR"]

    class SHA1_POST:
        def __init__(self, sha1):
            self.URL = {
                "https://md5decrypt.net/en/Sha1": {
                    "parameters": {
                        "hash": sha1,
                        "captcha58": "",
                        "ahah58": "15dcf9dc3024bc33a723cb4958598499",
                        "decrypt": "Decrypt"
                    },
                    "regex": r'<b>.(*?)\b',
                    "success": "Found in"

                }
            }
            global HEADER

        def decriptor(self):
            for web, data in self.URL.items():
                try:
                    response = requests.post(web, data=data["parameters"], headers=HEADER, timeout=5)

                    yield [web, re.search(data["regex"], response.text).group(1)] if data["success"] in response.text else [web, "N/A"]

                except:
                    yield [web, "ERROR"]


class MD5:
    class MD5_GET:
        def __init__(self, md5):
            self.URL = {
                "https://md5.gromweb.com/": {
                    "parameters": {"md5": md5},
                    "regex": r'string">(.*?)</em></p>',
                    "success": "succesfully"

                }
            }
            global HEADER

        def decriptor(self):
            for web, data in self.URL.items():
                try:
                    response = requests.get(web, params=data["parameters"], headers=HEADER, timeout=5)

                    yield [web, re.search(data["regex"], response.text).group(1)] if data["success"] in response.text else [web, "N/A"]

                except:
                    yield [web, "ERROR"]

    class MD5_POST:
        def __init__(self, md5):
            self.URL = {
                "https://www.md5online.org/md5-decrypt.html": {
                    "parameters": {
                        "hash": md5,
                        "quick": 1,
                        "g-recaptcha-response": "03AGdBq26CyPfi9sd2pWnFD4YT2ltLdFk39ZIbj3MiBNASmxFR1WmqJbFFwzlm-PmTUUR4TYdo21hwlrTE-bWfU5r3FNbs3NQe78gaijYaKYnE7taH62qchs1tPW-_rgjmfrdRAgrgWQn2962YrbpO3Dyge-O2evTSP5SP-WOWXwNR065JTjaJatQIMcd0RUpFQjBEuZH_rIaOS0hV1YK0kl7NcYCa8cAolxgygvS9IpEi9oZ3Q__zNdqF6peUnfIoQ8odx0El_XKWchIXVfQs088z3l9HW2nU-a51ewVpHL049bfuoABTzgYqLH_nn7zIaHZKeZcbv_JZ1nlg6unESc0ThBtkBmL0TcRhqSNh5E88nGpVR-ri86dUcJM5f7Tn13IAD8eLimnkda6dGxvW302f-y5YV1F3Aw"
                    },
                    "regex": r'Found : <b>*?</b>',
                    "success": ">Found : <b>"

                }
            }

            global HEADER

        def decriptor(self):
            for web, data in self.URL.items():
                try:
                    response = requests.post(web, params=data["parameters"], headers=HEADER, timeout=5)

                    yield [web, re.search(data["regex"], response.text).group(1)] if data["success"] in response.text else [web, "N/A"]

                except:
                    yield [web, "ERROR"]


if __name__ == "__main__":
    try:
        hash_ = getopt(argv[1:], "e:", ["encoding="])[1][0]
        encoding_ = "ALL"

        for opt, arg in getopt(argv[1:], "e:", ["encoding="])[0]:
            if opt in ["-e", "--encoding"]:
                encoding_ = arg

        if encoding_:
            if encoding_.upper() in ["MD5", "ALL"] and hash_:
                MD5_G = MD5().MD5_GET(hash_)

                print("\n\nMD5 GET")
                for web_, decode_ in MD5_G.decriptor():
                    print(web_, ":", decode_)

            if encoding_.upper() in ["SHA1", "ALL"] and hash_:
                SHA_G = SHA1().SHA1_GET(hash_)

                print("\n\nSHA1 GET")
                for web_, decode_ in SHA_G.decriptor():
                    print(web_, ":", decode_)

            if encoding_.upper() in ["MD5", "ALL"] and hash_:
                MD5_P = MD5().MD5_POST(hash_)

                print("\n\nMD5 POST")
                for web_, decode_ in MD5_P.decriptor():
                    print(web_, ":", decode_)

            if encoding_.upper() in ["SHA1", "ALL"] and hash_:
                SHA_P = SHA1().SHA1_POST(hash_)

                print("\n\nSHA1 POST")
                for web_, decode_ in SHA_P.decriptor():
                    print(web_, ":", decode_)

    except Exception:
        print("ERROR")

    except KeyboardInterrupt:
        print("STOOPING")
