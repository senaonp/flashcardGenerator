import tkinter as tk
import datetime as dt
import os

# config variables
entries = [] # flashcard entries
maxDisplay = 10 # number of entries to display in GUI
delimiter = ":" # delimiter for front and back in generated file
folderPath = "./decks/" # folder path for generated files
filename = f'{folderPath}{dt.datetime.now().strftime("%Y%m%d_%H%M%S")}_deck{len(os.listdir(folderPath))+1}.txt' # filename to generate
allowBlankCards = False # allow blank front or back entries in a card

# window instance
w=tk.Tk()

frontEntry = tk.StringVar()
backEntry = tk.StringVar()
entriesText = tk.StringVar()
infoText = tk.StringVar()

# add card to session
def addCard():
	if validateCard():
		entries.append([frontEntry.get().strip(),backEntry.get().strip()])
		entriesText.set('saved entries\n' + "\n".join([str(entry) for entry in entries[-maxDisplay:][::-1]]))
		doAfterAddCard()

# workflow after adding card
def doAfterAddCard():
	frontEntry.set("")
	backEntry.set("")

# validate card entry
def validateCard():
	infoText.set('')
	if allowBlankCards:
		return True
	isValid = (frontEntry.get().strip() != "" and backEntry.get().strip() != "")
	if not isValid:
		infoText.set('error: front or back entries cannot be blank')
	return isValid

# save entries into deck and exit program
def saveCards():
	fileText = "\n".join([delimiter.join(entry) for entry in entries])
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(fileText)
		file.close()
	infoText.set(f'saved file:\n({filename})')
	

# labels
tk.Label(w, text="Front").grid(row=0, column=0)
tk.Label(w, text="Back").grid(row=0, column=1)
entriesLabel = tk.Label(w, textvariable=entriesText).grid(row=3, column=0, columnspan=2)
infoLabel = tk.Label(w, textvariable=infoText, padx=5, pady=5).grid(row=4, column=0, columnspan=2)

# front and back input fields
front = tk.Entry(w, textvariable=frontEntry).grid(row=1, column=0)
back = tk.Entry(w, textvariable=backEntry).grid(row=1, column=1)

# add card button
tk.Button(w, text="Add Card", command=addCard).grid(row=2, column=0, pady=5)
# save cards button
tk.Button(w, text="Save", command=saveCards).grid(row=2, column=1, pady=5)

w.wm_attributes("-topmost", 1)
w.mainloop()
