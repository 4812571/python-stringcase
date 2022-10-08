#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import stringcase

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    num = fdp.ConsumeIntInRange(0, 10)
    str = fdp.ConsumeString(128)

    if num == 0:
        stringcase.camelcase(str)
    elif num == 1:
        stringcase.capitalcase(str)
    elif num == 2:
        stringcase.constcase(str)
    elif num == 3:
        stringcase.lowercase(str)
    elif num == 4:
        stringcase.pascalcase(str)
    elif num == 5:
        stringcase.pathcase(str)
    elif num == 6:
        stringcase.sentencecase(str)
    elif num == 7:
        stringcase.snakecase(str)
    elif num == 8:
        stringcase.spinalcase(str)
    elif num == 9:
        stringcase.titlecase(str)
    elif num == 10:
        stringcase.trimcase(str)
    elif num == 11:
        stringcase.uppercase(str)
    elif num == 12:
        stringcase.alphanumcase(str)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()