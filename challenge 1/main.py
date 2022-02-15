
def stringLen(phrase):
    """
        return the length of string

        >>>stringLen("hello")
        5
    """
    return len(phrase)

if __name__ == "__main__":
    testCases = ["", "H", "HELLO", "AMAZING"]
    for i in testCases:
        print(stringLen(i))