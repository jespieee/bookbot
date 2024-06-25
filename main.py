def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path} ---")
        print(f"{numWordsinString(file_contents)} words found in the document")
        print("\n\n")
        char_dict = numCharsinString(file_contents)
        sorted_list = dictToSortedList(char_dict)
        for char in sorted_list:
            if not char["char"].isalpha():
                continue
            print(f"The '{char['char']}' character was found {char['num']} times")
        print("--- End report ---")

def numWordsinString(str):
    return len(str.split())

def numCharsinString(str):
    char_dict = {}
    lower_str = str.lower()
    for c in lower_str:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def sortOn(d):
    return d["num"]

def dictToSortedList(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sortOn)
    return sorted_list

main()