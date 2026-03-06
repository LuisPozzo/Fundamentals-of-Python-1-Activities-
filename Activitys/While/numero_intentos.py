range_approved = [1,2,3,4,5,6,7,8,9,10] 

while True:
    number = int(input('Enter a number between 1 - 10: '))
    if number in range:
        print(f"You entered the correct number {number in range}")
        break
    else:
        print('***Number out of range.')

