#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# This program is for adding positive numbers


def main():
    # main function for adding positive numbers

    # variables
    total_sum = 0
    # input
    total = input("How many numbers would you like to add: ")
    total = int(total)

    # Process & Input
    for number in range(total):
        sec_num = input("Enter a number to add: ")
        sec_num = int(sec_num)
        if sec_num <= 0:
            continue
        total_sum += sec_num

    # Output
    print(f"Sum of just the positive numbers is = {total_sum}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
