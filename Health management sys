def getdate():
        import datetime
        return datetime.datetime.now()


    time = getdate()


    def food():
        a = input('enter the food you are eating')
        f = open(foods, 'a')
        f.write('[' + str(time) + ']' + a + '\n')
        f.close()


    def Exercise():
        a = input('enter the Exercise you are doing')
        f = open(Exer, 'a')
        f.write('[' + str(time) + ']' + a + '\n')
        f.close()
        
        
to_do = int(input('what would to like to do\n'
                  'Press 1 : To Log Data\n'
                  '      2 : To Retrieve Data\n'
                  '      >>>>>>>>>>>>>>>>>>>'))
name = int(input('who\'s file you want to acess\n '
                 'Press 1 : Harry\n'
                 '       2 : Rohan\n'
                 '       3 : Hammad\n'
                 '       >>>>>>>>>>>>'))

file = int(input('which file you would like to acess\n'
                 'Press 1 : Food\n'
                 '      2 : Exercise\n'
                 '      >>>>>>>>>>>>>>'))
if to_do == 2:
    if file == 1:
        if name == 1:
            foods = 'Harry\'s Food.txt'
        elif name == 2:
            foods = 'Rohan\'s Food.txt'
        elif name == 3:
            foods = 'Hammad\'s Food.txt'
        else:
            print('pls choose a correct number')
        with open(foods) as f:
            print(f.read())


    elif file == 2:
        if name == 1:
            Exer = 'Harry\'s Exe.txt'
        elif name == 2:
            Exer = 'Rohan\'s Exe.txt'
        elif name == 3:
            Exer = 'Hammad\'s Exe.txt'
        else:
            print('pls choose a correct number')
        with open(Exer) as f:
            print(f.read())

elif to_do == 1:
    
   if file == 1:
        if name == 1:
            foods = 'Harry\'s Food.txt'
        elif name == 2:
            foods = 'Rohan\'s Food.txt'
        elif name == 3:
            foods = 'Hammad\'s Food.txt'
        else:
            print('pls choose a correct number')
        food()

    elif file == 2:
        if name == 1:
            Exer = 'Harry\'s Exe.txt'
        elif name == 2:
            Exer = 'Rohan\'s Exe.txt'
        elif name == 3:
            Exer = 'Hammad\'s Exe.txt'
        else:
            print('pls choose a correct number')
        Exercise()

    else:
        print('pls choose a correct number')
