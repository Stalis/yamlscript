from typing import Annotated
from typing import Any
from typing import Optional

from annotated_types import Len
from pydantic import BaseModel


class ParameterDefinition(BaseModel):
    type: str
    description: Optional[str] = None


CommandDefinition = Annotated[dict[str, dict[str, Any]], Len(max_length=1)]


class ReturnDefinition(BaseModel):
    type: str
    description: Optional[str] = None


class FunctionDefinition(BaseModel):
    description: Optional[str] = None
    parameters: dict[str, ParameterDefinition] = {}
    commands: list[CommandDefinition]
    returns: Optional[list[ReturnDefinition]] = []


class ImportDefinition(BaseModel):
    version: str


class SourceFile(BaseModel):
    package: str
    version: str
    description: Optional[str] = None
    author: Optional[str] = None

    imports: dict[str, ImportDefinition] = {}
    functions: dict[str, FunctionDefinition] = {}


if __name__ == "__main__":
    import yaml

    yaml.dump(SourceFile.model_json_schema(), open("schema.yaml", "w"))
