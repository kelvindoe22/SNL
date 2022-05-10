import sys



def fmt(word: str):
    words = word.split("|")
    words = list(map(str.strip, words))
    val = ""
    for i in words[1]:
        val += f"{words[0]}{i}, "
    return val



def lt65(word: str) -> str:
    if len(word) >= 65:
        pos = word.find(",", 60)
        return word[:pos+1] + '\n' + lt65(word[pos+2:])
    return word


if __name__ == "__main__":
    a = []
    with open(sys.argv[1],"r") as read:
        a.extend(read.read().split("\n"))
    
    
    val = ""
    with open(sys.argv[2],"a+") as f:
        for i in a:
            if a[len(a) - 1] == i:
                val += f"{ fmt(i)[:-2] }"
            else:
                val += f"{ fmt(i) }"
        try:
            data = sys.argv[3]
        except:
            data = "data"
        f.write(f"\n{data} <- c({lt65(val)});")