# HASHDecoder


HASHDecoder is a hash decoder tool.

  - Enter a HASH and show up all results
  - Easy to use
  - Easy set-up

# New Features!

  - GET and POST methods for search


You can also:
  - Search for a wanted encoding

### Tech

HASHDecoder uses a number of open source projects to work properly:

* [Sys] - System-specific parameters and functions.
* [Requests] - Elegant and simple HTTP library for Python, built for human beings.
* [Getopt] - C-style parser for command line options.
* [Re] - Regular expression operations.

And of course HASHDecoder itself is open source.

### Installation

HASHDecoder requires [Python3.x](https://www.python.org/downloads/) to run.

Install the dependencies and start decoder.py.

```sh
LINUX:
$ cd HASHDecoder
$ python3 -m pip install -r requirements.txt
$ python3 decoder.py

WINDOWS:
$ cd HASHDecoder
$ python3 -m pip install -r requirements.txt
$ python3 decoder.py
```

For Undefined HASH encoding

```sh
$ python3 decoder.py <hash>
# This wil check for all HASH SOLUTIONS
```

For Defined HASH encoding
```sh
$ python3 decoder.py --encoding MD5 <hash>
# This wil check for all HASH SOLUTIONS
```


### USAGE MENU
```sh
Usage:
    decoder.py <hash>
    decoder.py -e <encoding> <hash>
    decoder.py --encoding <encoding> <hash>

Options:
    Encoding: -e <encoding> | --encoding <encoding>

```


### TODO

 - Add more encodings