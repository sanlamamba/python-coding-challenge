
def reverseString(text):
    return text[::-1]

if __name__ == "__main__":
    testCases = ["Hello", "Wo", ""]
    for i in testCases:
        print(reverseString(i))