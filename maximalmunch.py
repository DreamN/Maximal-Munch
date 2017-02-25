import re


def to_token(str, regex_dict):
    str_len = 1
    token = ''
    word = ''
    wordlen = 0
    result = []
    while str != '':
        c_str = str[:str_len]
        found = False
        for regex in regex_dict:
            token_check = re.compile(regex)
            if token_check.fullmatch(c_str):
                found = True
                token = regex_dict[regex]
                word = c_str
                wordlen = str_len
            elif(not '[' in regex):
                for i in range(len(regex)):
                    token_check = re.compile(regex[:i])
                    if token_check.fullmatch(c_str):
                        found = True

        if(not found and token or str == word):
            result.append([token, word])
            token = ''
            str = str[wordlen:]
            str_len = 0
        str_len += 1
    return result
