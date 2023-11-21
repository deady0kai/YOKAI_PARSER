import module.parser as PS
import interface
def main() -> int:
    interface.Interface(PS.get_html, PS.parse_html)
    return 1
if __name__ == '__main__':
    main()