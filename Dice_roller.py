from tkinter import *
import random, time

root = Tk()
root.geometry("1370x768")
root.title('Dice Roller')

dice_images = [
    PhotoImage(file='1 dice.png'),
    PhotoImage(file='2 dice.png'),
    PhotoImage(file='3 dice.png'),
    PhotoImage(file='4 dice.png'),
    PhotoImage(file='5 dice.png'),
    PhotoImage(file='6 dice.png')
]
dice_labels = []
def roll_dice():
    num_dice = int(number_of_dice.get())
    result = []

    for _ in range(num_dice):
        result.append(random.randint(1, 6))

    # Clear previous result
    result_label.config(text='')

    # Remove existing dice labels
    for label in dice_labels:
        label.destroy()
    dice_labels.clear()

    # Animate the dice 
    for _ in range(10):
        dice_result = [random.randint(1, 6) for _ in range(num_dice)]
        dice_images_result = [dice_images[num-1] for num in dice_result]
        for i in range(num_dice):
            dice_label = Label(dice_frame, image=dice_images_result[i])
            dice_label.grid(row=i // 12, column=i % 12, padx=5)
            dice_labels.append(dice_label)
        root.update()
        time.sleep(0.1)
        # Removing dice labels after each animation frame
        for label in dice_labels:
            label.destroy()
        dice_labels.clear()

    # Displaying the final result
    dice_images_result = [dice_images[num-1] for num in result]
    for i in range(num_dice):
        dice_label = Label(dice_frame, image=dice_images_result[i])
        dice_label.grid(row=i // 12, column=i % 12, padx=5)
        dice_labels.append(dice_label)
    result_label.config(text=','.join(map(str, result)))



title_label = Label(root, text='Dice Roller', font=('Arial', 16, 'bold'))
title_label.pack(pady=10)

text_frame = Frame(root)
text_frame.pack(pady=5)

dice_frame=Frame(root)
dice_frame.pack()

number_label = Label(text_frame, text='Number of Dice:')
number_label.grid(row=0, column=0, padx=5)

number_of_dice = Spinbox(text_frame, from_=1, to=60)
number_of_dice.grid(row=0, column=1, padx=5, pady=5)

roll_button = Button(root, text='Roll Dice', command=roll_dice)
roll_button.pack(pady=10)

dice_label = Label(root)
dice_label.pack()

result_label = Label(root, text='', font=('Arial', 14))
result_label.pack()

quit_button = Button(root, text='Quit', command=root.destroy)
quit_button.pack()

root.mainloop()
