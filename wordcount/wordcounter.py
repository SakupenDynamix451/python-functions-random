def freq_count(search_str, word_list):
    for x in range(len(word_list)):
        index = 0 # position
        count = 0 # counter
        temp = word_list[x]
        temp2 = word_list[x]
        while index != -1:
            index = temp.find(search_str)
            if index != -1:
                count += 1
                temp = temp[index+1:]
        print(temp2, count)

def main():
    print("Welcome to the Word Counter!")
    path = input("Enter filename: ")
    toSearch = input("Enter substring to search for: ")
    fileToUse = open(path)
    stuff = fileToUse.read()
    word_list = stuff.split()
    print("")
    script_list = []
    for x in range(len(word_list)):
        word = word_list[x]
        word = word.lower()
        if word_list[x] not in script_list:
            script_list.append(word)
    script_list.sort()
    freq_count(toSearch, script_list)

main()
