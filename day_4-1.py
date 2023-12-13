# import numpy as np
import textwrap

with open ("problems\\day_4.txt") as file:
    section1: str = ""
    section2: str = ""
    sec1arr: int = [0,0]
    sec2arr: int = [0,0]
    counter: int = 0
    # print(f"section1-1: {section1[0]}, 1-2: {section1[1]}") # Testausgabe
    while line := file.readline():
        section1 = line.split(",")[0]
        section2 = line.split(",")[1]
        # print(f"sec2: {section2}") # Testausgabe
        sec1arr[0] = section1.split("-")[0]
        sec1arr[1] = section1.split("-")[1]
        sec2arr[0] = section2.split("-")[0]
        sec2arr[1] = section2.split("-")[1]
        # print(f"sec1: {sec1arr[0]}-{sec1arr[1]}") # Testausgabe
        if (sec1arr[0] <= sec2arr[0] and sec1arr[1] >= sec2arr[1]) or (sec1arr[0] >= sec2arr[0] and sec1arr[1] <= sec2arr[1]):
            counter += 1
            print(f"counter+: {sec1arr}, {sec2arr}")
    print(f"Counter: {counter}")