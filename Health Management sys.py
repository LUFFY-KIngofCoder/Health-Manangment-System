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
def long():
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
        def getdate():
            import datetime
            return datetime.datetime.now()


        time = getdate()


        def food(file_name):
            a = input('enter the food you are eating')
            f = open(file_name, 'a')
            f.write('[' + str(time) + ']' + a + '\n')
            f.close()


        def Exercise(file_name):
            a = input('enter the Exercise you are doing')
            f = open(file_name, 'a')
            f.write('[' + str(time) + ']' + a + '\n')
            f.close()


        if file == 1:
            if name == 1:
                foods = 'Harry\'s Food.txt'
            elif name == 2:
                foods = 'Rohan\'s Food.txt'
            elif name == 3:
                foods = 'Hammad\'s Food.txt'
            else:
                print('pls choose a correct number')
            food(foods)

        elif file == 2:
            if name == 1:
                Exer = 'Harry\'s Exe.txt'
            elif name == 2:
                Exer = 'Rohan\'s Exe.txt'
            elif name == 3:
                Exer = 'Hammad\'s Exe.txt'
            else:
                print('pls choose a correct number')
            Exercise(Exer)

        else:
            print('pls choose a correct number')

def short():
    names = ['Harry', 'Rohan', 'Hammad']
    files = ["Food", "Exercise"]

    file = f"{names[name - 1]} {files[file - 1]}.txt"

    if to_do == 1:
        def getdate():
            import datetime
            return datetime.datetime.now()

        with open(file, 'a') as f:
            info = input("enter the msg>>>>")
            f.write(f"[{getdate()}] {info}")
    else:
        with open(file) as f:
            print(f.read())
