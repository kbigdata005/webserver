import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-he", "--hello", dest="hello", action="store")
args = parser.parse_args()
if args.hello == '1':
    print("Hello World!!!")
else:
    print("What the Hell!!")