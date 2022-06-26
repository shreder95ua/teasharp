ver = 1.2
from time import sleep
def cool_print(string, noend=False,title=False,slow=False):
    if title:
        for s in string:
            print(s,end="")
            sleep(0.005)
    else:
        for s in string:
            print(s,end="")
            sleep(0.05*(4 if slow else 1))
            if s==" ":
                sleep(0.05*(4 if slow else 1))
            elif s==",":
                sleep(0.2*(4 if slow else 1))
            elif s=="!":
                sleep(0.4*(4 if slow else 1))
    if not noend:
        print()
    sleep(0.4*(4 if slow else 1))
from colorama import init
init()
from os import system as sys
from os import path
#from keyboard import read_key
import platform as pl
Procedures = {}
imported_modules = []
def cls():
    sys("cls" if pl.system()=="Windows" else "clear")
if int("".join(pl.python_version().split(".")[0:2])) < 37:
    print('\033[30m\033[43m',end='')
    cool_print(''' █████ ████   █     ████ █   █   █   ███  ███   
   █   █     ███   █     █   █  ███  ████ ████  ''',title=True)
    print('\033[41m',end='')
    cool_print('''    █   ████  ███    ███  █████ █████ ███  ███  
   █   █     █ █       █ █   █ █   █ █ █  █     
    █   ████ █   █  ████  █   █ █   █ █  █ █    
██████████████████████████████████████████████  ''',title=True)
    print("\033[0m",end='')
    cool_print("Warning! Your Python version is "+pl.python_version()+"!")
    cool_print("This version is not have things, that was added in Python 3.7,")
    cool_print("like sorting, getting information about Windows version, and many-many others.")
    cool_print("You can get a new interpretator on https://python.org/downloads")
    cool_print("But if you think, you can still use TeaSharp, you just using")
    cool_print("emulator, or python interpretator that don't shows any kind")
    cool_print("of versions, or this is long-long future, where versions, are not allowed,")
    cool_print("you can run this interpretator.")
    sleep(0.4)
    cool_print("Will you run TeaSharp? ", noend=True)
    sleep(0.4)
    if input("[Y/n]: ") == "Y":
        cool_print("TeaSharp can crash in any moment! You really wanna run TeaSharp?")
        if input("[Y/n]: ") == "Y":
            cool_print("That is your last warning, the TeaSharp will crash, and...")
            cool_print("And... I don't know... It can do... Okay. You can run Teasharp.")
            cool_print("But at own risk...",slow=True)
            cls()
        else:
            exit()
    else:
        cool_print("Oh. That was fast.")
        exit()
def hlp():
    print('''|--------------------|
|     TEA SHARP      |
|TeaSharp help center|
|--------------------|
|     2022.03.27     |
|--------------------|
| TeaSharp is BASIC- |
| based programming  |
| language, that is  |
| easy to learn.     |
----------------------''')
    while True:
        c = input("What command help you need? ").lower()
        if c == "print":
            cool_print('Command print is used to "print" text.')
            cool_print('You can write text, like this:')
            cool_print('print Some funny text!')
            cool_print('What will return "Some funny text!" on the screen.')
            cool_print('But if you assign a variable (for example "to_show" as "Something to show!")')
            cool_print('It will show contents of the variable you named')
            cool_print('For example: if you assign variable "text" to "Somehing to show",')
            cool_print('And write "print text" it will show "Somehing to show"')
        elif c == "dir":
            cool_print('Command "dir" can show all variables you have!')
            cool_print('For example: if you have two variables "com" and "var"')
            cool_print('And print "dir", you will see "com, var"')
        elif c == "":
            break
        else:
            print('TeaSharp doesn\'t have a command "' + c + '". If you wanna exit: just type blank input.')
def c(code):
    return "\033[" + str(code) + "m"
init()
title = '''\033[30m\033[106m █████ ████   █     ████ █   █   █   ███  ███   
\033[46m   █   █     ███   █     █   █  ███  ████ ████  
\033[104m   █   ████  ███    ███  █████ █████ ███  ███   
\033[44m   █   █     █ █       █ █   █ █   █ █ █  █     
\033[43m   █   ████ █   █  ████  █   █ █   █ █  █ █     
 ███████████     ██████████████████████████████ 
                                                
              PRAY WITH UKRAINE!                
\033[0m\033[92mlmao, who needs licenses? 2022 3 march-iNfInItY. Shreder95ua!
'''
fg = {"dark gray": c(90), "red": c(91), "green": c(92), "yellow": c(93), "blue": c(94), "pink": c(95),
      "cyan": c(96), "white": c(97), "black": c(30), "dark red": c(31), "dark green": c(32), "orange": c(33),
      "dark_blue": c(34), "purple": c(35), "dark_cyan": c(36), "light gray": c(37)}
bg = {"dark gray": c(100), "red": c(101), "green": c(102), "yellow": c(103), "blue": c(104), "pink": c(105),
      "cyan": c(106), "white": c(107), "black": c(40), "dark red": c(41), "dark green": c(42), "orange": c(43),
      "dark_blue": c(44), "purple": c(45), "dark_cyan": c(46), "light gray": c(47)}
