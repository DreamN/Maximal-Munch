from maximalmunch import to_token

str_test = 'doubdoublezADdoubleDoubledo'
regex = {'do': 'T_DO',
         'double': 'T_Double',
         '[a-zA-Z]': 'T_Mystery'}

result = to_token(str_test, regex)
print('\n')
print('Word:\n' + str_test + '\n\n')
print('Regex:\n' + str(regex) + '\n')
for r in result:
    print(r[0] + ' : ' + r[1])
