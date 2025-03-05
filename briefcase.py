from tkinter import *


root = Tk()
root.title("Brifecase editor")
root.geometry("800x600")
root.iconbitmap("Brifecase.ico")
	
root.option_add("*tearOff", FALSE)

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

main_menu = Menu()
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Viev")
main_menu.add_cascade(label="Help")

root.config(menu=main_menu)
root.mainloop()
