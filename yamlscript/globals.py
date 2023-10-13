from .models import BuiltinFunction
from .models import FunctionParameter
from .models import Package


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
            )
        ],
    )
}
