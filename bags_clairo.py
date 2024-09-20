#!/usr/bin/env python3
from time import sleep

def main():
    #lines = ["Lyrics", charDelay, lineDelay]
    lines = [
        ("Every minute counts", 0.07, 0.6),
        ("I don't wanna watch TV ", 0.07, 0.05),
        ("anymore", 0.2, 3.3),
        ("Can you figure me out?", 0.07, 0.52),
        ("Just doin' to waste more time on the couch", 0.07, 3),
        ("Can you see me? I'm waiting for the right time", 0.06, 1.3),
        ("I can't read you, but if you want, the pleasure's all mine", 0.065, 1), 
        ("Can you see me using everything to hold back?", 0.065, 0.4),
        ("I guess this could be worse", 0.07, 0.08),
        ("Walkin' out the door with your bags", 0.06, 2.1),
        ("Walkin' out the door with your bags", 0.06, 2.1),
        ("Walkin' out the door with your bags", 0.06, 2.1),
        ("Walkin' out the door with your bags", 0.06, 2.1)
    ]

    # i= line index
    for i, (line, charDelay, lineDelay) in enumerate(lines):
        for char in line:
            print(char, end="",flush=True) #flush stdout
            sleep(charDelay)

        sleep(lineDelay)
        if i != 1:
            print()

if __name__ == "__main__":
    main()