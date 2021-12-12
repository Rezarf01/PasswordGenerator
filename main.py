import string, random
from gui import Window
from tkinter import *

class Password:

    def __init__(self, password_info, include_symbols):


        try:
            self.length, self.security_level = tuple(map(int, ' '.join(password_info).split(' ')))
        except ValueError:
            if not password_info[0] and not password_info[1]:
                self.password = 'Please fill in both fields'
            elif not password_info[0]:
                self.password = 'Please provide a length'
            elif not password_info[1]:
                self.password = 'Please provide a security level'
        else:

            if self.length > 10 or self.length < 1:
                self.password = 'Length must be within 1 - 10'
            elif self.security_level > 10 or self.security_level < 1:
                self.password = 'Security level must be within 1 - 10'
            else:

                self.security_multiplyer = (self.security_level - 1) / 10

                chars = string.printable[:len(string.printable)-6]
                 
                if include_symbols:
                    chars_list = list(chars)
                elif not include_symbols:
                    chars_list = list(chars)[:len(chars)-32]

                 

                bool_list = []

                for x in range(len(chars_list)):
                    tf_list = [True, False]
                    bool_list.append(random.choices(tf_list, weights=[self.security_multiplyer, 1-self.security_multiplyer ], k=1))

                 

                weight_list = []


                for i in bool_list:

                    if i[0] == True:
                        weight_list.append(round(random.uniform(0 + random.uniform(0, 1-self.security_multiplyer), 1-self.security_multiplyer), 3))

                    elif i[0] == False:
                        bin = [0, 1]
                        if random.choices(bin, weights=[10, self.security_level], k=1)[0] == 1:
                            weight_list.append(round(random.uniform(0 + random.uniform(0, 1-self.security_multiplyer), 1-self.security_multiplyer), 3))
                        else:
                            weight_list.append(0)


                self.password = random.choices(chars_list, weights=weight_list, k=self.length)
                self.password = ''.join(self.password)

         

    def get(self):
        try:
            return self.password
        except AttributeError:
            return 'One of the fields is not an integer or contains spaces'


 

def main():
    root = Tk()
    window = Window(root, Password)
    root.mainloop()
    
main()
