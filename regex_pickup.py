import re


def partialExtraction(path: str):
    return ''.join(re.findall('win.*\.', path))[:-1]


if __name__ == "__main__":
    test = '20210114-01-win_basic_setup.log'
    result = partialExtraction(test)
    print(result)
    test = '20210114-01-win_update.log'
    result = partialExtraction(test)
    print(result)
    txt = '-abcd.'
    print(txt[1:-1])
