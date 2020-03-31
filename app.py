#! /usr/bin/env python
import argparse,textwrap
import pyperclip

# for multi-line description
class SaneFormatter(argparse.RawTextHelpFormatter, 
                    argparse.ArgumentDefaultsHelpFormatter):
    pass

def run(args):
    res=''
    s=args.strInput
    caseInput=args.caseInput
    if caseInput=='u':
        s=s.upper()
    elif caseInput=='l':
        s=s.lower()
    elif caseInput=='t':
        s=s.title()
    elif caseInput=='a':
        for i in range(len(s)):
            if not i%2==0:
                res+=s[i].upper()
            else:
                res+=s[i].lower()
        s=res
    elif caseInput=='i':
        s=s.swapcase()
    elif caseInput=='s':
        firstLetter=s[0]
        firstLetter=firstLetter.upper()
        s=firstLetter+s[1:]
    print(s)
    pyperclip.copy(s)
def main():
    parser=argparse.ArgumentParser(description='''Convert The case of a given string. The tool automatically copies the output to your clipboard.
-u  Convert given string to upper Case. eg python app.py -str "hello world" -to "u" -> HELLO WORLD
-l  Convert given string to lower Case. eg python app.py -str "hEllO woRld" -to "l" -> hello world
-t  Convert given string to title Case. eg python app.py -str "hello world" -to "t" -> Hello World
-a  Convert given string to alternate Case. eg python app.py -str "hello world" -to "a" -> hElLo wOrLd
-i  Convert given string to inverse Case. eg python app.py -str "hEllo WOrld" -to "i" -> HeLLO woRLD
-s  Convert given string to sentence Case. eg python app.py -str "hello world" -to "s" -> Hello world
''', formatter_class=SaneFormatter)
    parser.add_argument("-str",help="input string" ,dest="strInput", type=str, required=True)
    parser.add_argument("-to",help="To upper case" ,dest="caseInput", type=str, required=True)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
	main()