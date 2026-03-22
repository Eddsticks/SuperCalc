class CalcLogic:
    def __init__(self):
        self.expression = ""
        self.result_shown = False

    def process_input(self, key, current_on_screen):
        self.expression = current_on_screen

        operators = "+-*/."

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
            result = str(eval(self.expression))
            self.expression = result
            self.result_shown = True
            return result
        except:
            self.expression = ""
            self.result_shown = False
            return "Error"