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
        # print('\n\n' + "=====================================\n"+str + " :: Current |" + c_str)
        for regex in regex_dict:
            token_check = re.compile(regex)
            if token_check.match(c_str):
                if len(token_check.match(c_str).group()) == len(c_str):
                # print('Found: ' + c_str)
                    found = True
                    token = regex_dict[regex]
                    word = c_str
                    wordlen = str_len

            elif token_check.match(str):
                if len(token_check.match(str).group()) > wordlen:
                    # print('It can be: ' + token_check.match(str).group())
                    found = True

        if(not found and token or str == word):
            # print('Append: ' + word)
            result.append([token, word])
            token = ''
            str = str[wordlen:]
            str_len = 0
        str_len += 1
    return result
