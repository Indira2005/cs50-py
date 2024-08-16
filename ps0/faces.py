def convert(s):
    if ":)" in s:
        s = s.replace (":)", "🙂")
    if ":(" in s:
        s = s.replace(":(", "🙁")
    return s

def main ():
    input_str = input()
    print(convert(input_str))

main() 



