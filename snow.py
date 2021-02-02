def hello_world(snow):
    snowday =1
    if snow//2 == 0:
        print("yay!")
        return 0
    print("sad :(")
    return 1

if __name__ == "__main__":
    hello_world(0)
    hello_world(2)
    hello_world(3)
