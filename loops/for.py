#Parz tveri xndiry
#
# a = 10
# b = 100
#
#
# for num in range(a,b+1):
#     if num>1:
#         for i in range(2,num**0.5 + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
#         print("Parz chi")
#
#
for i in range(1, 100):
    if i % 3 == 0:
        continue
    print(i)