import ast
import operator

from backend.tools.base_tool import BaseTool


class CalculatorTool(BaseTool):


    @property
    def name(self):

        return "calculator"


    @property
    def description(self):

        return "Used for mathematical calculations"


    def run(self, input_data: str):

        try:

            expression = input_data.strip()

            result = self.safe_eval(expression)

            return str(result)


        except Exception:

            return "Invalid expression"



    def safe_eval(self, expression):

        allowed_operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod
        }


        def evaluate(node):

            if isinstance(node, ast.Constant):

                return node.value


            elif isinstance(node, ast.BinOp):

                left = evaluate(node.left)
                right = evaluate(node.right)

                operator_function = allowed_operators[
                    type(node.op)
                ]

                return operator_function(
                    left,
                    right
                )


            else:

                raise ValueError(
                    "Unsupported expression"
                )


        tree = ast.parse(
            expression,
            mode="eval"
        )


        return evaluate(tree.body)