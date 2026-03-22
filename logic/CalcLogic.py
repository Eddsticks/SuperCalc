class CalcLogic:
    def __init__(self):
        self.expression = ""
        self.result_shown = False

    def process_input(self, key, current_on_screen):
        self.expression = current_on_screen

        operators = "+-*/."

        if current_on_screen == "Error":
            self.expression = ""

        if self.result_shown and key not in operators and key not in ['=', 'E', 'C']:
            self.expression = ""
            self.result_shown = False

        if self.result_shown and key in operators:
            self.result_shown = False

        if key == "=":
            return self.calculate()
        elif key == "C":
            self.expression = ""
            return ""
        elif key == "E":
            self.expression = self.expression[:-1]
            return self.expression
        else:
            if key in operators and self.expression and self.expression[-1] in operators:
                self.expression = self.expression[:-1]

            self.expression += key
            return self.expression

    def calculate(self):
        try:
            result = eval(self.expression)
            form_result = f"{result:.2f}"

            if result == int(result):
                form_result = f"{int(result):,}"

            self.expression = str(result)
            self.result_shown = True

            return form_result

        except Exception as e:
            print(f"Error de calculo {e}")
            self.expression = ""
            self.result_shown = False
            return "Error"