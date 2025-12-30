# tatsu-json2yaml

A JSON to YAML converter built with [TatSu](https://github.com/neogeny/TatSu), a Python library for parsing grammars.

## Features

- Interactive REPL for quick conversions
- File-based conversion via command line
- Custom JSON parser using TatSu grammar

## Installation

```bash
pip install tatsu-json2yaml
```

### Development Setup

```bash
git clone https://github.com/conao3/python-tatsu-json2yaml.git
cd python-tatsu-json2yaml
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Usage

### Interactive Mode

Run the command without arguments to enter the interactive REPL:

```bash
tatsu-json2yaml
```

```
json2yaml> [1, 2, 3]
- 1
  2
  3

json2yaml> {"a": {"b": "c"}, "d": [1, 2, 3]}
a:
  b: "c"
d:
  - 1
    2
    3
```

### File Mode

Convert a JSON file directly:

```bash
tatsu-json2yaml -i input.json
```

## Requirements

- Python 3.10

## License

See [LICENSE](LICENSE) for details.
