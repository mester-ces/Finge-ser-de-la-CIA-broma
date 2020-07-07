from sys import stdout 

def red() :
    RED = "\033[1;31m"
    stdout.write(RED)


def green() :
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def bold() :
    BOLD = "\033[1m"
    stdout.write(BOLD)

def cyan() :
    CYAN = "\033[1;36m"
    stdout.write(CYAN)

def yellow() :
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def reset() :
    RESET = "\033[0m"
    stdout.write(RESET)
