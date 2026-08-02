import re


class CalculatorTool:

    name = "calculator"

    description = "Performs mathematical calculations"


    def run(self, expression: str):

        try:
            expression = expression.lower()

            # Convert words into operators
            expression = expression.replace("divided by", "/")
            expression = expression.replace("divide", "/")
            expression = expression.replace("multiplied by", "*")
            expression = expression.replace("multiply", "*")
            expression = expression.replace("times", "*")
            expression = expression.replace("plus", "+")
            expression = expression.replace("minus", "-")

            # Remove unnecessary words
            expression = expression.replace("calculate", "")
            expression = expression.replace("find", "")
            expression = expression.replace("what is", "")

            expression = expression.strip()


            # Keep only numbers and operators
            expression = re.sub(
                r"[^0-9+\-*/().]",
                "",
                expression
            )


            result = eval(expression)

            return str(result)


        except Exception:
            return "Unable to calculate expression"