# n = input("Enter a number")
# n = int(n)
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# indian = ['samosa', 'naan', 'roti']
# chinese = ['prawn', 'roll', 'keema noodles']
# italian = ['pizza', 'burger', 'pasta']
#
# dish = input("Enter dish name: ")
#
# if dish in indian:
#     print("Indian dish")
# elif dish in chinese:
#     print("Chinese dish")
# else:
#     print("Italian dish")

# score=70
#
# grade = "A" if score >= 80 else "B"
# print(grade)


'''FOR LOOP'''
# for expense in expenses:
#  total_expense = total_expense + expense
# print (total_expense)

# expenses = [1050, 2000, 5000, 2850]
# total_expense = 0
#
# for i in range(len(expenses)):
#     expense = expenses[i]
#     print(f'Month: {i+1}, Expense: {expense}')
#     total_expense +=   expense
# print("Total Expense:", total_expense)

# expenses = [1050, 2000, 5000, 2850]
#
# for i, expense in enumerate(expenses):
#     if expense >= 2000:
#         print(f" Month: {i+1}, budget exceeded: {expense}")
#     else:
#         print(f" Month {i+1}, Under budget: {expense}")

# locations = ['chair','sofa','table','keyboard']
# key_location = 'chair'
# for location in locations:
#     if location == key_location:
#         print(f"we found the key is {location}")
#         break
#     else:
#         print(f 'not in {location}')


# j = 3
# for i in range(1, j + 1):
#     print('*' * i)

# for i in range(11):
#     if i % 2 == 1:
#         continue
#     print(i)
#
# n = 0
# while n <= 10:
#     print(n)
#     n += 1

# for l in 'SkillBasics':
#     if l == 'i':
#         continue
#     print(l, end='')

# count=0
# transactions = [(456, 'f'), (457, 'n'), (458, 'w'), (459, 'f')]
# for transaction in transactions:
#     if transaction[1]!='f':
#         count+=1
# print(count)



# x = -1
# while x <=99:
#   x += 2
# print(x)

# for n in range(1, -6, -2):
#     print(n, end=', ')

# x=6
# for i in range(x, 1, -1):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()
#

# for i in range(1, 6, 1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

# sum = 0
# for i in range(1, 21):
#     if i % 2 == 1:
#         continue
#     else:
#         sum = sum + i
# print(sum)

# dice_result = [5, 6, 4, 2, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 6]
# # count_6 = 0
# # count_1 = 0
# # for i in dice_result:
# #     if i == 6:
# #         count_6 += 1
# #     elif i == 1:
# #         count_1 += 1
# # print(f'1 is repeated {count_1} times\n6 is repeated {count_6} times')
#
# two_6s = 0
# l = len(dice_result)
# for i in range(l-1):
#     if dice_result[i] == 6 and dice_result[i+1] == 6:
#         two_6s += 1
# print(two_6s)


# pushups = 0
# while True:
#     if pushups <= 50:
#         print("doing pushup.")
#         pushups += 1
#         if pushups == 50:
#             print("Congo babe")
#             break
#         elif pushups % 10 == 0:
#             q = input("Are you tired? (y/n)")
#             if q=="y":
#                 break
#             else:
#                 print(f'you have done {pushups} pushups, now {50-pushups} pushups remaining')
# print(f"you did total {pushups} pushups today")


# my_expense = [100, 200, 500, 700]
# her_expense = [1000, 2000, 5000, 7000]
# total = 0
#
# for expense in my_expense:
#     total += expense
# print("my_expence", total)
#
# for expense in her_expense:
#     total += expense
# print("her_expence", total)

'''FUNCTION'''
# def find_total(expenses):
#         '''
#         :param expenses: list of expenses
#         :return: total expenses
#         '''
#     total = 0
#     for expense in expenses:
#         total += expense
#     return total
#
#
# my_expense = [100, 200, 500, 700]
# her_expense = [1000, 2000, 5000, 7000]
#
# total = find_total(my_expense)
# print(f'my expense is {total}')
#
# total = find_total(her_expense)
# print(f'her expense is {total}')

# def aoc(r,h):
#     '''
#     :param r: radius of cylinder
#     :param h: height of cylinder
#     :return: area of cylinder
#     '''
#     pi=22/7
#     a=pi*r*r*h
#     return a
#
#
# print(aoc(58, 7))

'''Write a python function to check if any given number is a prime number and odd number?'''

# def prime (n):
#     poo = 0
#     po = 0
#     for i in range (1, n+1):
#         if n%i == 0 and n%2==1:
#             poo += 1
#         elif n%i == 0:
#             po += 1
#     if poo == 2:
#         return 1
#     elif po == 2:
#         return 0
#
# n=int(input("Enter n:"))
# p=prime(n)
# if p == 1:
#     print("Prime and odd")
# elif p == 0:
#     print("prime but not odd")
# else:
#     print("none")

'''Write a python function that will take n as input and print
 the pattern of n rows. If the n is even, then print it flipped.'''

# def odd(n):
#     for i in range(1, n+1, 1):
#         for j in range(1, i+1):
#             print("*", end=' ')
#         print()
#
# def even(n):
#     for i in range(n, 0, -1):
#         for j in range(0, i):
#             print("*", end=' ')
#         print()
#
# num = int(input("enter a number: "))
# if num%2 == 0:
#     print(even(num))
# else:
#     print(odd(num))


# def even(num):
#     if num%2 == 0:
#         return True
#     else:
#         return False
#
# def pattern(n):
#     if even(n):
#         for i in range(n, 0, -1):
#             for j in range(i):
#                 print("*", end=" ")
#             print()
#     else:
#         for i in range(n+1):
#             for j in range(i):
#                 print("*", end=" ")
#             print()
#
# pattern(4)

