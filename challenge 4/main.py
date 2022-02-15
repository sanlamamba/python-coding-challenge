def threeFirstAndLast(text):
    return "" if len(text) < 6 else text[0:3] +""+ text[-3:]



if __name__ == "__main__":
    testCases = ["WONDERFUL", "AMAZING", "BLUE"]
    for i in testCases:
        print(threeFirstAndLast(i))