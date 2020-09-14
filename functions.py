import sys
import time

def printf(sentence: str):
    # Print one character at a time
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        # time.sleep(0.08)
    print()

def dateprint(sentence: str):
    # Print one character at a time
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)
    input()
    print()


def inputf(sentence: str):
    # Print one character at a time and take in the output
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    input()
