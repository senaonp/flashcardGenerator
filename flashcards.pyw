import tkinter as tk
import datetime as dt
import os

entries = [] # number of entries
maxDisplay = 10 # number of entries to display in GUI
delimiter = ":" # delimiter for front and back in generated file
folderPath = "./decks/" # folder path for generated files
filename = f'{folderPath}{dt.datetime.now().strftime("%Y%m%d_%H%M%S")}_deck{len(os.listdir(folderPath))+1}.txt' # filename to generate
allowBlankCards = False # allow blank front or back entries in a card

w=tk.Tk()

frontEntry = tk.StringVar()
backEntry = tk.StringVar()
entriesText = tk.StringVar()
errorsText = tk.StringVar()

def addCard():
	if validateCard():
		entries.append([frontEntry.get(),backEntry.get()])
		entriesText.set('saved entries\n' + "\n".join([str(entry) for entry in entries[-10:][::-1]]))
		doAfterAddCard()

def doAfterAddCard():
	frontEntry.set("")
	backEntry.set("")

def validateCard():
	errorsText.set('')
	if allowBlankCards:
		return
	isValid = (frontEntry.get().strip() != "" and backEntry.get().strip() != "")
	if not isValid:
		errorsText.set('error: front or back entries cannot be blank')
	return isValid

def saveAndExit():
	file = open(filename, "w")
	file.write("\n".join([delimiter.join(entry) for entry in entries]))
	file.close()
	exit()

# labels
tk.Label(w, text="Front").grid(row=0, column=0)
tk.Label(w, text="Back").grid(row=0, column=1)
entriesLabel = tk.Label(w, textvariable=entriesText).grid(row=3, column=0, columnspan=2)
errorsLabel = tk.Label(w, textvariable=errorsText, fg='red').grid(row=4, column=0, columnspan=2)

# front and back input fields
front = tk.Entry(w, textvariable=frontEntry).grid(row=1, column=0)
back = tk.Entry(w, textvariable=backEntry).grid(row=1, column=1)

# add card button
tk.Button(w, text="Add Card", command=addCard).grid(row=2, column=0, pady=5)
# save and exit button
tk.Button(w, text="Save and Exit", command=saveAndExit).grid(row=2, column=1, pady=5)

w.wm_attributes("-topmost", 1)
w.mainloop()