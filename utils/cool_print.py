from time import sleep

def cool_print(string: str, noend: bool = False, title: bool = False, slow: bool = False) -> None:

    if not title:
        for s in string:

            time_multiplier = 4 if slow else 1

            print(s, end="")
            sleep(0.05 * time_multiplier)

            if s == " ":
                sleep(0.05 * time_multiplier)

            elif s == ",":
                sleep(0.2 * time_multiplier)

            elif s == "!":
                sleep(0.4 * time_multiplier)

        return

    for s in string:
        print(s, end="")
        sleep(0.005)

    if not noend:
        print()

    sleep(0.4 * time_multiplier)