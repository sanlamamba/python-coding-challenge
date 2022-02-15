def varAtIndex(word,index):
    return word[index] if index < len(word) else "i is out of range" if word != "" else "Empty String"

if __name__ == "__main__":
    testCases = [["HELLO",2], ["PIZZA",4], ["",3], ["WORLD",15]]
    for i in testCases:
        print(varAtIndex(i[0],i[1]))