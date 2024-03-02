



def countdown(num):
    while num > 0:
        print(f'{num} SECOND(S)!')
        num -= 1
countdown(20)
print("HAPPY NEW YEAR!")


import time

def countdown_with_sleep(num):
    while num > 0:
        print(f'{num} SECOND(S)!')
        time.sleep(1) 
        num -= 1
countdown(10)
print("HAPPY NEW YEAR!")