extra_ansi = {"italic": c(3), "flash": c(6)}
code_list = {}
del c
color = "green"
object_sel = "meta_cons"
objects = {"meta_cons": {"type": "console", "deletable": False}, "meta_bg": {"type": "bg", "deletable": False, "tile": "X", "height": 6, "width": 12, "fgcolor": "red", "bgcolor": "white", "BGorFG": False}}
def bgconf(dat, dat_str, cnl="bg"):
    global objects
    if dat == []:
        print(cnl)
    else:
        st = dat[0]
        if len(st) < 3:
            try:
                print(objects["meta_bg"][st])
            except KeyError:
                print("No setting " + st + ". Do You Understand?")
        else:
            data = dat[1:len(dat)]
            if st == "tile":
                objects["meta_bg"][st] = " ".join(data)
            elif st == "width" or st == "height":
                try:
                    objects["meta_bg"][st] = int(data[0])
                except ValueError:
                    print(data[0] + " is not a number!")
def run(s=1):
    try:
        cd = dict(list(code_list.items())[s-1:len(list(code_list.items()))])
        for command in cd:
            try:
                thing = interpretator(cd[command],is_run=True)
                if thing != None:
                    run(s=thing)
                    break
            except RecursionError:
                print("\nMaximum recursion!")
                print("Stopping the script...")
                break
    except KeyboardInterrupt:
        print("\nOops! You accidentaly pressed Ctrl+C!")
def interpretator(com_str,is_run=False):
    global code_list,echo_on_mode,username,path,object_sel,imported_modules
    code_list = dict(sorted(list(code_list.items()), key = lambda kv: kv[0]))
    if com_str.split() == []:
        if com_str == "":
            print("There's nothing in the cup!")
        else:
            print("I don't want to drink water!")
    else:
        com_list = com_str.split()
        cnl = com_list[0]
        com = cnl.lower()
        try:
            int(com)
            iva = com_list[1] == "=" #is_variable_assign
        except IndexError:
            iva = False
        except ValueError:
            try:
                iva = com_list[1] == "="
            except IndexError:
                iva = False
        if iva:
            data = com_list[2:len(com_list)]
        else:
            data = com_list[1:len(com_list)]
        try:
            code_num = int(com)
            code_list[code_num] = " ".join(data)
            del code_num
            if not iva:
                return
        except:
            pass
        if com == "cookie":
            print("Thanks a bunch for a cookie to my tea!")
        elif com == "hi":
            if username == 0:
                print("Hello! Nice to meet you, user. Can I know your name?")
                username = input("My name is ")
            else:
                print("Hi", username + "! Nice to meet you.")
            print('Are you a begginer,', username + '? Try command "help".')
            print('It contains some help for you,', username + "!")
        elif com == "dir":
            print(", ".join(variables))
        elif com == "print":
            try:
                print(variables["_".join(data)])
            except:
                print(" ".join(data))
        elif com == "username":
            if data == []:
                print(username)
            else:
                username = " ".join(data)
        elif com == "py":
            try:
                exec(" ".join(data))
            except Exception as e:
                print("Error:",e)
        elif com == "obj":
            try:
                objects["_".join(data)]
                object_sel = "_".join(data)
            except KeyError:
                if data == []:
                    print(object_sel)
                else:
                    print("I don't know object " + " ".join(data) + ". Maybe try to create it?")
        elif com == "about":
            if pl.system() == "Windows":
                if int("".join(pl.python_version().split(".")[0:2])) > 37:
                    if pl.win32_is_iot():
                        runon = [pl.system(), pl.version(), "IoT editon"]
                    else:
                        runon = [pl.system(), pl.version(), pl.win32_edition()]
                else:
                    runon = [pl.system(), pl.version()]
            elif pl.system() == "":
                runon = ["?"]
            else:
                runon = [pl.system(), pl.version()]
            print("Tea Sharp ver.", ver)
            print("Python version:", pl.python_version())
            print("Running on", " ".join(runon))
        elif com == "look":
            looknoobj = ""
            for row in range(0,objects["meta_bg"]["height"]):
                for col in range(0,objects["meta_bg"]["width"]):
                    looknoobj = looknoobj + bg[objects["meta_bg"]["bgcolor"]] + fg[objects["meta_bg"]["fgcolor"]] + objects["meta_bg"]["tile"] + "\033[0m"
                looknoobj = looknoobj + "\n"
            print(looknoobj)
        elif com == "del":
            if data == []:
                objtodel = object_sel
            else:
                objtodel = "_".join(data)
            try:
                if objects[objtodel]["deletable"]:
                    del objects[objtodel]
                else:
                    print(fg["red"] + extra_ansi["flash"] + "ACCESS DENIED")
            except KeyError:
                print("No object called" + objtodel + ". Maybe you allready deleted it?")
        elif com == "exit":
            exit()
        elif com == "bg":
            bgconf(data, com_str, cnl)
        elif com == "echo":
            try:
                if data[0] == "on":
                    echo_on_mode = False
                elif data[0] == "off":
                    echo_on_mode = True
                else:
                    from random import choice
                    while True:
                        print(fg[choice(list(fg.keys()))] + " ".join(data),end='')

            except IndexError:
                print("Echo... and...", end='')
                while True:
                    print(end='.')
                    sleep(0.01)
        elif com == "run":
            run()
        elif com == "new":
            code_list = {}
        elif com == "load":
            filename = " ".join(data)
            if path.isfile(filename):
                file = open(filename, "r")
                opcode = file.read().split("\n")
                for lines in opcode:
                    interpretator(lines)
                file.close()
        elif com == "save":
            filename = " ".join(data)
            from os import path
            file = open(filename, "w")
            tosave = ""
            for lines in code_list:
                tosave = tosave + code_list[lines]
                if lines != len(list(code_list.keys())):
                    tosave = tosave + "\n"
            file.write(tosave)
            file.close()
        elif com == "list":
            for num in range(0, len(code_list)):
                print(list(code_list.keys())[num], code_list[list(code_list.keys())[num]])
        elif com == "input":
            try:
                data[0]
                try:
                    data[1:len(data)]
                    variables[com_list[1]] = input(" ".join(data[1:len(data)]) + " ")
                    variables[com_list[1]] = int(variables[com_list[1]])
                except KeyError:
                    input(">")
                except ValueError:
                    variables[com_list[1]] = str(variables[com_list[1]])
            except KeyError:
                input(">")
        elif com == "goto":
            if is_run == True:
                try:
                    return variables["_".join(data)]
                except KeyError:
                    try: return int("".join(data))
                    except: pass
        elif com == "help":
            hlp()
        elif com == "if":
            try:
                detect = "_".join(data[0:data.index("then")]) # idk how it's in english named     qoq
                try:
                    todo = " ".join(data[data.index("then")+1:data.index("else")])
                    els = " ".join(data[data.index("else")+1:len(data)])
                except:
                    todo = " ".join(data[data.index("then")+1:len(data)])
                try:
                    if bool(variables[detect]):
                        interpretator(todo)
                    else:
                        interpretator(els)
                except KeyError:
                    if bool(detect):
                        interpretator(todo)
                    else:
                        interpretator(els)
            except:
                print("What I need to do?")
        elif com_str.lower() == "edit map":
            cls()
            map = ['........']*8
            x=0
            y=0
            while True:
                print('\n'.join(map))
                print('Press Escape to exit')
