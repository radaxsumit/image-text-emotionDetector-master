from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from deepface import DeepFace
import text2emotion as te

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\PythonProjects\Face_emotion\build\assets\frame0")
filename = None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("862x519")
window.configure(bg="#3A7FF6")


canvas = Canvas(
    window,
    bg="#3A7FF6",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    430.99,
    0.0,
    861.99,
    519.0,
    fill="#FCFCFC",
    tag="rectangleSomething",
    outline="",
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: faceAnalyze(currentType, filename),
    relief="flat",
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mainMenu("text"),
    relief="flat",
)
button_4.place(x=470.99, y=303.0, width=150.0, height=55.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mainMenu("image"),
    relief="flat",
)
button_5.place(x=650.99, y=303.0, width=150.0, height=55.0)

canvas.create_text(
    58.99,
    46.0,
    anchor="nw",
    text="Image Emotion Detector",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1),
)

canvas.create_text(
    500.99,
    74.0,
    anchor="nw",
    text="Upload the image to detect",
    fill="#505485",
    font=("Roboto Bold", 24 * -1),
)

canvas.create_rectangle(
    58.99, 74.0, 365.99, 79.0, fill="#FCFCFC", outline=""
)

canvas.create_rectangle(
    473.99,
    203.0,
    818.99,
    265.0,
    tags="rectanglePath",
    fill="#F1F5FF",
    outline="",
)

canvas.create_text(
    128.99,
    154.0,
    anchor="nw",
    text="Add the Image",
    fill="#FCFCFC",
    font=("Tajawal Regular", 24 * -1),
)

canvas.create_text(
    128.99,
    302.0,
    anchor="nw",
    width=300,
    text="Get captions related to your mood",
    fill="#FCFCFC",
    font=("Tajawal Regular", 24 * -1),
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: upload_file(),
    relief="flat",
)

canvas.create_text(
    128.99,
    234.0,
    anchor="nw",
    text="Wait for 5 seconds",
    fill="#FFFFFF",
    font=("Tajawal Regular", 24 * -1),
)

canvas.create_rectangle(
    86.99999999999989, 313.0, 120.99999999999989, 344.0, fill="#000000", outline=""
)

canvas.create_rectangle(
    86.99999999999989, 229.0, 120.99999999999989, 260.0, fill="#000000", outline=""
)

canvas.create_rectangle(
    86.99999999999989, 152.0, 120.99999999999989, 183.0, fill="#000000", outline=""
)
window.resizable(False, False)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: resetButtons(),
    relief="flat",
)

entry_widget = Entry(window, background="#F1F5FF", width=50)


def upload_file():
    global filename
    f_types = [("Jpg Files", "*.jpg"), ("PNG Files", "*.png"), ("ALL Files", ".*")]
    filename = filedialog.askopenfilename(filetypes=f_types)
    # img = ImageTk.PhotoImage(file=filename)
    canvas.create_text(
        630.99,
        240.0,
        text=filename,
        width=290,
        fill="#848484",
        tag="filepath",
        font=("Tajawal Regular", 16 * -1),
    )


def faceAnalyze(type, path):
    canvas.delete("filepath")
    print(path)
    canvas.itemconfig(tagOrId="rectanglePath", state="hidden")
    button_2.place_forget()
    button_1.place_forget()
    canvas.itemconfig(tagOrId="textInput", state="hidden")
    if type == "image":
        face_analysis = DeepFace.analyze(img_path=path)
        print(face_analysis)
        canvas.create_text(
            580.0,
            234.0,
            anchor="nw",
            text="Mood: " + face_analysis[0]["dominant_emotion"],
            fill="#848484",
            tags="mood_details",
            font=("Tajawal Regular", 24 * -1),
        )
        button_3.place(x=556.99, y=303.0, width=180.0, height=55.0)

    if type == "text":
        text = entry_widget.get()
        emotion = te.get_emotion(text)
        dominant_emotion = max(emotion, key=emotion.get)
        print(dominant_emotion)
        canvas.create_text(
            565.0,
            234.0,
            anchor="nw",
            width=400,
            text="Mood: " + dominant_emotion,
            fill="#848484",
            tags="mood_details",
            font=("Tajawal Regular", 24 * -1),
        )
        button_3.place(x=556.99, y=303.0, width=180.0, height=55.0)


def resetButtons():
    button_4.place(x=470.99, y=303.0, width=150.0, height=55.0)
    button_5.place(x=650.99, y=303.0, width=150.0, height=55.0)
    button_3.place_forget()
    canvas.delete("mood_details")
    
    canvas.itemconfig(tagOrId="rectanglePath", state="normal")
    canvas.itemconfig(tagOrId="textInput", state="hidden")


def mainMenu(type):
    if type == "text":
        global currentType
        button_1.place(x=556.99, y=303.0, width=180.0, height=55.0)
        button_5.place_forget()
        button_4.place_forget()
        canvas.create_rectangle(
            473.99,
            203.0,
            818.99,
            265.0,
            tags="rectanglePath",
            fill="#F1F5FF",
            outline="",
        )
        canvas.create_window(650.0, 230.0, window=entry_widget, tags="textInput")
        currentType = "text"

    if type == "image":
        button_2.place(x=775.99, y=223.0, width=24.0, height=22.0)
        button_1.place(x=556.99, y=303.0, width=180.0, height=55.0)
        button_5.place_forget()
        button_4.place_forget()
        canvas.create_rectangle(
            473.99,
            203.0,
            818.99,
            265.0,
            tags="rectanglePath",
            fill="#F1F5FF",
            outline="",
        )
        currentType = "image"


window.mainloop()
