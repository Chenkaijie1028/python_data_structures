from deque import Deque


def palindrome(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == "__main__":
    print(palindrome("radar"))
    print(palindrome("lsdkjfskf"))
