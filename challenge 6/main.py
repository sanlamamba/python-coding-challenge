def isNumbersOnly(text):
    return text.isnumeric()


if __name__ == "__main__":
    testCases = ["HELLO", "4567", "HELLO59", ""]
    for i in testCases:
        print(isNumbersOnly(i))