from string import ascii_lowercase
import random

def binary_write():
    rand_string = ''.join(random.choice(ascii_lowercase) for i in range(10))
    with open("solve.txt", mode="wb") as file:
        file.write(rand_string.encode())
def binary_read():
    with open("solve.txt", mode="rb") as file:
        rand_string=file.read().decode("utf-8")
    return rand_string

binary_write()
print(binary_read())