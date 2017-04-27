while True:
    try:
        x = int(input("key a number"))
        break
    except ValueError:
        print("other message")

print("this is in end")