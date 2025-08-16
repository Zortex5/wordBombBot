import pytesseract
import pyautogui as pag
import tkinter as tk

pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract_OCR\\tesseract.exe"

words = []
word_num = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0

def main():
    load_words("wordFile.txt")

    root = tk.Tk()
    frm = tk.ttk.Frame(root, padding=10)
    frm.grid()
    tk.ttk.Label(frm, text="Ward Bumo").grid(column=0, row=0)
    tk.ttk.Button(frm, text="Run", command=run).grid(column=1, row=0)
    tk.ttk.Button(frm, text="Up", command=up).grid(column=1, row=1)
    tk.ttk.Button(frm, text="Reset", command=reset).grid(column=1, row=2)
    tk.ttk.Button(frm, text="Clear", command=clear).grid(column=1, row=3)
    tk.ttk.Button(frm, text="Setup1", command=setup1).grid(column=0, row=4)
    tk.ttk.Button(frm, text="Setup2", command=setup2).grid(column=2, row=4)
    root.mainloop()


def run():
    global word_num
    global x1, x2, y1, y2
    #img = pag.screenshot(region=(960, 600, 1020, 620))
    img = pag.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    print(f"width = {x2 - x1}")
    print(f"height = {y2 - y1}")
    prompt = pytesseract.image_to_string(img)
    print("prompt is " + prompt)

    for word in words:
        if prompt in word:
            if word_num > 0:
                word_num -= 1
                continue
            #pag.leftClick(x=1240, y=1900) # open 18th app
            pag.leftClick(x=400, y=900)
            pag.typewrite(word + "\n")
            current_prompt = prompt
            return
        

def load_words(filename):
    global words
    list = open(filename, "r")

    while True:
        word = list.readline()
        if not word:
            break
        words.append(word)
    
    list.close()


def setup1():
    global x1, y1
    x1, y1 = pag.position()
    print(f"x1 = {x1}")
    print(f"y1 = {y1}")


def setup2():
    global x2, y2
    x2, y2 = pag.position()
    print(f"x2 = {x2}")
    print(f"y2 = {y2}")


def up():
    global word_num
    word_num += 1


def reset():
    global word_num
    word_num = 0


def clear():
    global word_num
    word_num = 0


if __name__ == "__main__":
    main()