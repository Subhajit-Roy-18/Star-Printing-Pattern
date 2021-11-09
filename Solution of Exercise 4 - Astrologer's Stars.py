# PROBLEM: Code a Program which will help the user in Printing a Star Pattern according to their wish of style.

print("Select the Pattern from the Two Options given below. \n")
print("Here's Option 1:-")

R = 5
while R >= 1:
    print(R * "*")
    R = R - 1



print()
print("Option 2 on your Screen:-")

H = 1
while H <= 5:
    print(H * "*")
    H = H + 1



print()
print("Enter either 1 or 2, according to your preference.")
Style = int(input())

print("OK, now Input the no. of Rows.")
Rows = int(input())



print()
print("Here we go.")

while Rows >= 1 and Style == 1:
    print(Rows * "*")
    Rows = Rows - 1


One = 1
while One <= Rows and Style == 2:
    print(One * "*")
    One = One + 1
