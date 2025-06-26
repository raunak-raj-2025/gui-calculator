import tkinter as tk
import math
import re

class Calculator(tk.Tk):
    
    def equal(self):
        try:
            expression = self.operationvar.get().replace("×", "*").replace("÷", "/").replace("%", "/100").replace("√", "math.sqrt(").replace("^", "**").replace("π", "math.pi")
            open_sqrt_count = expression.count("math.sqrt(")
            close_paren_count = expression.count(")")
            expression += ")"*(open_sqrt_count - close_paren_count)
            result = eval(expression, {"__builtins__": None, "math": math})
            self.historyvar.set(self.operationvar.get()+"\n"+str(result))
            self.operationvar.set(str(result))
        except Exception as e:
            self.operationvar.set("Error")

    def one(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("1")
        else:
            self.operationvar.set(current+"1")
  
    def two(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("2")
        else:
            self.operationvar.set(current+"2")
    
    def three(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("3")
        else:
            self.operationvar.set(current+"3")
    
    def four(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("4")
        else:
            self.operationvar.set(current+"4")
    
    def five(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("5")
        else:
            self.operationvar.set(current+"5")
    
    def six(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("6")
        else:
            self.operationvar.set(current+"6")
    
    def seven(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("7")
        else:
            self.operationvar.set(current+"7")
    
    def eight(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("8")
        else:
            self.operationvar.set(current+"8")
    
    def nine(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("9")
        else:
            self.operationvar.set(current+"9")
    
    def zero(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("0")
        else:
            self.operationvar.set(current+"0")
    
    def dot(self):
        current = self.operationvar.get()
        parts = re.split(r'[\+\-\*/\^%√×÷]', current)
        last_number = parts[-1] if parts else ""
        if '.' not in last_number:
            self.operationvar.set(current + ".")
    
    def multiply(self):
        current = self.operationvar.get()
        if current.endswith("×"):
            pass
        elif current == "0":
            pass
        else:
            self.operationvar.set(current+"×")
    
    def divide(self):
        current = self.operationvar.get()
        if current.endswith("÷"):
            pass
        elif current == "0":
            pass
        else:
            self.operationvar.set(current+"÷")
    
    def add(self):
        current = self.operationvar.get()
        if current.endswith("+"):
            pass
        elif current == "0":
            pass
        else:
            self.operationvar.set(current+"+")
    
    def substract(self):
        current = self.operationvar.get()
        if current.endswith("-"):
            pass
        elif current == "0":
            self.operationvar.set("-")
        else:
            self.operationvar.set(current+"-")
    
    def percent(self):
        current = self.operationvar.get()
        if current.endswith("%"):
            pass
        elif current == "0":
            pass
        else:
            self.operationvar.set(current+"%")
    
    def sq_root(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("√")
        else:
           self.operationvar.set(current + "√")
            
    def cut(self):
        current = self.operationvar.get()
        if len(current) > 1:
            self.operationvar.set(current[:-1])
        else:
            self.operationvar.set("0")
            
    def ac(self):
        self.historyvar.set("No History")
        self.operationvar.set("0")
        
    def c(self):
        self.operationvar.set("0")
        
    def power(self):
        current = self.operationvar.get()
        if current.endswith("^"):
            pass
        elif current == "0":
            self.operationvar.set("^")
        else:
            self.operationvar.set(current+"^")
            
    def open(self):
        current = self.operationvar.get()
        if current.endswith("("):
            pass
        elif current == "0":
            self.operationvar.set("(")
        else:
            self.operationvar.set(current+"(")
            
    def close(self):
        current = self.operationvar.get()
        if current.endswith(")"):
            pass
        elif current == "0":
            self.operationvar.set(")")
        else:
            self.operationvar.set(current+")")
            
    def pie(self):
        current = self.operationvar.get()
        if current == "0":
            self.operationvar.set("π")
        else:
            self.operationvar.set(current+"π")

    def __init__(self):
        super().__init__()
        self.geometry("720x1540")
        self.title("My Calculator")
        self.configure(bg="grey")
        self.operationvar = tk.StringVar(value="0")
        self.historyvar = tk.StringVar(value="No History")

    def create_labels(self):
        self.heading_label = tk.Label(self, text="Calculator", bg="grey", font="comicsansms 30")
        self.heading_label.grid(padx=115, row=0, column=0, columnspan=5)

        self.history_labels = tk.Label(self, textvariable=self.historyvar, bg="grey", pady=250, font="comicsansms 10")
        self.history_labels.grid(sticky="e", row=1, column=0, columnspan=5, padx=10)

        self.operation_label = tk.Label(self, textvariable=self.operationvar, pady=60, bg="grey", font="comicsansms 15", wraplength=700, justify="right")
        self.operation_label.grid(sticky="e", row=3, column=0, columnspan=5, padx=10)

    def create_buttons(self):
        tk.Button(self, text="AC", fg="dark blue", font="comicsansms 15", padx=10, command=self.ac).grid(row=4, column=1)
        
        tk.Button(self, text="CUT", fg="dark blue", font="comicsansms 15", padx=1, command=self.cut).grid(row=4, column=2)
        
        tk.Button(self, text="%", fg="dark blue", font="comicsansms 15", padx=27, command=self.percent).grid(row=4, column=3)
        
        tk.Button(self, text="÷", fg="dark blue", font="comicsansms 15", command=self.divide).grid(row=4, column=4, pady=20)

        tk.Button(self, text="7", fg="dark blue", font="comicsansms 15", command=self.seven).grid(row=5, column=1)
        
        tk.Button(self, text="8", fg="dark blue", font="comicsansms 15", command=self.eight).grid(row=5, column=2)
        
        tk.Button(self, text="9", fg="dark blue", font="comicsansms 15", command=self.nine).grid(row=5, column=3)
        
        tk.Button(self, text="×", fg="dark blue", font="comicsansms 15", command=self.multiply).grid(row=5, column=4, pady=20)

        tk.Button(self, text="4", fg="dark blue", font="comicsansms 15", command=self.four).grid(row=6, column=1, pady=20)
        
        tk.Button(self, text="5", fg="dark blue", font="comicsansms 15", command=self.five).grid(row=6, column=2)
        
        tk.Button(self, text="6", fg="dark blue", font="comicsansms 15", command=self.six).grid(row=6, column=3)
        
        tk.Button(self, text="-", fg="dark blue", font="comicsansms 15", padx=39, command=self.substract).grid(row=6, column=4)

        tk.Button(self, text="1", fg="dark blue", font="comicsansms 15", command=self.one).grid(row=7, column=1)
        
        tk.Button(self, text="2", fg="dark blue", font="comicsansms 15", command=self.two).grid(row=7, column=2, pady=20)
        
        tk.Button(self, text="3", fg="dark blue", font="comicsansms 15", command=self.three).grid(row=7, column=3)
        
        tk.Button(self, text="+", fg="dark blue", font="comicsansms 15", command=self.add).grid(row=7, column=4)

        tk.Button(self, text="C", fg="dark blue", font="comicsansms 15", command=self.c, padx=29, pady=12).grid(row=8, column=1, pady=20)
        
        tk.Button(self, text="0", fg="dark blue", font="comicsansms 15", command=self.zero).grid(row=8, column=2)
        
        tk.Button(self, text=".", fg="dark blue", font="comicsansms 15", padx=38, command=self.dot).grid(row=8, column=3)
        
        tk.Button(self, text="=", fg="dark blue", font="comicsansms 15", command=self.equal).grid(row=8, column=4)
        
        tk.Button(self, text="√", fg="dark blue", font="comicsansms 15", command=self.sq_root, padx=27).grid(row=4, column=0)
        
        tk.Button(self, text="^", fg="dark blue", font="comicsansms 15", command=self.power).grid(row=5, column=0)
        
        tk.Button(self, text="(", fg="dark blue", font="comicsansms 15", command=self.open, padx=33).grid(row=6, column=0)
        
        tk.Button(self, text=")", fg="dark blue", font="comicsansms 15", command=self.close, padx=33).grid(row=7, column=0)
        
        tk.Button(self, text="π", fg="dark blue", font="comicsansms 15", command=self.pie, padx=27).grid(row=8, column=0)

if __name__ == "__main__":
    window = Calculator()
    window.create_labels()
    window.create_buttons()
    window.mainloop()