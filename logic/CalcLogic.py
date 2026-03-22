class CalcLogic:
    def __init__(self):
        pass

    def calculate(self, expression):
        try:
            return str(eval(expression))
        except:
            return "Error"

    def backspace(self, current_text):
        return current_text[:-1] if current_text else ""