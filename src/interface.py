from os import system
def Interface(func_get, func_parse) -> None:
    HTML = ""
    while 1:
        system("cls || clear")
        print("Interface")
        print("[1][GET HTML]")
        print("[2][PARSE HTML]")
        print("[3][EXIT]")
        choice = int(input("[CHOISE][~>]"))
        match choice:
            case 1:
                system("cls || clear")
                print("[WHAT URL YOU WANT TO GET?][:]")
                url = input("[URL][~>]")
                HTML = func_get(url)
                print(HTML)
                input()
            case 2:
                system("cls || clear")
                print("[WHAT TAG YOU WANT TO PARSE?][:]")
                tag = input("[TAG][~>]")
                class_ = input("[TAG CLASS][~>]") 
                print(func_parse(HTML, tag, class_ if class_ != "" else None))
                input()
            case 3:
                break
            case _:
                print("[INVALID CHOISE]")
                input()
