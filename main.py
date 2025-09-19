from stats import word_count, character_count, dict_sort
import sys

def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    text = get_book_text(filename)
    count = word_count(text)
    char_count = character_count(text)
    dict_list = dict_sort(char_count)
    char_count_sorted = {}
    for dict in dict_list:
        if dict['name'].isalpha():
            char_count_sorted[dict["name"]] = dict["num"]
    char_count_string = ""
    for i in char_count_sorted:
        if i == 'e':
            char_count_string += (f"{i}: {char_count_sorted[i]}")
        else:
           char_count_string += ('\n' + f"{i}: {char_count_sorted[i]}") 
    title_string = "============ BOOKBOT ============"
    word_count_title = "----------- Word Count ----------"
    char_count_title = "--------- Character Count -------"
    analyze_string = f"Analyzing book found at {filename}"
    word_count_string = f"Found {count} total words"
    end_string = "============= END ==============="
    report_items = [title_string, analyze_string, word_count_title, word_count_string, char_count_title, char_count_string, end_string]
    report_string = ""
    for item in report_items:
        if item == title_string:
            report_string += item
        else:
            report_string += ('\n' + item)
    print(report_string)
        


main()