try:
    file = open('nowf','r+')
except Exception as e:
    print(e)
    response = input('do you want to create a new file:')
    if response == 'Y':
        file = open('nowf','w')
    else:
        pass
else:
    file.write('you are write an content')
    file.close()