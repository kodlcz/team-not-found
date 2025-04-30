"""
@file calculator.py
@brief GUI kalkulačka s běžnými a pokročilými matematickými funkcemi.

@details Tento modul implementuje grafickou kalkulačku pomocí Tkinteru.
Poskytuje základní aritmetické operace, stejně jako pokročilé funkce
jako faktoriály, exponenty, Fibonacciho posloupnost a absolutní hodnoty.
Kalkulačka podporuje zadávání jak myší, tak klávesnicí.

@author William Denis Tihelka
@date 30. dubna 2025
@version 1.0
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import calc_lib

class Calculator:
    """
    @class Calculator
    @brief Grafická kalkulačka s podporou základních a pokročilých matematických operací.

    @details Tato třída implementuje kalkulačku s grafickým uživatelským rozhraním pomocí Tkinteru.
    Poskytuje standardní aritmetické operace, pokročilé funkce jako faktoriál a Fibonacciho posloupnost
    a podporuje jak klikání na tlačítka, tak zadávání z klávesnice.
    """

    def __init__(self, root):
        """
        @brief Inicializace grafického rozhraní kalkulačky.

        @details Nastaví hlavní okno, zobrazovací oblasti, tlačítka a vazby na klávesnici.

        @param root Hlavní okno Tkinteru.
        """

        self.root = root
        self.root.title("Kalkulačka")
        self.root.geometry("360x540")  # Increased height to accommodate additional row
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Create menu bar
        self.create_menu()
        
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=5)
        
        # Display variables
        self.current_expression = "" 
        self.total_expression = ""
        self.pending_operation = None
        self.first_number = None
        self.second_number = None
        self.result = None
        self.expecting_second_number = False
        self.just_evaluated = False
        
        # Create display frame
        self.display_frame = tk.Frame(self.root, height=100, bg="#f0f0f0")
        self.display_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Expression label (shows the current calculation)
        self.expression_label = tk.Label(
            self.display_frame, 
            text="", 
            font=("Arial", 14),
            anchor="e",
            bg="#f0f0f0",
            fg="#505050"
        )
        self.expression_label.pack(fill="both")
        
        # Result label (shows the result)
        self.result_label = tk.Label(
            self.display_frame, 
            text="0", 
            font=("Arial", 24, "bold"),
            anchor="e",
            bg="#f0f0f0"
        )
        self.result_label.pack(fill="both", expand=True)
        
        # Create buttons frame
        self.buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configure grid layout
        for i in range(7):  # Added an extra row for Fibonacci and Absolute
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
        
        # Button layout
        self.create_buttons()
        
        # Set up keyboard bindings
        self.setup_keyboard_bindings()
    
    def create_menu(self):
        # Create menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # Create Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Nápověda", menu=help_menu)
        help_menu.add_command(label="Jak používat kalkulačku", command=self.show_help)
        help_menu.add_command(label="O aplikaci", command=self.show_about)
    
    def show_help(self):
        help_text = """
Kalkulačka - Nápověda

Základní operace:
- Sčítání (+): Sečte dvě čísla
- Odčítání (-): Odečte druhé číslo od prvního
- Násobení (×): Vynásobí dvě čísla
- Dělení (÷): Vydělí první číslo druhým

Pokročilé funkce:
- Umocnění (x^y): Umocní první číslo na hodnotu druhého
- Druhá mocnina (x²): Umocní číslo na druhou
- N-tá odmocnina (n√x): Vypočítá n-tou odmocninu čísla (první zadejte číslo k odmocnění, pak klikněte na n√x, nakonec zadejte stupeň odmocniny)
- Faktoriál (n!): Vypočítá faktoriál celého čísla
- Fibonacciho číslo (Fib): Vypočítá číslo Fibonacciho posloupnosti
- Absolutní hodnota (|x|): Vypočítá absolutní hodnotu čísla
- Změna znaménka (±): Změní znaménko aktuálního čísla

Postup pro výpočet n-té odmocniny:
1. Zadejte číslo, které chcete odmocnit
2. Klikněte na tlačítko n√x
3. Zadejte stupeň odmocniny (např. 3 pro třetí odmocninu)
4. Stiskněte =

Klávesové zkratky:
- Čísla 0-9: Zadávání čísel
- + - * /: Základní operace
- ^: Umocnění
- !: Faktoriál
- a: Absolutní hodnota
- f: Fibonacciho číslo
- Enter: Vyhodnocení výrazu
- Backspace: Smazání posledního znaku
- Esc nebo C: Vymazání všeho
- .: Desetinná tečka
- F1: Zobrazení nápovědy
"""
        messagebox.showinfo("Nápověda", help_text)
    
    def show_about(self):
        about_text = """
