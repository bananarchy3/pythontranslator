import os
from translate import Translator

os.chdir(r'C:\Users\savew\Desktop')

output_lang = input('Enter output language ISO code. A full list is available at '
                    'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes')
translator = Translator(to_lang=output_lang)

try:
    with open('input.txt', mode='r', encoding="utf-8") as my_file:
        text = my_file.read()
        translation = str(translator.translate(text))
        # Creates a new output file for translated text.
        with open('output.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('File not found, check your file path or file name')
