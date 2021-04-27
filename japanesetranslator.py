import os
from translate import Translator

os.chdir(r'C:\Users\savew\Desktop')

translator = Translator(to_lang='ja')

try:
    with open('test.txt', mode='r', encoding="utf-8") as my_file:
        text = my_file.read()
        translation = str(translator.translate(text))
        # Creates a new output file for translated text.
        with open('ja-test.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('File not found, check your file path')
