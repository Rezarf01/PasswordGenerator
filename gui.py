from tkinter import *
from tkinter import ttk
import subprocess

class Window(Frame):
	def __init__(self, root, Password):	

		self.Password = Password	

		root.geometry('300x250')

		self.labelframe1 = LabelFrame(root, text='Password Info')
		self.labelframe1.pack(fill='both', expand=False)

		self.length = Label(self.labelframe1, text='Length (1 - 10)').grid(row=0, column=0, pady=10, padx=10)
		self.length_input = ttk.Entry(self.labelframe1)
		self.length_input.grid(row=0, column=1)

		self.security_level = Label(self.labelframe1, text='Security Level (1 - 10)').grid(row=1, column=0, padx=10)
		self.sl_input = ttk.Entry(self.labelframe1)
		self.sl_input.grid(row=1, column=1)

		self.symbols_state = IntVar()
		self.include_symbols = ttk.Checkbutton(self.labelframe1, text='Include Symbols', variable=self.symbols_state, onvalue=1, offvalue=0)
		self.include_symbols.grid(row=2, column=0, pady=10)
		self.Checkbutton_desc = Label(self.labelframe1, text='Such as "+" or "#"', fg='Gray', relief=RAISED)
		self.Checkbutton_desc.place(x=140, y=72)

		button1_style = ttk.Style()
		button1_style.configure('B1.TButton', foreground='blue')

		self.generate_password = ttk.Button(root, text='Generate Password', command=self.get_output, style='B1.TButton')
		self.generate_password.pack()

		self.password = StringVar()
		self.password_label = Label(root, text=self.password.get(), textvariable=self.password)
		self.password_label.pack()

		button2_style = ttk.Style()
		button2_style.configure('B2.TButton', foreground='red')

		self.copytoclip = Button(root, text='Copy to clipboard', fg='red', font='Verdana 8 underline', activeforeground='blue', command=self.copy2clip)
		self.copytoclip.pack()

		self.on_copied = StringVar()
		self.copytoclip_label = Label(root, text=self.on_copied.get(), fg='gray', textvariable=self.on_copied)
		self.copytoclip_label.pack()

		self.password_active = False

	def get_output(self):

		self.on_copied.set('')

		self.password_main = self.Password(password_info=(self.length_input.get(), self.sl_input.get()),include_symbols=self.symbols_state.get())
				  

		if self.password_main.get() == 'Please fill in both fields':
			self.fill_both_fields()
			self.password_label.config(foreground='red', background='yellow')

		
		try:
			if self.password_main.get().split()[1] == 'provide':
				self.password_label.config(foreground='red', background='yellow')

				if self.password_main.get() == 'Please provide a length':

					self.length_input.config(foreground='red')
					self.length_input.insert(0, 'This field must be filled in')
				else:
					self.sl_input.config(foreground='red')
					self.sl_input.insert(0, 'This field must be filled in')
		except:
			pass

		if self.length_input.get() == 'This field must be filled in':
			self.length_input.bind('<1>', lambda event: self.length_input.delete(0, 'end'))
			 
		else:
			self.length_input.unbind('<1>')
			self.length_input.config(foreground='black')

		if self.sl_input.get() == 'This field must be filled in':
			self.sl_input.bind('<1>', lambda event: self.sl_input.delete(0, 'end'))
		else:
			self.sl_input.unbind('<1>')
			self.sl_input.config(foreground='black')


		try:
			int(self.length_input.get())
		except:
			self.password_label.config(foreground='red', background='yellow')
			self.password_active = False
			self.copytoclip.pack_forget()
			self.copytoclip_label.pack_forget()

		else:
			if len(self.password_main.get()) == int(self.length_input.get()):
				self.password_label.config(foreground='black', background='white')
				self.password_active = True
				self.copytoclip.pack()
				self.copytoclip_label.pack()
			else:
				self.password_label.config(foreground='red', background='yellow')
				self.password_active = False
				self.copytoclip.pack_forget()
				self.copytoclip_label.pack_forget()



		self.password.set(self.password_main.get())

	def fill_both_fields(self):
		for entry in (self.length_input, self.sl_input):
			entry.config(foreground='red')
			entry.insert(0, 'This field must be filled in')

	def copy2clip(self):
		if self.password_active:
			cmd='echo '+self.password_main.get().strip()+'|clip'
			try:
				subprocess.check_call(cmd, shell=True)
			except:
				self.on_copied.set("Can't copy")
			else:

				self.on_copied.set('Copied!')





 