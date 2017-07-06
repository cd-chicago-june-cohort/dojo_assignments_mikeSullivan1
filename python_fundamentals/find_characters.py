def find_characters(some_list,ch):
    list_w_chars =[]
    for x in some_list:
        if ch in x:
            list_w_chars.append(x)
    return list_w_chars

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

print find_characters(word_list, char)