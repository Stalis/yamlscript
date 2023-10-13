from abc import ABC
from typing import Any
from typing import Callable
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Import(BaseModel):
    name: str
    package: "Package"


class FunctionParameter(BaseModel):
    name: str
    type: str
    description: Optional[str] = None


class ReturnValue(BaseModel):
    type: str
    description: Optional[str] = None


class CommandExpression(BaseModel):
    command: str
    parameters: dict = Field(default_factory=dict)


class Function(BaseModel, ABC):
    name: str
    description: Optional[str] = None
    parameters: list[FunctionParameter] = Field(default_factory=list)
    returns: list[ReturnValue] = Field(default_factory=list)


class UserFunction(Function):
    commands: list[CommandExpression] = Field(default_factory=list)


class BuiltinFunction(Function):
    func: Callable[[dict[str, Any]], Optional[list]]

    def __call__(self, args: dict[str, Any]) -> Optional[list]:
        return self.func(args)


class Package(BaseModel):
    name: str
    version: str
    description: Optional[str] = None
    author: Optional[str] = None
    imports: dict[str, "Package"] = Field(default_factory=dict, repr=False)
    functions: list[Function] = Field(default_factory=list, repr=False)
