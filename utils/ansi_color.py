def c(code: int) -> str:
    return f"\033[{code}m"

FOREGROUND = {
    "dark gray": c(90), 
    "red": c(91), 
    "green": c(92), 
    "yellow": c(93), 
    "blue": c(94), 
    "pink": c(95),
    "cyan": c(96), 
    "white": c(97), 
    "black": c(30), 
    "dark red": c(31), 
    "dark green": c(32), 
    "orange": c(33),
    "dark_blue": c(34), 
    "purple": c(35), 
    "dark_cyan": c(36), 
    "light gray": c(37)
}

BACKGROUND = {
    "dark gray": c(100), 
    "red": c(101), 
    "green": c(102), 
    "yellow": c(103), 
    "blue": c(104), 
    "pink": c(105),
    "cyan": c(106), 
    "white": c(107), 
    "black": c(40), 
    "dark red": c(41), 
    "dark green": c(42), 
    "orange": c(43),
    "dark_blue": c(44), 
    "purple": c(45), 
    "dark_cyan": c(46), 
    "light gray": c(47)
}

EXTRA_ANSI = {
    "italic": c(3), 
    "flash": c(6)
}

del c