Kalkulačka v1.0

Jednoduchá kalkulačka s pokročilými matematickými funkcemi.
Vytvořeno pomocí Pythonu a knihovny Tkinter.

© 2025
"""
        messagebox.showinfo("O aplikaci", about_text)
        
    def setup_keyboard_bindings(self):
        """
        @brief Nastavení klávesových zkratek pro operace kalkulačky.

        @details Mapuje klávesy na funkce kalkulačky:
        - Číselné klávesy (0–9) pro zadávání číslic
        - Operátory (+, -, *, /, ^) pro základní operace
        - Funkční klávesy (!, a, f) pro faktoriál, absolutní hodnotu a Fibonacciho posloupnost
        - Řídicí klávesy (Enter, Backspace, Escape) pro vyhodnocení, mazání a vymazání
        """

        # Number keys
        for i in range(10):
            self.root.bind(str(i), lambda event, digit=i: self.append_number(digit))
        
        # Operation keys
        self.root.bind("+", lambda event: self.prepare_operation("add"))
        self.root.bind("-", lambda event: self.prepare_operation("sub"))
        self.root.bind("*", lambda event: self.prepare_operation("mul"))
        self.root.bind("/", lambda event: self.prepare_operation("div"))
        self.root.bind("^", lambda event: self.prepare_operation("expon"))
        
        # Function keys
        self.root.bind("!", lambda event: self.calculate_factorial())
        self.root.bind("a", lambda event: self.calculate_absolute())
        self.root.bind("f", lambda event: self.calculate_fibonacci())
        
        # Control keys
        self.root.bind("<Return>", lambda event: self.evaluate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("c", lambda event: self.clear())
        self.root.bind("C", lambda event: self.clear())
        self.root.bind("<Escape>", lambda event: self.clear())
        self.root.bind(".", lambda event: self.append_number("."))
        
        # Help key
        self.root.bind("<F1>", lambda event: self.show_help())
        
    def create_buttons(self):
        """
        @brief Vytvoření a umístění všech tlačítek kalkulačky.

        @details Nastaví rozložení všech tlačítek kalkulačky, včetně čísel, operátorů
        a speciálních funkcí jako Fibonacciho posloupnost a absolutní hodnota.
        """

        # Clear and operations buttons (row 0)
        self.create_button("C", 0, 0, 1, 1, command=self.clear, bg="#ff9500")
        self.create_button("⌫", 0, 1, 1, 1, command=self.backspace, bg="#d9d9d9")
        self.create_button("±", 0, 2, 1, 1, command=self.negate, bg="#d9d9d9")
        self.create_button("÷", 0, 3, 1, 1, command=lambda: self.prepare_operation("div"), bg="#ff9500")
        
        # Advanced functions (row 1)
        self.create_button("x²", 1, 0, 1, 1, command=lambda: self.prepare_operation("expon2"), bg="#d9d9d9")
        self.create_button("n√x", 1, 1, 1, 1, command=lambda: self.prepare_operation("sqrt"), bg="#d9d9d9")
        self.create_button("x^y", 1, 2, 1, 1, command=lambda: self.prepare_operation("expon"), bg="#d9d9d9")
        self.create_button("×", 1, 3, 1, 1, command=lambda: self.prepare_operation("mul"), bg="#ff9500")
        
        # New row for Fibonacci and Absolute (row 2)
        self.create_button("Fib", 2, 0, 1, 1, command=self.calculate_fibonacci, bg="#d9d9d9")
        self.create_button("|x|", 2, 1, 1, 1, command=self.calculate_absolute, bg="#d9d9d9")
        self.create_button("n!", 2, 2, 1, 1, command=self.calculate_factorial, bg="#d9d9d9")
        self.create_button("-", 2, 3, 1, 1, command=lambda: self.prepare_operation("sub"), bg="#ff9500")
        
        # Numbers and operations (rows 3-6)
        buttons = [
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("+", 3, 3, lambda: self.prepare_operation("add"), "#ff9500"),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("=", 4, 3, self.evaluate, "#ff9500", 1, 3),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2),
            ("0", 6, 0, None, None, 2), (".", 6, 2)
        ]
        
        for button in buttons:
            if len(button) == 3:  # Regular number button
                self.create_button(button[0], button[1], button[2], command=lambda x=button[0]: self.append_number(x))
            elif len(button) == 4:  # Operation button with special command
                self.create_button(button[0], button[1], button[2], command=button[3])
            elif len(button) == 5:  # Operation button with special command and color
                self.create_button(button[0], button[1], button[2], command=button[3], bg=button[4])
            elif len(button) == 6:  # Button with custom width (like "0")
                self.create_button(button[0], button[1], button[2], command=lambda x=button[0]: self.append_number(x), columnspan=button[5])
            else:  # Button with custom width and height (like "=")
                self.create_button(button[0], button[1], button[2], command=button[3], bg=button[4], columnspan=button[5], rowspan=button[6])
    
    def create_button(self, text, row, column, columnspan=1, rowspan=1, command=None, bg="#e0e0e0"):
        """
        @brief Vytvoření jednotlivého tlačítka v kalkulačce.

        @param text Text, který se zobrazí na tlačítku.
        @param row Pozice řádku v mřížce.
        @param column Pozice sloupce v mřížce.
        @param columnspan Počet sloupců, které tlačítko zabírá (výchozí: 1).
        @param rowspan Počet řádků, které tlačítko zabírá (výchozí: 1).
        @param command Funkce, která se zavolá po kliknutí na tlačítko (výchozí: None).
        @param bg Barva pozadí tlačítka (výchozí: "#e0e0e0").

        @return Objekt vytvořeného tlačítka.
        """

        button = tk.Button(
            self.buttons_frame, 
            text=text, 
            font=("Arial", 16), 
            bg=bg,
            fg="black" if bg != "#ff9500" else "white",
            borderwidth=0,
            command=command,
            relief="flat",
            highlightthickness=0
        )
        button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=2, pady=2)
        return button
    
    def append_number(self, number):
        """
        @brief Přidání číslice nebo desetinné čárky do aktuálního výrazu.

        @details Zpracovává logiku pro různé stavy: zahájení nového výpočtu,
        zadávání prvního čísla nebo zadávání druhého čísla.

        @param number Číslice nebo desetinná čárka, která se má přidat.
        """

        if self.just_evaluated:
            self.current_expression = ""
            self.total_expression = ""
            self.pending_operation = None
            self.just_evaluated = False
        
        if self.expecting_second_number:
            self.current_expression = str(number)
            self.expecting_second_number = False
        else:
            self.current_expression += str(number)
        
        # If we're entering the second number, append to total expression
        if self.pending_operation and not self.expecting_second_number:
            # Only update the total expression if we've already entered a first number and operation
            self.total_expression = self.total_expression.rstrip() + str(number)
        
        self.update_display()
    
    def prepare_operation(self, operation):
        """
        @brief Nastavení binární operace mezi dvěma čísly.

        @details Uloží první číslo a typ operace, aktualizuje displej
        a připraví kalkulačku na zadání druhého čísla.

        @param operation Řetězec reprezentující operaci ("add", "sub" atd.).
        """

        if not self.current_expression and operation != "sub":
            return
        
        # If this is a new operation after completing another one, use the result
        if self.just_evaluated:
            self.first_number = float(self.current_expression)
            self.total_expression = self.current_expression
            self.just_evaluated = False
        else:
            try:
                self.first_number = float(self.current_expression)
                self.total_expression = self.current_expression
            except ValueError:
                return
        
        self.pending_operation = operation
        
        # Display the operation symbol
        op_symbols = {
            "add": "+", 
            "sub": "-", 
            "mul": "×", 
            "div": "÷",
            "expon": "^",
            "expon2": "²",
            "sqrt": "√"
        }
        
        if operation == "expon2":
            # For operations that don't require a second number
            self.evaluate()
        elif operation == "sqrt":
            # For square root, we need the root degree
            self.total_expression += f" {op_symbols.get(operation, '?')} "
            self.expecting_second_number = True
            self.update_display()
        else:
            # For operations that need two numbers
            self.total_expression += f" {op_symbols.get(operation, '?')} "
            self.expecting_second_number = True
            self.update_display()
    
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.pending_operation = None
        self.first_number = None
        self.second_number = None
        self.expecting_second_number = False
        self.just_evaluated = False
        self.update_display()
    
    def backspace(self):
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            self.update_display()
    
    def calculate_factorial(self):
        try:
            value = float(self.current_expression)
            if value.is_integer():
                result = calc_lib.factorial(int(value))
                if isinstance(result, str) and result.startswith("chyba"):
                    self.display_error(result)
                else:
                    self.current_expression = str(result)
                    self.total_expression = f"{int(value)}!"
                    self.just_evaluated = True
                    self.update_display(True)
            else:
                self.display_error("chyba_3")  # Not an integer
        except ValueError:
            self.display_error("chyba_1")
    
    def calculate_fibonacci(self):
        try:
            value = float(self.current_expression)
            if value.is_integer():
                result = calc_lib.fib(int(value))
                if isinstance(result, str) and result.startswith("chyba"):
                    self.display_error(result)
                else:
                    self.current_expression = str(result)
                    self.total_expression = f"Fib({int(value)})"
                    self.just_evaluated = True
                    self.update_display(True)
            else:
                self.display_error("chyba_3")  # Not an integer
        except ValueError:
            self.display_error("chyba_1")
    
    def calculate_absolute(self):
        try:
            value = float(self.current_expression)
            result = calc_lib.absolute(value)
            if isinstance(result, str) and result.startswith("chyba"):
                self.display_error(result)
            else:
                self.current_expression = str(result)
                self.total_expression = f"|{value}|"
                self.just_evaluated = True
                self.update_display(True)
        except ValueError:
            self.display_error("chyba_1")
    
    def evaluate(self):
        if not self.pending_operation and not self.just_evaluated:
            return
        
        try:
            if self.pending_operation == "expon2":
                # Handle single operand operation
                result = calc_lib.expon(self.first_number, 2)
                self.total_expression = f"{self.first_number}²"
            else:
                # Handle two operand operations
                if self.expecting_second_number:
                    # If we're still expecting a second number, use the first number
                    self.second_number = self.first_number
                else:
                    try:
                        self.second_number = float(self.current_expression)
                    except ValueError:
                        self.display_error("chyba_1")
                        return
                
                # Perform the operation using calc_lib functions
                if self.pending_operation == "add":
                    result = calc_lib.add(self.first_number, self.second_number)
                elif self.pending_operation == "sub":
                    result = calc_lib.sub(self.first_number, self.second_number)
                elif self.pending_operation == "mul":
                    result = calc_lib.mul(self.first_number, self.second_number)
                elif self.pending_operation == "div":
                    result = calc_lib.div(self.first_number, self.second_number)
                elif self.pending_operation == "expon":
                    result = calc_lib.expon(self.first_number, self.second_number)
                elif self.pending_operation == "sqrt":
                    # For nth root, fixed the order: first number is the value to root, second is the root degree
                    result = calc_lib.sqr(self.second_number, self.first_number)  # <-- FIXED ORDER HERE
                    self.total_expression = f"{self.first_number}√{self.second_number}"
                else:
                    result = self.first_number  # Fallback
            
            # Check if the result is an error message
            if isinstance(result, str) and result.startswith("chyba"):
                self.display_error(result)
                return
                
            # Format the result (convert to int if it's a whole number)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            self.current_expression = str(result)
            self.pending_operation = None
            self.just_evaluated = True
            self.update_display(True)
            
        except Exception as e:
            self.display_error("chyba_1")
    
    def display_error(self, error_code):
        error_messages = {
            "chyba_1": "Neplatný vstup",
            "chyba_2": "Dělení nulou",
            "chyba_3": "Faktoriál jen pro celá čísla",
            "chyba_4": "Záporné číslo nepřípustné",
            "chyba_5": "Odmocnina záporného čísla"
        }
        self.current_expression = error_messages.get(error_code, "Chyba")
        self.update_display()
    
    def negate(self):
        if self.current_expression and self.current_expression not in ["Chyba", "Neplatný vstup", "Dělení nulou"]:
            try:
                value = float(self.current_expression)
                # Use absolute function to handle negation
                if value < 0:
                    result = calc_lib.absolute(value)
                else:
                    result = -value
                
                if isinstance(result, float) and result.is_integer():
                    self.current_expression = str(int(result))
                else:
                    self.current_expression = str(result)
                self.update_display()
            except ValueError:
                pass
    
    def update_display(self, evaluated=False):
        """
        @brief Aktualizace displeje kalkulačky aktuálními hodnotami.

        @details Aktualizuje jak displej pro výraz (ukazuje výpočet), tak i displej pro výsledek (ukazuje aktuální číslo nebo výsledek).

        @param evaluated Boolean určující, zda byl výraz právě vyhodnocen (výchozí: False).
        """

        if evaluated:
            # When result is evaluated, show the full expression in the top label
            self.expression_label.config(text=self.total_expression)
        else:
            if self.expecting_second_number:
                # Keep showing the full expression when waiting for second number
                self.expression_label.config(text=self.total_expression)
            elif self.pending_operation:
                # If we have an operation but aren't expecting second number yet,
                # keep showing the first number and operation
                self.expression_label.config(text=self.total_expression)
            else:
                # When no operation is pending, just show current input
                self.expression_label.config(text=self.current_expression)
        
        # Update result label
        result_text = self.current_expression if self.current_expression else "0"
        if result_text in ["Chyba", "Neplatný vstup", "Dělení nulou", "Faktoriál jen pro celá čísla", 
                          "Záporné číslo nepřípustné", "Odmocnina záporného čísla"]:
            self.result_label.config(text=result_text, fg="red")
        else:
            self.result_label.config(text=result_text, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()