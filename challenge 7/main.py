from unittest import TestCase


def removeNChar(text,n):
    return text[:n] + text[n+1:] if n < len(text) else text

if __name__ == "__main__":
    testCases = [["HELLO",1], ["WORLD",3], ["DOG", 15], ["",2]]
    for i in testCases:
        print(removeNChar(i[0],i[1]))