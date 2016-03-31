import os
import random


def mode_select():
    selection = raw_input("Encrypt (e) or Decrypt (d)?")
    selection = selection[0]
    selection = selection.lower()
    return selection


def unscramble_files():
    file_list = os.listdir(directory)
    print(file_list)
    print("Number of files:" + str(len(file_list)))
    count = 1
    for file_name in file_list:
        old = directory + "/" + file_name
        new = old.translate(None, "0123456789")
        os.rename(old, new)
        print(str(count) + ":" + old + " was renamed to " + new)
        count += 1


def scramble_files():
    file_list = os.listdir(directory)
    print(file_list)
    print("Number of files:" + str(len(file_list)))
    count = 1
    for file_name in file_list:
        random_start = str(random.randrange(0, 100, 1))
        random_end = str(random.randrange(0, 100, 1))
        old = directory + "/" + file_name
        if len(file_name.split()) > 1:
            split_words = file_name.split()
            for i in range(0, len(split_words) - 1):
                random_mid = str(random.randrange(0, 10, 1))
                split_words[i] += random_mid
            file_name = " ".join(split_words)
        file_name = file_name.split(".")
        new = directory + "/" + random_start + file_name[0] + random_end + ".jpg"
        os.rename(old, new)
        print(str(count) + ":" + old + " was renamed to " + new)
        count += 1


directory = "alphabet"
mode = mode_select()
performed_action = False

while not performed_action:
    if mode == "e":
        scramble_files()
        performed_action = True
    elif mode == "d":
        unscramble_files()
        performed_action = True
    else:
        print("Bad input")
