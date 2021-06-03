import os

def solve(flag:str) -> None:
    if(flag in (1, 2, 3)):
        tree = os.walk('/Users/sif/desktop/backendPython')
        for address, dirs, files in tree:
            for file in files:
                if(flag in (1, 3)):
                    print(f"путь: {address+'/'+file}", end=" ")
                if(flag in(2, 3)):
                    print(f"размер: {os.path.getsize(address+'/'+file) } бит")
    else:
        print(f"argument {flag} not found")
# my_example.py
import argparse
parser = argparse.ArgumentParser(description='My example explanation')
parser.add_argument(
    '--my_optional',
    type=int,
    default=2,
    help='1 output only PATH, 2 output only size 3 output path and file size'
)
my_namespace = parser.parse_args()
print(type(my_namespace.my_optional))
solve(my_namespace.my_optional)