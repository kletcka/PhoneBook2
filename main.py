from tkinter import *
from tkinter.ttk import *
import functions
import json
import initialization


def main():
    initialization.start()
    window = Tk()
    window.title = "Book"
    window.resizable(width=False, height=False)
    dictionary = {}


    with open('root.json', 'r', encoding='utf-8') as read_file:
        size = dict(json.load(read_file))
        x = size["x"]
        y = size["y"]
        window.geometry(f"{x}x{y}")

    with open('configure.json', 'r', encoding='utf-8') as read_file:
        dictionary = dict(json.load(read_file))

    for i in list(dictionary.keys()):
        t = functions.create_object(name=dictionary[i]["name"], pos=dictionary[i]["pos"], ob_type=dictionary[i]
                                    ["type"], size=dictionary[i]["size"], id=i, g_id=dictionary[i]["command_id"])
        for j in t:
            j[0].place(x=str(j[1][0]), y=str(j[1][1]))

    window.mainloop()

if __name__ == "__main__":
    main()
