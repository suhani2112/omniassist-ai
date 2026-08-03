from backend.tools.base_tool import BaseTool
import ast
import operator


class CalculatorTool(BaseTool):

    def __init__(self):

        super().__init__()

        self.name = "calculator"

        self.description = "Performs mathematical calculations."

        self.category = "utility"

        self.supported_inputs = [
            "25+10",
            "100/4",
            "50*20",
            "(5+3)*2"
        ]
        self.capabilities = [

        "mathematical calculation",

        "arithmetic",

        "evaluate expressions",

        "basic mathematics"
]

        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
            ast.USub: operator.neg
        }


    def run(self, input_data):

        try:

            result = self.evaluate(input_data)

            return {
                "success": True,
                "result": str(result)
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


    def evaluate(self, expression):

        node = ast.parse(expression, mode="eval").body

        return self._eval(node)


    def _eval(self, node):

        if isinstance(node, ast.Constant):
            return node.value

        elif isinstance(node, ast.Num):
            return node.n

        elif isinstance(node, ast.BinOp):

            return self.operators[type(node.op)](
                self._eval(node.left),
                self._eval(node.right)
            )

        elif isinstance(node, ast.UnaryOp):

            return self.operators[type(node.op)](
                self._eval(node.operand)
            )

        else:
            raise TypeError("Unsupported expression")