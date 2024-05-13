from server import *
import webbrowser


def main():
    print("started!")
    webbrowser.open_new_tab('http://127.0.0.1:5000')
    app.run()
    return 0

if __name__ == "__main__":
    main()