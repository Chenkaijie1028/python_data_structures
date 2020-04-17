from stack import Stack


def parChecker(symbolString):
    stack = Stack()
    balabced = True
    index = 0
    while index < len(symbolString) and balabced:
        symbol = symbolString[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balabced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balabced = False
        index = index + 1

    if balabced and stack.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


if __name__ == "__main__":
    print parChecker('{{([][])}()}')
    print parChecker('[{()]')
