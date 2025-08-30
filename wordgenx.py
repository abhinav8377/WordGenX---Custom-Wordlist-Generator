#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WordGenX - Advanced Custom Password Generator
Author: Abhinav
Repo: https://github.com/abhinav8377/WordGenX
License: MIT
"""

import argparse
import random
import string

BANNER = r"""
__        __   _                         ____  __
\ \      / /__| | ___ ___  _ __ ___   __| ___|/ _|_   _
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _` | | | |_| | | |
  \ V  V /  __/ | (_| (_) | | | | | | (_| | | |  _| |_| |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\__,_|_| |_|  \__, |
                                                   |___/ 
     🔑 WordGenX - Unpredictable Custom Password Generator
"""

LEET_MAP = {
    "a": ["a", "@", "4"],
    "e": ["e", "3"],
    "i": ["i", "1", "!"],
    "o": ["o", "0"],
    "s": ["s", "$", "5"],
    "t": ["t", "7"],
}

SPECIALS = list("!@#$%^&*()-_=+[]{};:,<.>/?")

def leet_transform(word):
    result = ""
    for ch in word:
        if ch.lower() in LEET_MAP and random.choice([True, False]):
            result += random.choice(LEET_MAP[ch.lower()])
        else:
            result += ch
    return result

def insert_specials(word, specials, count=1):
    word = list(word)
    for _ in range(count):
        pos = random.randint(0, len(word))
        word.insert(pos, random.choice(specials))
    return "".join(word)

def random_case(word):
    return "".join(random.choice([ch.upper(), ch.lower()]) for ch in word)

def reverse_or_duplicate(word):
    choice = random.choice(["reverse", "duplicate", "none"])
    if choice == "reverse":
        return word[::-1]
    elif choice == "duplicate":
        return word * 2
    return word

def generate_passwords(seeds, length, count, specials, leet, complexify):
    passwords = set()

    for _ in range(count):
        base = random.choice(seeds)

        if leet:
            base = leet_transform(base)

        if complexify:
            base = random_case(base)
            base = reverse_or_duplicate(base)
            base = insert_specials(base, specials, random.randint(1, 3))

        # ensure min length by padding numbers/specials if needed
        while len(base) < length:
            base += random.choice(string.digits + "".join(specials))

        passwords.add(base[:length])  # truncate if too long

    return list(passwords)


def main():
    print(BANNER)

    parser = argparse.ArgumentParser(
        description="WordGenX - Advanced Custom Password Generator"
    )
    parser.add_argument("-w", "--words", nargs="+", required=True, help="Seed words (e.g., abhinav mahakal hacker)")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("-c", "--count", type=int, default=20, help="How many passwords to generate (default: 20)")
    parser.add_argument("--leet", action="store_true", help="Enable leetspeak mangling")
    parser.add_argument("--complex", action="store_true", help="Enable complex transformations (specials inside, random case, reverse, duplicate)")
    parser.add_argument("-s", "--specials", nargs="+", default=SPECIALS, help="Custom special characters (default: full set)")
    parser.add_argument("-o", "--output", help="Save passwords to file")

    args = parser.parse_args()

    passwords = generate_passwords(
        seeds=args.words,
        length=args.length,
        count=args.count,
        specials=args.specials,
        leet=args.leet,
        complexify=args.complex,
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("\n".join(passwords))
        print(f"[+] Saved {len(passwords)} passwords to {args.output}")
    else:
        for pwd in passwords:
            print(pwd)
        print(f"\n[+] Generated {len(passwords)} unpredictable passwords")


if __name__ == "__main__":
    main()