#                 kp = read_key()
#                 if kp == "esc":
#                     break
#                 elif kp == "down" and y < 9:
#                     y += 1
#                 elif kp == "right" and x < 9:
#                     x += 1
#                 elif kp == "up" and y > 1:
#                     y -= 1
#                 elif kp == "left" and x < 1:
#                     x -= 1
                kp = input("> ").lower()
                if kp == "exit":
                    break
                elif kp == "s" and y < 9:
                    y += 1
                elif kp == "d" and x < 9:
                    x += 1
                elif kp == "w" and y > 1:
                    y -= 1
                elif kp == "a" and x < 1:
                    x -= 1
        elif com == "import":
            if len(com_list) > 1:
                try:
                    file_to_import = open(" ".join(data),"r")
                    exec(file_to_import.read())
                    file_to_import.close()
                    imported_modules.append(" ".join(data))
                except FileNotFoundError:
                    print("File"," ".join(data),'''was not found.
Remember: if the file you wan't to import is not in the TeaSharp folder, you must insert the full path to the file.''')
            else:
                print("; ".join(imported_modules))
        elif iva:
            if len(com_list) < 3:
                print("What I need to assign? If you need to assign something put the data after the equal sign")
            else:
                if data[0] == "True":
                    variables[cnl] = True
                elif data[0] == "False":
                    variables[cnl] = False
                try:
                    if len(com_list) == 3:
                        variables[cnl] = int(com_list[2])
                    else:
                        raise ValueError("It's not a number... But wait! Who reads this? kek")
                except ValueError:
                    variables[cnl] = " ".join(data)
        elif com_str == "who did this all stuff, and why?":
            cls()
            print(f'''\033[103m\033[34m\t\t█▐█▐▌
 Made by        ▌ ▄ ▌
Shreder95ua     ▐█▀█
\t\t█  ▐▌''')
            sleep(2)
            cool_print("> END",slow=True)
            sleep(2)
            cool_print("btw if ur ukrainian check out 5brocks.netlify.com")
            input()
            print("\033[0m")
            cls()
        elif com_str.lower() in Procedures:
            Procedures[com_str.lower()]()
        else:
            print("Nice drink! But it's weird. I never drunk " + com_str)
        del com,com_list,com_str,cnl
variables = {}
print(title)
username = 0
echo_on_mode = False
while True:
    print(fg[color], end = '')
    try:
        if echo_on_mode:
            com_str = input("")
        else:
            com_str = input("[" + object_sel + "]: ")
        interpretator(com_str)
    except KeyboardInterrupt:
        print("\nExiting... (You pressed Ctrl+C)")
        exit()