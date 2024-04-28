import time


file_to_read = "arquivo.txt"

with open(file_to_read, "r") as my_file:
    while True:
        for linha in my_file:
            print(linha.strip(), end="\n")

        time.sleep(1)
