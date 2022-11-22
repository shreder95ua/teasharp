from time import sleep

def cool_print(string: str, noend: bool = False, title: bool = False, slow: bool = False) -> None:

    if title:
        for s in string:
            print(s, end="")
            sleep(0.005)

    else:
        for s in string:

            print(s, end="")
            sleep(0.05 * (4 if slow else 1))

            if s == " ":
                sleep(0.05 * (4 if slow else 1))

            elif s == ",":
                sleep(0.2 * (4 if slow else 1))

            elif s == "!":
                sleep(0.4 * (4 if slow else 1))

    if not noend:
        print()

    sleep(0.4*(4 if slow else 1))