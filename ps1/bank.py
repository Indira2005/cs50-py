greeting = input()
if greeting.startswith("h") or greeting.startswith("H"):
    if greeting.startswith("Hello") or greeting.startswith("hello"):
        print("$0")
    else:
        print("$20")
else:
    print("$100")

