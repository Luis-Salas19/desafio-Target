def inverte_string(string):
    for i in string[::-1]:
        print(i, end='')

string = str(input('Digite algum texto:'))
inverte_string(string)
