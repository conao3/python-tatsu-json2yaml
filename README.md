# python-tatsu-json2yaml

json2yaml converter powered by TatSu.

# Usage

Install `tatsu-json2yaml` in local Python.

```sh
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

Then, you could run `tatsu-json2yaml`.

```sh
$(.venv) tatsu-json2yaml
json2yaml> [1,2,3]
- 1
  2
  3

json2yaml> {"a":{"b":"c"},"d":[1,2,3]}
a:
  b: "c"
d:
  - 1
    2
    3
```

And you want to leave this virtualenv, execute below command.

```sh
$ deactivate
```
