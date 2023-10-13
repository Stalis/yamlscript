from .models import BuiltinFunction
from .models import FunctionParameter
from .models import Package
from .models import ReturnValue


GLOBALS = {
    "std": Package(
        name="std",
        version="0.0.1",
        description="Standard library",
        author="",
        imports={},
        functions=[
            BuiltinFunction(
                name="echo",
                description="Prints a message",
                parameters=[
                    FunctionParameter(
                        name="message",
                        type="str",
                        description="Message to print",
                    )
                ],
                returns=[],
                func=lambda args: print(args["message"]),
            ),
            BuiltinFunction(
                name="add",
                description="Adds two numbers",
                parameters=[
                    FunctionParameter(
                        name="a",
                        type="int",
                        description="First number",
                    ),
                    FunctionParameter(
                        name="b",
                        type="int",
                        description="Second number",
                    ),
                ],
                returns=[
                    ReturnValue(
                        type="int",
                        description="Sum of the two numbers",
                    )
                ],
                func=lambda args: args["a"] + args["b"],
            ),
            BuiltinFunction(
                name="sub",
                description="Subtracts two numbers",
                parameters=[
                    FunctionParameter(
                        name="a",
                        type="int",
                        description="First number",
                    ),
                    FunctionParameter(
                        name="b",
                        type="int",
                        description="Second number",
                    ),
                ],
                returns=[
                    ReturnValue(
                        type="int",
                        description="Difference of the two numbers",
                    )
                ],
                func=lambda args: args["a"] - args["b"],
            ),
        ],
    )
}
