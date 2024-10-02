
def update_count(word, letter_count):
    for character in word:
        lower_case_char = character.lower()
        if lower_case_char in letter_count:
            letter_count[lower_case_char] = letter_count[lower_case_char] + 1
        else:
            letter_count[lower_case_char] = 1

def sort_on(dict):
    return dict["count"]

def print_report(letter_count, wordcount):
    print('--- Begin report of books/frankenstein.txt ---')
    
    print(f"{wordcount} words found in the document\n")
    char_list = [{'char': char, 'count': count} for char, count in letter_count.items()]
    char_list.sort(reverse=True, key=sort_on)
    for char_count_obj in char_list:
        char = char_count_obj['char']
        if char.isalpha():
            print(f"The '{char}' character was found {letter_count[char]} times")
    print("--- End report ---")

   

def main():

    letter_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            update_count(word, letter_count)

    print_report(letter_count, len(words))


main()