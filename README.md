# Alphabet Converter

Alphabet Converter is a script that converts letters from one language to another.
Good way to learn some new language's alphabet, because text, that you read,
is still on your native language, but it is written with another languages letters.

## Setup

* Clone this repository  to your local storage.
    ```commandline
    git clone https://github.com/otanadzetsotne/alphabet_converter
    ```
* From repository folder install all requirements
  to your local Python virtual environment.
  ```commandline
  pip install -r requirements.txt
  ```
* Add to [dictionaries](./dictionaries/) folder new JSON file with your
  alphabet translations (just Russian to Georgian yet).
  ```json
  {
  "А": "ა",
  "а": "ა",
  "Б": "ბ",
  "б": "ბ",
  "Дз": "ძ",
  "дз": "ძ"
  }
  ```
  
## Using

Run commands from your shell.

* You could convert plain text.

```commandline
python app.py convert ru_ge 'Some text to convert'
```

* And you could convert utf-8 encoded text files, giving path to file and 
path to new file with converted text, that will be created automatically.

```commandline
python app.py convert_file ru_ge path_to_file.txt path_to_converted.txt
```

## License

MIT License

Copyright (c) 2022 Tsotne Otanadze

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

