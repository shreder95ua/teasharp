import os 
import sys
import platform as pl

from colorama import init
from random import choice
from time import sleep

from os import path

from utils.help import hlp
from utils.cool_print import cool_print
from utils.ansi_color import FOREGROUND, BACKGROUND, EXTRA_ANSI

ver = 1.4
init()

username = 0
echo_on_mode = False

Procedures = {}
code_list = {}
variables = {}
imported_modules = []


title = '''\033[30m\033[106m █████ ████   █     ████ █   █   █   ███  ███   
\033[46m   █   █     ███   █     █   █  ███  ████ ████  
\033[104m   █   ████  ███    ███  █████ █████ ███  ███   
\033[44m   █   █     █ █       █ █   █ █   █ █ █  █     
\033[43m   █   ████ █   █  ████  █   █ █   █ █  █ █     
 ███████████     ██████████████████████████████ 
                                                
              PRAY WITH UKRAINE!                
\033[0m\033[92mlmao, who needs licenses? 2022 3 march-iNfInItY. Shreder95ua!
'''

color = "green"
object_sel = "meta_cons"

objects = {

    "meta_cons": {
        "type": "console", 
        "deletable": False
    }, 

    "meta_bg": {
        "type": "bg", 
        "deletable": False,
        "tile": "X", 
        "height": 6, 
        "width": 12, 
        "fgcolor": "red", 
        "bgcolor": "white", 
        "BGorFG": False
    }

}

def cls() -> None:
    os.system("cls" if pl.system() == "Windows" else "clear")


def bgconf(dat: list, cnl: str = "bg") -> None:

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


def run(s: int = 1) -> None:

    try:
        
        cd = dict(list(code_list.items())[s-1:len(list(code_list.items()))])
        
        for i in range(0,len(cd)):
        
            command = list(cd.values())[i]

            try:
                
                thing = interpretator(command,current_line=i,is_run=True)

                if thing != None:
                    run(s=thing)
                    break
            
            except RecursionError:
                print("\nMaximum recursion!")
                print("Stopping the script...")
                break

    except KeyboardInterrupt:
        print("\nOops! You accidentaly pressed Ctrl+C!")


def interpretator(com_str: str, current_line: int, is_run: bool = False) -> any:

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

            if data:
                code_list[code_num] = " ".join(data)
            
            else:
                del code_list[code_num]

            if not iva:
                return

        except KeyError:
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
                print(f"Hi, {username}! Nice to meet you.")
            
            print(f'Are you a begginer, {username}? Try command "help".')
            print(f"It contains some help for you, {username}!")

        elif com == "dir":
            
            if variables:
                for i in range(0,len(variables)):
                    print(list(variables.keys())[i]+":",list(variables.values())[i]+";")
            
            else:
                print("Oh no! You've got stinky'd!")

        elif com == "print":
            
            try:
                print(variables["_".join(data)])
            
            except:
                print(com_str.removeprefix(cnl+" ").replace("\\n","\n"))

        elif com == "read" and "file" == data[0].lower():
            with open(" ".join(data[1:(" ".join(data).lower()).split().index("as")])) as file:
                variables[" ".join(data[(" ".join(data).lower()).split().index("as")+1:len(data)])]=file.read()

        elif com == "write":
            
            if "file" == data[0].lower():
                with open(" ".join(data[1:(" ".join(data).lower()).split().index("as")]),'w') as file:
                    file.write(" ".join(data[(" ".join(data).lower()).split().index("as")+1:len(data)]))

            else:
                try:
                    print(variables["_".join(data)],end="")
                except:
                    print(com_str.removeprefix(cnl+" ").replace("\\n","\n"),end='')

        elif com == "username":

            if data:
                username = " ".join(data)

            else:
                print(username if username else str(interpretator("hi")) * 0)

        elif com == "py":
            
            try:
                exec(" ".join(data))
            
            except Exception as e:
                print("Error:", e)

        elif com == "obj":

            try:
                objects["_".join(data)]
                object_sel = "_".join(data)
            
            except KeyError:
                
                if data == []:
                    print(object_sel)
                
                else:
                    print(f"I don't know object {' '.join(data)}. Maybe try to create it?")
        
        elif com == "about":

            if pl.system() == "Windows":
                
                if int("".join(pl.python_version().split(".")[0:2])) > 37:
                    runon = [pl.system(), pl.version(), "IoT editon" if pl.win32_is_iot() else pl.win32_edition()]
                
                else:
                    runon = [pl.system(), pl.version()]

            elif pl.system() == "":
                runon = ["?"]

            else:
                runon = [pl.system(), pl.version()]

            print(f"Tea Sharp ver.{ver}")
            print(f"Python version: {pl.python_version()}")
            print(f"Running on {' '.join(runon)}")

        elif com == "look":

            looknoobj = ""

            for _row in range(0,objects["meta_bg"]["height"]):
                for _col in range(0,objects["meta_bg"]["width"]):
                    looknoobj = looknoobj + BACKGROUND[objects["meta_bg"]["bgcolor"]] + FOREGROUND[objects["meta_bg"]["fgcolor"]] + objects["meta_bg"]["tile"] + "\033[0m"

                looknoobj = looknoobj + "\n"

            print(looknoobj)

        elif com == "delete":
            
            if data == []:
                objtodel = object_sel
            
            else:
                objtodel = "_".join(data)
            
            try:
                
                if objects[objtodel]["deletable"]:
                    del objects[objtodel]
                
                else:
                    print(FOREGROUND["red"] + EXTRA_ANSI["flash"] + "ACCESS DENIED\033[0m")
            
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
                    while True:
                        print(FOREGROUND[choice(list(FOREGROUND.keys()))] + " ".join(data),end='')

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
                
                for lines in range(0,len(opcode)):
                    interpretator(opcode[lines],current_line,is_run=True)
                
                file.close()
        
        elif com == "save":

            filename = " ".join(data)
            
            with open(filename, "w") as file:

                tosave = ""
                
                for lines in code_list:
                    tosave = tosave + code_list[lines]
                    if lines != len(list(code_list.keys())):
                        tosave = tosave + "\n"

                file.write(tosave)

        elif com == "list":
            
            if code_list:
                for num in range(0, len(code_list)):print(list(code_list)[num]+":", code_list[list(code_list.keys())[num]])

            else:
                print("Looks like you didn't wrote any code!")

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

                    try: 
                        return int("".join(data))
                    
                    except: 
                        pass
        
        elif com == "help":
            hlp()
        
        elif com == "if":
            
            try:
                
                detect = "_".join(data[0:data.index("then")]) # idk how it's in english     qoq
                
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

        elif com == "from":
            
            if is_run:

                _from = int(data[0])
                to = int(data[2])
                
                try:
                    _as = " ".join(data[4:len(data)-(1if"do"in data else 0)])

                except:
                    _as = 0

                todo = []
                count = 0

                while True:

                    command = list(code_list.values())[(current_line + 1):len(code_list)][count]

                    if command.lower() == "end":
                        break

                    todo.append(command)
                    count += 1

                for i in range(_from,to+1):
                    for command in range(0,len(todo)):
                        
                        interpretator(todo[command],command)
                        
                        if _as != 0: 
                            variables[_as] = i

        elif com == "while":

            if is_run:
                
                condition = data
                
                if condition[len(data)-1]=="do":
                    del condition[len(data)-1]
                
                todo = []
                count = 0
                
                while True:
                    
                    command = list(code_list.values())[current_line+1:len(code_list)][count]
                    
                    if command.lower() == "end":
                        break
                    
                    todo.append(command)
                    count += 1

                while True:
                    
                    try:
                        if bool(variables["_".join(condition)]):
                            break

                    except KeyError:
                        if bool("_".join(condition)):
                            break

                    for command in range(0, len(todo)):
                        interpretator(todo[command], command)

        elif com == "import":

            if len(com_list) > 1:

                try:

                    with open(" ".join(data)) as file_to_import:
                        exec(file_to_import.read())

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
                    variables[cnl] = " ".join(data).replace("\\n","\n")
        
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
        
        elif com=="end":
            pass

        elif com_str.lower() in Procedures:
            Procedures[com_str.lower()]()
        
        else:
            print(f"Nice drink! But it's weird. I've never drank it before. {com_str}")
        
        del com,com_list, com_str, cnl


