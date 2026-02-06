#The core functions of the word counter, but for text files only.
#Will get the output in a list

def freq_count(search_str, word_list):
    templist = []
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
        templist.append(f"{temp2} {count}")
    return templist


def filewordcounthost(substring, path):
    toSearch = substring
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
    result = freq_count(toSearch, script_list)
    return result

# example syntax for this function: print(filewordcounthost("grief", "romeo.txt"))
