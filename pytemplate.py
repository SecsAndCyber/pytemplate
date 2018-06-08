from __future__ import print_function
import argparse, sys, os, logging
CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def main(args):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--arg")
    parser.add_argument('--verbose', '-v', action='count')
    args = parser.parse_args()
    
    if args.verbose > 3:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose == 3:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose == 2:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARN)
        
    main(args)
