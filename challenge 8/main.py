from dataclasses import replace


def replaceChar(text,currC,newC):
    return text.replace(currC,newC)


if __name__ == '__main__':
    testCases = [["Hello",'l', 's'], ['World', 'W', "A"], ["Python", "P", "x"], ["Python", "p", "a"]]

    for i in testCases:
        print(replaceChar(i[0],i[1],i[2]))
