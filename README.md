# caseConverter
A CLI tool to convert case of the input string, Made using python. The ouput is copied to your clipboard automatically.

## Usage
Convert The case of a given string. The tool automatically copies the output to your clipboard.


-u  Convert given string to upper Case. eg `python app.py -str "hello world" -to "u"` -> HELLO WORLD

-l  Convert given string to lower Case. eg `python app.py -str "hEllO woRld" -to "l"` -> hello world

-t  Convert given string to title Case. eg `python app.py -str "hello world" -to "t"` -> Hello World

-a  Convert given string to alternate Case. eg `python app.py -str "hello world" -to "a"` -> hElLo wOrLd

-i  Convert given string to inverse Case. eg `python app.py -str "hEllo WOrld" -to "i"` -> HeLLO woRLD

-s  Convert given string to sentence Case. eg `python app.py -str "hello world" -to "s"` -> Hello world

## Dependencies
It uses pyperclip to copy output to [clipboard](https://pypi.org/project/pyperclip/). Install it using `pip install pyperclip` 

## Authors

* **Pratik Kumar Singh** - *Initial work* - [singhkumarpratik](https://github.com/singhkumarpratik/)
