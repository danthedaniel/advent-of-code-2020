#!/usr/bin/env python3


def parse_input(path):
    passwords = []

    with open(path, "r") as input:
        for line in input.readlines():
            rule, password = line.split(': ')
            counts, letter = rule.split(' ')
            low, high = counts.split('-')

            passwords.append((int(low), int(high), letter, password))

    return passwords


def sled_password_valid(low, high, letter, password):
    num_occurances = len([x for x in password if x == letter])
    return num_occurances >= low and num_occurances <= high


def tob_password_valid(low, high, letter, password):
    return (password[low - 1] == letter) != (password[high - 1] == letter)


def main():
    passwords = parse_input("input")
    valid_sled_passwords = [password for password in passwords if sled_password_valid(*password)]
    print(f"Part 1: {len(valid_sled_passwords)}")
    valid_tob_passwords = [password for password in passwords if tob_password_valid(*password)]
    print(f"Part 2: {len(valid_tob_passwords)}")


if __name__ == "__main__":
    main()
