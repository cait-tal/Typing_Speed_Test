from tkinter import *
from random import choice

# ------------------------------------------FONTS and SAMPLE TEXTS-----------------------------------------#
FONT_START = ("Arial", 60, "bold")
FONT_TEXT = ("Arial", 30, "bold")

TEXT_1 = [
    "Sunset is the time of day when our sky meets the outer space solar winds. There are blue, pink, and purple swirls, spinning and twisting, like clouds of balloons caught in a whirlwind.",
    "The sun moves slowly to hide behind the line of horizon, while the moon races to take its place in prominence atop the night sky. People slow to a crawl, entranced, fully forgetting the deeds that must still be done.",
    "There is a coolness, a calmness, when the sun does set."]
TEXT_2 = [
    "Here is the perfect system for cleaning your room. First, move all of the items that do not have a proper place to the center of the room. Get rid of at least five things that you have not used within the last year.",
    "Take out all of the trash, and place all of the dirty dishes in the kitchen sink. Now find a location for each of the items you had placed in the center of the room. For any remaining items, see if you can squeeze them",
    "in under your bed or stuff them into the back of your closet. See, that was easy!"]
TEXT_3 = [
    "The Blue Whales just played their first baseball game of the new season; I believe there is much to be excited about. Although they lost, it was against an excellent team that had won the championship last year. The Blue Whales fell behind early but",
    "showed excellent teamwork and came back to tie the game. The team had 15 hits and scored 8 runs. That’s excellent! Unfortunately, they had 5 fielding errors, which kept the other team in the lead the entire game. The game ended with the umpire making a bad call,",
    "and if the call had gone the other way, the Blue Whales might have actually won the game. It wasn’t a victory, but I say the Blue Whales look like they have a shot at the championship, especially if they continue to improve."]
TEXT_4 = [
    "People often install a kitty door, only to discover that they have a problem. The problem is their cat will not use the kitty door. There are several common reasons why cats won’t use kitty doors.",
    "First, they may not understand how a kitty door works. They may not understand that it is a little doorway just for them. Second, many kitty doors are dark, and cats cannot see to the other side. As such, they can’t be sure of what is on the other side of the door, so they won’t take the risk.",
    "One last reason cats won’t use kitty doors is because some cats don’t like the feeling of pushing through the door and having the door drag across their back. But don’t worry—there is a solution for this kitty-door problem."]

TEXT_LIST = [TEXT_1, TEXT_2, TEXT_3, TEXT_4]
CHOSEN_TEXT = None
CURRENT_INDEX = 0


# --------------------------------------------Typing Test Functions----------------------------------------#
def start_test():
    global CHOSEN_TEXT
    global CURRENT_INDEX
    button.config(state="disabled")
    CHOSEN_TEXT = choice(TEXT_LIST)
    CURRENT_INDEX = 0
    canvas.itemconfig(button_window, state="hidden")
    canvas.itemconfig(text, font=FONT_TEXT, text=CHOSEN_TEXT[CURRENT_INDEX])
    typing_box.config(state="normal")
    typing_box.delete("1.0", END)
    canvas.itemconfig(frame_window, state="normal")
    canvas.itemconfig(timer_text, state="normal")


def start_timer(event):
    current_text = typing_box.get("1.0", END)
    if current_text[0] != "\n":
        pass
    else:
        count_down(60)


def show_score():
    user_input = typing_box.get("1.0", END)
    typing_box.config(state="disabled")
    canvas.itemconfig(frame_window, state="hidden")
    wpm = user_input.split()
    cpm = len(user_input)
    correct_wpm = 0
    mistakes = 0
    word_list = " ".join(CHOSEN_TEXT).split()
    if "\n" in word_list:
        word_list.remove("\n")
    index = 0
    for word in wpm:
        if word == word_list[index]:
            correct_wpm += 1
        else:
            mistakes += 1
        index += 1
    result_text = f"Results\n" \
                  f"Character Per Minute: {cpm}\n" \
                  f"Words Per Minute: {len(wpm)}\n" \
                  f"Mistakes: {mistakes}\n" \
                  f"\nYour final score: {len(wpm) - mistakes} words per minute!!\n" \
                  f"\n(Most people average 40 wpm."

    canvas.itemconfig(text, text=result_text)
    canvas.itemconfig(button_window, state="normal")
    button.config(state="normal")


# ----------------------------------------Timer Function-------------------------------#
def count_down(count):
    global CHOSEN_TEXT
    global CURRENT_INDEX
    if count > -1:
        canvas.itemconfig(timer_text, text=f"{count}")
        if CURRENT_INDEX == 0:
            if len(typing_box.get("1.0", END)) >= len(CHOSEN_TEXT[0]):
                CURRENT_INDEX += 1
                canvas.itemconfig(text, text=CHOSEN_TEXT[CURRENT_INDEX])
        if CURRENT_INDEX == 1:
            if len(typing_box.get("1.0", END)) >= (len(CHOSEN_TEXT[0]) + len(CHOSEN_TEXT[1])):
                CURRENT_INDEX += 1
                canvas.itemconfig(text, text=CHOSEN_TEXT[CURRENT_INDEX])
        window.after(1000, count_down, count - 1)
    else:
        show_score()


# ------------------------------UI Setup------------------------------------------#
# Create Window
window = Tk()
window.geometry("800x800-260+20")
window.title("Typing Speed")
# Images
bg_img = PhotoImage(file="Images/bg_img.png", height=800, width=800)
button_img = PhotoImage(file="Images/button_img.png")
results_img = PhotoImage(file="Images/results_img.png", height=800, width=800)
# Create Canvas and Background
canvas = Canvas(window, width=800, height=800)
canvas.pack()
background = canvas.create_image(400, 400, image=results_img)
# Text and button items
text = canvas.create_text(400, 300, text="\n    Typing Speed Test", font=FONT_START, width=600, fill="black")
timer_text = canvas.create_text(400, 35, text="60", fill="white", font=FONT_TEXT, state="hidden")
# Windows
button = Button(window, image=button_img, highlightthickness=0, command=start_test, bg="#23a64e")
frame = Frame(window)
# Typing Input Box
typing_box = Text(
    frame,
    height=13,
    width=26,
    wrap='word',
    font=FONT_TEXT,
    state="disabled"
)
typing_box.bind("<1>", start_timer)
typing_box.pack(side=LEFT, expand=True)
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

typing_box.config(yscrollcommand=sb.set)
sb.config(command=typing_box.yview)
# Canvas Windows
button_window = canvas.create_window(400, 680, window=button, height=94, width=181)
frame_window = canvas.create_window(400, 680, window=frame, height=94, width=600, state="hidden")
window.mainloop()
