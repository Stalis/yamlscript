from pathlib import Path
import sys
from typing import Optional

import yaml
from yamlscript.source import SourceFile

from .globals import GLOBALS
from .models import BuiltinFunction
from .models import CommandExpression
from .models import Function
from .models import FunctionParameter
from .models import Package
from .models import ReturnValue
from .models import UserFunction


def find_func(pkg: Package, name: str) -> Optional[Function]:
    for func in pkg.functions:
        if func.name == name:
            return func

    parts = name.split("::")
    if len(parts) == 2:
        for key, imported in pkg.imports.items():
            if key == parts[0]:
                return find_func(imported, parts[1])

    return None


def run_func(pkg: Package, name: str, args: dict) -> list:
    func = find_func(pkg, name)
    if not func:
        raise ValueError(f"Function {name} not found")

    for param in func.parameters:
        if param.name not in args:
            raise ValueError(f"Missing parameter {param.name}")

    if callable(func):
        func: BuiltinFunction = func
        return func(args)

    context = {
        param.name: args[param.name] for param in func.parameters if param.name in args
    }

    for cmd in func.commands:
        params = {key: value.format(**context) for key, value in cmd.parameters.items()}
        run_func(pkg, cmd.command, params)

    return {}


def find_package(pkg: Package, name: str) -> Optional[Package]:
    if pkg.name == name:
        return pkg

    for name, package in GLOBALS.items():
        if name == name:
            return package

    return None


def read_source(path: Path) -> SourceFile:
    with path.open("r") as f:
        return SourceFile(**yaml.full_load(f))


def main():
    file = read_source(Path(sys.argv[1]))

    pkg = Package(
        name=file.package,
        version=file.version,
        description=file.description,
        author=file.author,
    )
    for key, params in file.imports.items():
        pkg.imports[key] = find_package(pkg, key)

    for name, item in file.functions.items():
        function = UserFunction(name=name, description=item.description)
        for param_name, param in item.parameters.items():
            function.parameters.append(
                FunctionParameter(
                    name=param_name,
                    type=param.type,
                    description=param.description,
                )
            )
        for ret in item.returns:
            function.returns.append(
                ReturnValue(type=ret.type, description=ret.description)
            )

        for cmd in item.commands:
            if len(cmd) != 1:
                raise ValueError("Command must be a single key dict")

            cmd_name, cmd_params = [(key, value) for key, value in cmd.items()][0]

            function.commands.append(
                CommandExpression(
                    command=cmd_name,
                    parameters=cmd_params,
                )
            )

        pkg.functions.append(function)

    run_func(pkg, "main", {})


if __name__ == "__main__":
    main()
