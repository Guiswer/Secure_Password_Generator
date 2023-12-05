
# Secure Password Algorithm 
# Made by: Guiswer


from tkinter import *
import tkinter as tk
import random
import os


# Random number generator
def rand_number():
	x = random.randint(1, 10**999)
	y = random.randint(1, 10**584)
	z = random.randint(1, 10**4)

	mescle1 = x % y
	mescle2 = mescle1 % z

	number = hash(mescle2)

	return number


def label_color_change(created_label, screen2):
	# Change label's color

	created_label = Label(screen2, text= 'Password created', font= ('Terminal 15 bold'), bg= background_color, fg= green_color)
	created_label.place(x= 100, y= 410)


def close_frame(frame):
	frame.destroy()


def save_password(password_final):
	# Save passwords in "save" file

	save_directory = 'save'

	# If save_directory not exists then create it
	if not os.path.exists(save_directory):
		os.makedirs(save_directory)

	file_path = os.path.join(save_directory, 'your_passwords.txt')
	file_save = open(file_path, "a")
	file_save.write(password_final + "\n")
	file_save.close()


def make_password(entry_text, result_text, screen2, created_label):
	# Make the password		

	special_chrs = ['!', '@', '#', '$', '^', '&', '*', '_']

	text_insert = entry_text.get('1.0', 'end-1c') # Getting the phrase that user entered
	phrase_no_spaces = text_insert.strip()

	if phrase_no_spaces == "": # If it not have content - break the function
		return None

	phraselist = list(phrase_no_spaces)

	x = 0
	y = 0 
	while y < len(phraselist): 
		sltc_chr = random.choice(special_chrs)
		numbergen = rand_number()

		adding = sltc_chr + str(numbergen) 

		if " " in phraselist:
			place = phraselist.index(" ", x)
			phraselist[place] = adding
			x = place

		else:
			phraselist.append(adding)
			break
		
		y += 1 
	
	password_final = "".join(phraselist)

	# View the generated password
	result_text = Text(screen2, width=60, height=5, font= ('Arial 15 bold'), bg= result_color, fg= white_color, bd= 0, highlightthickness= 0, highlightbackground= background_color)
	result_text.place(x= 100, y= 460)
	result_text.insert(tk.END, password_final)
	result_text.config(state='disabled')

	save_password(password_final)
	label_color_change(created_label, screen2)


def password_window(screen1, inital_window):
	# Second screen

	# Screen2 configs
	screen2 = Frame(screen1, width= 870, height=673, bg= background_color )
	screen2.place(x= 0, y=0)

	# Labels
	insert_label = Label(screen2, text= 'Insert a random phrase', font= ('Terminal 15 bold'), bg= background_color, fg= white_color)
	insert_label.place(x= 100, y= 100)

	created_label = Label(screen2, text= 'Password created', font= ('Terminal 15 bold'), bg= background_color, fg= gray_color)
	created_label.place(x= 100, y= 410)

	# Result password label
	result_text = Text(screen2, width=60, height=5, font= ('Arial 15 bold'), bg= result_color, fg= white_color, bd= 0, highlightthickness= 0, highlightbackground= background_color)
	result_text.place(x= 100, y= 460)
	result_text.config(state="disabled")

	# Gen
	gen_label = Label(screen2, text= 'Generate as much as you want 😊', bg= background_color, fg= white_color)
	gen_label.place(x= 200, y= 245)

	# Button MAKE
	button_make = Button(screen2, width= 6, height= 1, text= 'MAKE', command= lambda: make_password(entry_text,result_text, screen2, created_label), font= ('Terminal 15 bold'), bg= lilas_button_make , fg= purple_button_make, bd= 0, highlightthickness= 0, highlightbackground= background_color)
	button_make.config(activebackground= button_make.cget('background'))
	button_make.place(x= 100, y= 240)
  	
	# Button to back
	button_back = Button(screen2, width= 5, height= 2, text= 'back', command= lambda: close_frame(screen2), font= ('Terminal 10 bold'), bg= gray_button_gray, fg= white_color, bd= 0, highlightthickness= 0, highlightbackground= background_color)
	button_back.place(x= 3, y= 3)


	# Entry
	entry_text = Text(screen2, width= 60, height= 3, font=('Aria 15 bold'), bg= entry_color, bd=0, fg='#ffffff', highlightthickness=0)
	entry_text.place(x=100, y=150)


def inital_window():
	# Screen definitions
	screen1 = Tk()
	screen1.geometry('870x673')
	screen1.config(bg = background_color)
	screen1.title('Secure Password Generator')
	screen1.resizable(width = False, height = False)

	# Labels
	top_label = Label(screen1, text= "Generate Secure Passwords", bg= background_color, fg= lilas_color, font= ('Arial 20 bold'))
	top_label.place(x=250, y=60)

	advice_label = Label(screen1, text= 'ADVICES', bg= background_color, fg= lilas_advices, font= ('Arial 13 bold'))
	advice_label.place(x=50, y=150)

	first_label = Label(screen1, text= '• Min 12 characters', bg= background_color, fg= white_color, font= ('Arial 13 bold'))
	first_label.place(x=50, y=200)

	second_label = Label(screen1, text= '• Complexity: numbers, special characters, lower and upper letters', bg= background_color, fg= white_color, font= ('Arial 13 bold'))
	second_label.place(x=50, y=250)

	third_label = Label(screen1, text= '• No personal informations', bg= background_color, fg= white_color, font= ('Arial 13 bold'))
	third_label.place(x=50, y=300)

	fourth_label = Label(screen1, text= '• Consider creating a phrase-based password', bg= background_color, fg= white_color, font= ('Arial 13 bold'))
	fourth_label.place(x=50, y=350)

	fifth_label = Label(screen1, text= "• Don't use the same password for all your accounts", bg= background_color, fg= white_color, font= ('Arial 13 bold'))
	fifth_label.place(x=50, y=400)

	byguiswer = Label(screen1, text= 'made by: Guiswer', bg= background_color, fg= lilas_advices, font= ('Arial 10 bold'))
	byguiswer.place(x=3, y=650)


	# Buttons
	button_start = Button(screen1, command=lambda: password_window(screen1, inital_window), width= 10, height= 2, text= 'START', font= ('Arial 20 bold'), bg= purple_dark_color, fg= light_lilas_color, bd= 0, highlightthickness= 6, highlightbackground= background_color)
	button_start.config(activebackground= button_start.cget('background'))
	button_start.place(x=330, y=500)

	screen1.mainloop()


# Colors
background_color = '#03000A'
entry_color = '#574390'
gray_button_gray = '#171321'
gray_color = '#3C3252'
green_color = '#54FA83'
light_lilas_color = '#C9AFFF'
lilas_advices = '#C6C0E8'
lilas_button_make = '#BFAFFF'
lilas_color = '#A596FF'
purple_button_make = '#3C2354'
purple_dark_color = '#251A64'
result_color = '#2D2466'
white_color = '#FFFFFF'


inital_window()