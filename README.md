# keyboard

Custom Keyboard Library implemented with pynput

Library Name: kbd

## Functions

| function         | description                                                                                         | args                                                                                  |
| ---------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `hotkey()`       | Initializes a hotkey                                                                                | key[`Key`], callback[`callable`], message[`str`], output[`bool`]                      |
| `once()`         | Initializes a one time use hotkey                                                                   | key[`Key`], callback[`callable`], message[`str`], init_output[`bool`], output[`bool`] |
| `toggle()`       | Initializes a hotkey that runs callback continuously with break of {sleep_time} between invocations | key[`Key`], callback[`callable`], message[`str`], output[`bool`], sleep_time[`int`]   |
| `wait()`         | Initializes listener to wait for key before activating function and moving on                       | until[`Key`], callback[`callable`], output[`bool`]                                    |
| `send()`         | Simulates keyboard sending key                                                                      | until[`Key`]                                                                          |
| `type_content()` | Simulates keyboard typing word at wpm                                                               | content[`str`], wpm[`int`], errors[`bool`], error_percentage[`int`]                   |

## Build

### Manually

1. Create Virtual Environement

```
python -m venv venv
```

2. Activate Virtual Environment

```
source ./venv/bin/activate
```

3. Update wheel and setuptools

```
pip install -U wheel setuptools
```

4. Build kbd

```
python -m setup bdist_wheel
```

5. Remove unnecessary files

```
rm -rf kbd.egg-info;rm -rf build;
```

6. Use wheel

- Built Wheel will be in dist/kbd\*.whl

### Makefile

1. Run make build

```
make build
```

2. Use wheel

- Built Wheel will be in dist/kbd\*.whl
