# YAMLScript

Programming language, using plain YAML syntax


## Examples

### Hello, World

```yaml
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
```

Run with `yamlscript examples/hello.yaml`

### Greeting

```yaml
# yaml-language-server: $schema=../schema.yaml
package: greeting
version: 1.0.0
description: A script to do something
author: John Doe

imports:
  std:
    version: 0.0.1

functions:
  main:
    description: |
      This is the main function of the script.
    commands:
      - greet:
          message: Hello world!
          name: John
          greeting: Hi
  greet:
    parameters:
      name:
        type: string
        description: The name of the person to greet
      greeting:
        type: string
        description: The greeting to use
        default: Hello
    description: |
      This function greets a person.
    commands:
      - std::echo:
          message: "{greeting} {name}!"
```

Run with `yamlscript examples/hello.yaml`
