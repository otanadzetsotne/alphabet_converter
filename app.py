import os
import re
import json
from pathlib import Path
from functools import cache, partial

from fire import Fire


DIR_ALPHABETS = 'dictionaries'
PATH_ALPHABETS = os.path.abspath(DIR_ALPHABETS)


@cache
def get_alphabets():
    alphabet_names = os.listdir(DIR_ALPHABETS)

    alphabets = dict()
    for alphabet_name in alphabet_names:
        alphabet_path = os.path.abspath(f'{PATH_ALPHABETS}/{alphabet_name}')
        with open(alphabet_path, encoding='utf8') as f:
            alphabets.update({Path(alphabet_name).stem: json.load(f)})

    return alphabets


def get_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def save_file(text: str, converted_file_path: str):
    with open(converted_file_path, 'w', encoding='utf-8') as f:
        f.write(text)


def get_regex(alphabet: dict):
    # Sorted alphabet keys by key length
    alphabet_keys = sorted(
        [str(v) for v in alphabet.keys()],
        key=len,
        reverse=True,
    )

    # Regex keys
    keys = '|'.join(alphabet_keys)
    keys = rf'(?P<key>{keys})'

    return keys


def convert_letter(
        match: re.Match,
        alphabet: dict,
):
    # Get matched key
    key = str(match.group())
    # Get replacement
    replace: str = alphabet.get(key)

    return replace


def convert(
        alphabet_name: str,
        text: str,
):
    # Get all alphabets
    alphabets = get_alphabets()
    # Get current alphabet
    alphabet = alphabets.get(alphabet_name)

    if alphabet is None:
        raise ValueError(f'Alphabet {alphabet_name} not exists')

    # Create regex for keys
    regex = get_regex(alphabet)
    regex = re.compile(regex)

    # Convert alphabet
    return regex.sub(partial(convert_letter, alphabet=alphabet), text)


def convert_file(
        alphabet_name: str,
        file_path: str,
        converted_file_path: str,
):
    # Get text from file
    text = get_file(file_path)
    # Convert text
    text_converted = convert(alphabet_name, text)
    # Save converted text to file
    save_file(text_converted, converted_file_path)


if __name__ == '__main__':
    Fire({
        'convert_file': convert_file,
        'convert': convert,
    })
