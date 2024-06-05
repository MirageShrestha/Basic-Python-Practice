x = input('enter a num')
y = input('enter second num')

try:
    z = int(x)/int(y)
    a = 'mirage'+7
except ZeroDivisionError as e:
    print('Exception occured', e)
    z = 0
except TypeError as te:
    print('Exception occured', te)

print (z)

'''skipped after zero division error'''
try:
  print(1)
  print(20 / 0)
  print(2) # 2 is skipped
except ZeroDivisionError:
  print(3)
finally:
  print(4)

'''Unsupported Operand'''
if __name__ == "__main__":
    x = input("Enter number 1: ")
    y = input("Enter number 2: ")
    try:
        z = x / int(y)

    except Exception as e:
        print("Exception type: ", type(e).__name__)
        print("Exception occurred:", e)
        z = None

    finally:
        print(z)

'''INDEX ERROR'''
list = [int(x) for x in input('Enter list:').split()]
try:
    i = int(input("Enter Index: "))
    print(list[i])

except IndexError:
    print("Index is not valid")

'''KEY ERROR'''
employees = [
    {"id": 1, "first_name": "Karan ", "middle_name": "Rama ", "last_name": "Reddy"},
    {"id": 2, "first_name": "Alex ", "last_name": "Gorge"},
    {"id": 3, "first_name": "Alice ", "middle_name": "M ", "last_name": "Warner"},
]

for employee in employees:
    try:
        full_name = employee['first_name'] + employee['middle_name'] + employee['last_name']
    except KeyError:
        full_name = employee['first_name'] + employee['last_name']
    finally:
        print(full_name)