import tkinter as tk
from chempy import Substance



class ChemistryCalculator:

  def __init__(self, master):
    self.master = master
    master.title("Chemistry Calculator")

    self.label_1 = tk.Label(master, text="Formula:")
    self.label_1.grid(row=0, column=0)

    self.entry_1 = tk.Entry(master)
    self.entry_1.grid(row=0, column=1)

    self.label_2 = tk.Label(master, text="Grams:")
    self.label_2.grid(row=1, column=0)

    self.entry_2 = tk.Entry(master)
    self.entry_2.grid(row=1, column=1)

    self.result_label = tk.Label(master, text="")
    self.result_label.grid(row=2, column=0, columnspan=1)

    self.convert_button = tk.Button(master,
                                    text="Convert",
                                    command=self.convert)
    self.convert_button.grid(row=3, column=0, columnspan=1)

  def convert(self):
    formula = self.entry_1.get()
    grams = float(self.entry_2.get())

    substance = Substance.from_formula(formula)
    molar_mass = substance.mass
    moles = grams / molar_mass

    result = f"{grams} grams of {formula} is equal to {moles:.2f} moles"
    self.result_label.config(text=result)


root = tk.Tk()
my_gui = ChemistryCalculator(root)

root.mainloop()
