import argparse
import os

class storePassword:
    def __init__(self):
        pass
    def execute(self, args):
        # the logic for storing a password based on arguments
        print("Storing encrypted password...")


def main():
    # define parser
    parser = argparse.ArgumentParser(description='Keygarden: password manager.')

    # parse arguments
    args = parser.parse_args()

    # store password
    parser.add_argument('spw', help='stores an ecrypted password.')

    if 'spw' in args:
        storePassword.execute(args)

if __name__ == "__main__":
    main()
