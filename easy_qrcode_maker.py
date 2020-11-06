import qrcode
from random import randint

def main():
    try:
        myQr = str(input("Type or paste your QR input: "))
        if len(myQr) >= 255:
            print("Input too long, max 255 chars")
            myQr = str(input("Type your QR input"))
        myQr = qrcode.make(myQr)
        fname = str(randint(1000,1000000)) + ".png"
        myQr.save(fname)
        print(f"\nSuccess, your filename is {fname} \nQR size is {myQr.size} \nQR type is {myQr.kind} \n")
        return 
    except BaseException as e:
        print("Something went wrong...",e)



if __name__ == "__main__":
    main()







