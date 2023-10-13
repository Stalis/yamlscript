test_script = """
package: hello
version: 1.0.0

imports:
  std:
    version: 0.0.1

functions:
  main:
    commands:
      - std::echo:
          message: Hello world!
"""

from yamlscript.main import compile
from yamlscript.main import read_source
from yamlscript.main import run_func


def test_helloworld(tmp_path, capsys):
    script_file = tmp_path / "helloworld.yaml"
    script_file.write_text(test_script)
    pkg = compile(read_source(script_file))

    assert pkg.functions[0].name == "main"
    run_func(pkg, "main", {})

    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == "Hello world!\n"
