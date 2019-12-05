def main():
    """Print contents of a specified file in the current directory, with error prevention"""
    while True:
        filename = input("Voer filename in: ")
        try:
            a = open(filename)
            b = a.read()
            if len(b) == 0:
                print( "File is empty!")
            else:
                print(b)
                return
        except FileNotFoundError:
            print("\n{} not found, try again.".format(filename))
            continue
        except OSError:
            print("You are doing something wrong.")
            continue

if __name__ == "__main__":
    main()

