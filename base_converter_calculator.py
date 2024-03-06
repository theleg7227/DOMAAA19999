# adham ayman mohamed (20230042)
#first of all we must define group of function help us in convertion
# transformation from decimal to (binary or octal or hexadecimal )
#all the upcoming decimal to other base function considered as beta functions used in most of other convertion
def dec_bin(num):
    result = ""
    while num > 0:
        remainder = num % 2
        result = str(remainder) + result
        num = num // 2
    return result

def dec_to_oct(num):
    result = ""
    while num > 0:
        remainder = num % 8
        result = str(remainder) + result
        num = num // 8
    return result

def dec_to_hex(num):
    result = ""
    hexadecimal_digits = "0123456789ABCDEF"
    while num > 0:
        remainder = num % 16
        result = hexadecimal_digits[remainder] + result
        num //= 16
    return result


#define function helps in changing from binary to(decimal or octal or hexdecimal)
#recall them later to help in convertion down
def binary_to_decimal(binary_num):# this function help us in all binary convertion this is alpha function
    decimal_num = 0
    binary_num = str(binary_num)[::-1]# help in reversing bin 3la kalam eyad
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            decimal_num += 2 ** i
    return decimal_num

def binary_to_octal(binary_num):
# we change from binary to deciaml first and recall function dec to oct
# the above techniqe help in abbrevation of time and to not define many function as possible
    decimal_num = binary_to_decimal(binary_num)
    return dec_to_oct(decimal_num)

def binary_to_hexadecimal(binary_num):
# we change from binary to deciaml first and recall function dec to hex
#to continue our mechanism of to not define many function as possible

    decimal_num = binary_to_decimal(binary_num)
    return dec_to_hex(decimal_num)

#define functions help in changing from octal to (decimal or binary or hexadecimal)
#recll them later when need to this convertion
def octal_to_decimal(octal_num):
# first we define the alpha function that help us in other octal convertion
#then we recall it to define from decimal to other numerical system type
    decimal_num = 0
    octal_num = str(octal_num)[::-1]
    for i in range(len(octal_num)):
        decimal_num += int(octal_num[i]) * (8 ** i)
    return decimal_num

def octal_to_binary(octal_num):
#by using alpha convertion then using decimal convertion
    decimal_num = octal_to_decimal(octal_num)
    return dec_bin(decimal_num)

def octal_to_hexadecimal(octal_num):
# by using alpha convertion then using decimal convertion
    decimal_num = octal_to_decimal(octal_num)
    return dec_to_hex(decimal_num)

#define functions help in changing from hexadecimal to (decimal or binary or octal)
#recll them later when need to this convertion
def hexadecimal_to_decimal(hexadecimal_num):
#this also considered as alpha convertion that helps in other hexa convertion
    hex_chars = "0123456789ABCDEF"#any other char not from this considered an error
    decimal_num = 0
    hexadecimal_num = str(hexadecimal_num)[::-1]
    for i in range(len(hexadecimal_num)):
        decimal_num += hex_chars.index(hexadecimal_num[i]) * (16 ** i)
    return decimal_num

def hexadecimal_to_binary(hexadecimal_num):
# by using alpha convertion to convert it to decimal then using decimal convertion
    decimal_num = hexadecimal_to_decimal(hexadecimal_num)
    return dec_bin(decimal_num)

def hexadecimal_to_octal(hexadecimal_num):
# by using alpha convertion to convert it to decimal then using decimal convertion
    decimal_num = hexadecimal_to_decimal(hexadecimal_num)
    return dec_to_oct(decimal_num)


# here we are going to define a new function called convert which help to taking inputs from user from no. and base
#and also help in showing menu to user to select from as said in assignment paper

def convert():
    print("\n#MENU2#")
    num = input("\nEnter your number : ")#asking user to put that no. he\she wants to convert
    print("\nIn which system does your number belong (type the number)?")
    #starting asking them about the basethey put this no. in

    print("[1] : Binary\n[2] : Decimal\n[3] : Octal\n[4] : Hexadecimal")#this help showing him list
    print(50 * "=")
    from_base = int(input("Choice : "))#this is input that user inserted the number in
    print("\n#MENU3#")
    print("\nChoose the system you want to convert your number")
#start giving all possible transformation and convertion user could ask for
#transformation between  other numeric system base usig previous defined function
#the following conditions help in seeing destnation of user and what he need by giving menu to choose from
#also give him varable to choose in which system he wants to convert
    if from_base == 1:  # User input in binary
        temp = binary_to_decimal(num)
        print("[1] : Decimal\n[2] : Octal\n[3] : Hexadecimal")
    elif from_base == 2:  # User input in decimal
        temp = int(num)
        print("[1] : Binary\n[2] : Octal\n[3] : Hexadecimal")
    elif from_base == 3:  # User input in octal
        temp = octal_to_decimal(num)
        print("[1] : Binary\n[2] : Decimal\n[3] : Hexadecimal")
    elif from_base == 4:  # User input in hexadecimal
        temp = hexadecimal_to_decimal(num)
        print("[1] : Decimal\n[2] : Binary\n[3] : Octal")
    else:
        print("Invalid choice. Please select a valid option.")
        return
    print(50 * "=")
    to_base = int(input("to-base : "))
#first possible chance (#1)
# transformation from decimal to other numeric system base using previous defined function
    if from_base == 2:# user input in decimal
        if temp >= 0:
            if to_base == 1:# change from decimal to binary
                result = dec_bin(temp)
            elif to_base == 2:# change from decimal to octal
                result = dec_to_oct(temp)
            elif to_base == 3:#change from decimal to hexadecimal
                result = dec_to_hex(temp)
#second possible chance(#2)
# transformation from decimal to other numeric system base using previous defined function
    elif from_base == 1:# user inputs in binary
                if to_base == 1:# changes from binary to decimal
                    result = binary_to_decimal(num)
                elif to_base == 2:#changes from binary to octal
                    result = dec_to_oct(binary_to_decimal(num))
                elif to_base == 3:#changes from binary to hexadecimal
                    result = dec_to_hex(binary_to_decimal(num))
# third possible chance(#3)
# transformation from octal to other numeric system base using previous defined function
    elif from_base == 3:#user inputs in octal
                if to_base == 2:#changes from octal to decimal remember alpha convertion
                    result = octal_to_decimal(num)
                elif to_base == 1:#changes from octal to binary
                    result = dec_bin(octal_to_decimal(num))
                elif to_base == 3:#changes from octal to hexadecimal
                    result = dec_to_hex(octal_to_decimal(num))
# fourth and last possible chance(#4)
# transformation from hexadecimal to other numeric system base using previous defined function
    elif from_base == 4:# user inputs in hexadecimal
                if to_base == 1:#changes from hexa to decimal that was considered as alpha covertion func.
                    result = hexadecimal_to_decimal(num)
                elif to_base == 2:#changes from hexa to binary
                    result = dec_bin(hexadecimal_to_decimal(num))
                elif to_base == 3:#changes from hexa to octal
                    result = dec_to_oct(hexadecimal_to_decimal(num))


    if result is not None:
        print(f"The result is: {result}")
#here lets make our main menu block called menu1 as mentioned in assignment
#it will help program keeps running waiting for responce from user
if __name__ == "__main__":
    while True:
        print("\n# MENU1 #")
        print("a) insert a new number")
        print("b) exit program")
        choice = input("\nplease select a valid choice: ").lower()
        if choice == "a":
            convert()
        elif choice == "b":
            print("exiting program")
            break
        else:
            print("please enter a valid choice from above")
