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

    if num == 1:
        stringcase.camelcase(str)
    elif num == 1:
        stringcase.capitalcase(str)
    elif num == 1:
        stringcase.constcase(str)
    elif num == 1:
        stringcase.lowercase(str)
    elif num == 1:
        stringcase.pascalcase(str)
    elif num == 1:
        stringcase.pathcase(str)
    elif num == 1:
        stringcase.sentencecase(str)
    elif num == 1:
        stringcase.snakecase(str)
    elif num == 1:
        stringcase.spinalcase(str)
    elif num == 1:
        stringcase.titlecase(str)
    elif num == 1:
        stringcase.trimcase(str)
    elif num == 1:
        stringcase.uppercase(str)
    elif num == 1:
        stringcase.alphanumcase(str)

def main():
    print('main')
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

print(__name__)

if __name__ == "__main__":
    main()