from teasharp.utils.cool_print import cool_print

def hlp() -> None:
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
            cool_print('It will return "Some funny text!" on the screen.')
            cool_print('But if you define a variable (for example "to_show" as "Something to show!")')
            cool_print('It will show contents of the variable you named')
            cool_print('For example: if you define variable "text" to "Somehing to show",')
            cool_print('And write "print text" it will show "Somehing to show"')

        elif c == "dir":
            cool_print('Command "dir" can show all variables you have!')
            cool_print('For example: if you have two variables "com" and "var"')
            cool_print('And print "dir", you will see "com, var"')

        elif c == "":
            break

        else:
            print(f'TeaSharp doesn\'t have a command {c}. If you wanna exit: just type blank input.')