if __name__ == '__main__':
    
    if sys.version_info[0:2] < (3, 7):

        print('\033[30m\033[43m',end='')
        cool_print(''' █████ ████   █     ████ █   █   █   ███  ███   
    █   █     ███   █     █   █  ███  ████ ████  ''',title=True)
        print('\033[41m',end='')
        cool_print('''    █   ████  ███    ███  █████ █████ ███  ███  
    █   █     █ █       █ █   █ █   █ █ █  █     
        █   ████ █   █  ████  █   █ █   █ █  █ █    
    ██████████████████████████████████████████████  ''',title=True)
        print("\033[0m",end='')
        cool_print(f"Warning! Your Python version is {pl.python_version()}!")
        cool_print("This version does not have features that were added in Python 3.7:")
        cool_print("sorting, getting information about Windows version, and many-many others.")
        cool_print("You can get a new interpreter on https://python.org/downloads")
        cool_print("But if you think that you can still use TeaSharp you just using")
        cool_print("emulator, or python interpretator that don't shows any kind")
        cool_print("of versions, or this is long-long future, where versions, are not allowed,")
        cool_print("you can run this interpreter.")
        sleep(0.4)

        cool_print("Will you run TeaSharp? ", noend=True)
        sleep(0.4)

        if input("[Y/n]: ") == "Y":

            cool_print("TeaSharp can crash in any moment! You really wanna run TeaSharp?")
            
            if input("[Y/n]: ") == "Y":
                cool_print("This is your last warning, the TeaSharp will crash, and...")
                cool_print("And... I don't know... It can do... Okay. You can run Teasharp.")
                cool_print("But at own risk...", slow=True)
                cls()
            
            else:
                exit()
    
    if sys.argv[-1][-4:] == '.tsh' and len(sys.argv) == 2:
        
        with open(os.path.abspath(sys.argv[-1])) as file:
            
            lines = [line for line in file.readlines() if line != '\n' and line != '\r\n' and line != '\r']
            
            for (line_num, line) in enumerate(lines):
                interpretator(line.rstrip(), line_num)
    
    elif len(sys.argv) != 2:
        
        print(title)

        while True:

            print(FOREGROUND[color], end = '')
            
            try:
                
                if echo_on_mode:
                    com_str = input()
                
                else:
                    com_str = input(f"[{object_sel}]: ")
                
                interpretator(com_str, 0)

            except KeyboardInterrupt:
                print("\nExiting... (You pressed Ctrl+C)")
                exit()