'''Mirage speaks a sentence in a different order. 
Let's say you want to convert a sentence to mirage’s speech.  
Write a function named mirage which will take a string 
as input and return the output after reversing the words of 
the sentence.'''

# def mirage(sentence):
#    words=[]
#    for word in sentence.split(' '):
#       words.append(word)
#
#    terminator=""
#    if words[-1].endswith('.') or words[-1].endswith('?'):
#       terminator=words[-1][-1]
#       words[-1]=words[-1][:-1]
#
#    words.reverse()
#
#    new_sentence = " ".join(words)
#    new_sentence = new_sentence+terminator
#    print(new_sentence)
#
# mirage("I love Jesus.")


# def pay_bill(expenses, percent_commission=0.098, offer_amount=None):
#     total_amount = 0
#     for amount in expenses:
#         total_amount += amount
#
#     extra_commission = 0
#     if offer_amount:
#         if total_amount >= offer_amount:
#             extra_commission = 0.012
#             print(f'congo for winning 1.2% commission')
#
#     commission_amount=total_amount*(percent_commission+extra_commission)
#     final_amount = total_amount - commission_amount
#     print(final_amount)
#
#
# pay_bill([100, 145, 567, 322], 0.078, 800)

# my_list = [1,2,3,4,5,6,7]
# for i in my_list:
#     my_list.remove(i)
# print(my_list)

'''Dictionary and Tuples'''
# def find_pe_and_pb(price, eps, book_value):
#     pe = price/eps
#     pb = price/book_value
#     return pe, pb
#
# pe_ratio, pb_ratio = find_pe_and_pb(100, 2, 4)
#
#
# print(pe_ratio )
# print(pb_ratio)

# contacts = [('rachel', 9867078356), ('samagya', 9841231743), ('mirage', 9848569098), ('parbat', 9823305496)]
# for contact in contacts:
#     if contact[0]=='mirage':
#         print(contact[1])
#     elif contact[0]=='rachel':
#         print(contact[1])
#     elif contact[0]=='parbat':
#         print(contact[1])
#     elif contact[0]=='samagya':
#         print(contact[1])

# d = {
#     'mirage': 9848569098,
#     'rachel': 9867078356,
#     'samagya': 9841231743,
#     'parbat': 9823305496
# }
#
# for name in d:
#     print(name, d[name])
#
# for name, number in d.items():
#     print(name,number)
#
# print(dir(d))
#
# print(list(d.keys()))

'''Create a list of your friends' names and now create a list
of tuples. The tuple should contain the friend’s name and
the length of the name. For Example: 
if someone’s name is Aditya, the tuple would be: (‘Aditya’, 6)
'''
# def list_of_tuples(friend_list):
#     new_list=[]
#     for friend in friend_list:
#         tuple=(friend, len(friend))
#         new_list.append(tuple)
#     print (new_list)
#
# friend = ['mirage', 'nishab', 'parbat']
# list_of_tuples(friend)

# my_expenses = dict()
# wife_expenses = dict()
#
# my_expenses['Clothes'] = 100
# my_expenses['Shoes'] = 1000
# my_expenses['Watch'] = 900
# my_expenses['Mobile Recharge'] = 699
# my_expenses['Petrol'] = 1980
#
# wife_expenses.update({
#     "Mobile Recharge" : 799,
#     "DTH recharge" : 999,
#     "Clothes" : 2310,
#     "Makeup" : 3670,
#     "Shoes" : 999
# })
#
# total = 0
# for key in my_expenses:
#     total += my_expenses[key]
# my_expenses['Total'] = total
# print(my_expenses['Total'])
#
# total = 0
# for tot in wife_expenses:
#     total+=wife_expenses[tot]
# wife_expenses['Total'] = total
# print(wife_expenses['Total'])
#
# def sort(dict):
#     sort_dict=sorted(dict.items(), key=lambda  kv:kv[1])
#     print(sort_dict)
# sort(my_expenses)


'''FILE HANDLING'''
# f = open("hello.txt", "r")
# for line in f:
#     print(line)
# f.close()

# with open("hello.txt", "r") as f:
#     line=f.readlines()
#     print(line)

# with open("mirage.txt", "w") as f:
#     f.writelines(["\nI am here",
#                   "\nhello",
#                   "\nnobody"
#                   "\neverybody"
#                   ])


# player_score={}
# with open("scores.csv", "r") as f:
#     for line in f:
#         player, score = line.split(',')
#         score = int(score)
#         if player in player_score:
#             player_score[player].append(score)
#         else:
#             player_score[player]=[score]
#
# for player, score in player_score.items():
#     min_score = min(score)
#     max_score = max(score)
#     avg_score = sum(score)/len(score)
#     print(f'max->{max_score}, min->{min_score}, avg->{avg_score}')
#

'''print the dictionary from the sourcs.csv files'''
# with open('student_marks.csv', 'r') as f:
#
#     d={}
#
#     keys=f.readline()
#     print(keys)
#
#     keys = keys.split(',')
#     keys[-1]=keys[-1][:-1]
#     print(keys)
#
#     for key in keys:
#         d[key]=[]
#     print(d)
#
#     for line in f.readlines():
#         data = line.split(',')
#         data[-1]=data[-1][:-1]
#
#
#         j=0
#         for key in d:
#             d[key].append(data[j])
#             j+=1
#     print(d)
#
#     import pprint
#     pprint.pprint(d)
#
#     print('keys: ')
#     print(d.keys())
#
#     print('values: ')
#     print(d.values())

