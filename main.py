from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
    checkmark_label.config(fg=GREEN, bg=YELLOW, font=("Arial", 20, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rep
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if rep == 0:
        rep = rep + 1
    if rep % 8 == 0:
        count_down(long_break)
        title_label.config(text="LONG-BREAK", fg=RED, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
        rep += 1
    elif rep % 2 == 1:
        count_down(work_min)
        title_label.config(text="WORK", fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
        rep += 1
    elif rep % 2 == 0:
        count_down(short_break)
        title_label.config(text="SHORT-BREAK", fg=PINK, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
        rep += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        works_session = math.floor(rep)
        for _ in range(works_session):
            marks += "✔"
            checkmark_label.config(text="✔")
            checkmark_label.grid(row=3, column=1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato (1).png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=("Arial", 20, "bold"))
title_label.grid(row=0, column=1)
checkmark_label.grid(row=3, column=1)

start_button = Button(text="start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()