def profiles(hash_):
    return {
        "*ENCODES": [
            "ALL",
            "SHA1",
            "MD5"
        ],
        "SHA1": {
            "GET": {
                "https://sha1.gromweb.com/": {
                    "parameters": {"hash": hash_},
                    "regex": r'string">(.*?)</em></p>',
                    "success": "succesfully"
                },
                "https://hashtoolkit.com/decrypt-hash/": {
                    "parameters": {"hash": hash_},
                    "regex": r'<span title="decrypted sha1 hash"><a href="/generate-hash/\?text=(.*?)">',
                    "success": "Hash Results"
                }
            },
            "POST": {
                "https://md5decrypt.net/en/Sha1": {
                    "parameters": {
                        "hash": hash_,
                        "captcha58": "",
                        "ahah58": "15dcf9dc3024bc33a723cb4958598499",
                        "decrypt": "Decrypt"
                    },
                    "regex": r'<b>.(*?)\b',
                    "success": "Found in"

                }
            }
        },
        "MD5": {
            "GET": {
                "https://md5.gromweb.com/": {
                    "parameters": {"md5": hash_},
                    "regex": r'string">(.*?)</em></p>',
                    "success": "succesfully"

                }
            },
            "POST": {
                "https://www.md5online.org/md5-decrypt.html": {
                    "parameters": {
                        "hash": hash_,
                        "quick": 1
                    },
                    "regex": r'Found : <b>*?</b>',
                    "success": "Found : "

                }
            }
        }

    }
