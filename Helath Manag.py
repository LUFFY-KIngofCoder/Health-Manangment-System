to_do = int(input('what would to like to do\n'
                  'Press 1 : To Log Data\n'
                  '      2 : To Retrieve Data\n'
                  '      >>>>>>>>>>>>>>>>>>>'))
name = input('Enter Your Name').lower()

file = int(input('which file you would like to acess\n'
                 'Press 1 : Food\n'
                 '      2 : Exercise\n'
                 '      >>>>>>>>>>>>>>'))

task = ['food','exercise']

file_name = f"{name}'s {task[file-1]}.txt"

if to_do == 2:
    with open(file_name) as f:
        print(f.read())

elif to_do == 1:
    with open(file_name,'a') as f:
        info = input("Enter Data::::")
        def getdate():
            import datetime
            return datetime.datetime.now()
        f.write(f"[{getdate()}] {info}\n")



