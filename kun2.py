import os
os.system("cls")


#######       30-masala
# def printer(a):
#     for i in a:
#         print(f"{a.index(i) + 1} - toplam yigindisi {sum(i)}")

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# printer(a)










#######     31-masala       1-usul
# def printer(*args):
#     for i in args:
#         if i.count(2) >= 1:
#             print(i)

# a = [1, 2, 3]
# f = [2, 45 , 67]
# b = [4, 5, 6] 
# c = [7, 8, 9] 
# d = [10, 11, 12]
# g = [90, 3457, 2]

# printer(a, b, c, d, f, g)


                            # 2-usul
# def printer(*args):
#     result  = list(filter(lambda x: 2 in x, args))
#     return result

# a = [1, 2, 3]
# f = [2, 45 , 67]
# b = [4, 5, 6] 
# c = [7, 8, 9] 
# d = [10, 11, 12]
# g = [90, 3457, 2]

# print(printer(a, b, c, d, f, g))










########        32-masala
# def printer(*args):
#     result = list(filter(lambda x: 2 in x, args))
#     for i in result:
#         print(i.index(2) + 1)
    
        
# a = [1, 223, 32]
# f = [4543, 2,  672]
# b = [4, 5, 6432] 
# c = [7, 328, 219] 
# d = [120, 11, 12]
# g = [90, 3457, 2]

# printer(a, b, c, d, f, g)








######      33-masala
# def printer(*args):
#     for i in args:
#         if 2 in i[::-1]:
#             print(i.index(2) + 1)
#         else:
#             print(0)
        
        
# a = [1, 223, 2]
# f = [4543, 2,  672]
# b = [4, 5, 6432] 
# c = [7, 328, 219] 
# d = [120, 11, 12]
# g = [90, 3457, 2]

# printer(a, b, c, d, f, g)








######          34-masala
# def printer(*args):
#     for i in args:
#         if 2 in i:
#             print(sum(i))
#         else:
#             print(0)
        
# a = [1, 223, 2]
# b = [4, 5, 6432] 
# c = [7, 3, 2] 
# d = [120, 11, 12]
# f = [4543, 2,  672]
# g = [90, 3457, 2]

# printer(a, b, c, d, f, g)








######        35-masala
# def printer(*args):
#     for i in args:
#         print(len(i))
    
    
# a = [1, 223, 2]
# b = [4, 5, 6432] 
# c = [7, 3, 2] 
# d = [120, 11, 12]
# f = [4543, 2,  672]
# g = [90, 3457, 2]

# printer(a, b, c, d, f, g)










#######     36-masala
# def printer(*args):
#     count = 0
#     for i in args:
#         if sorted(i) == i:
#             count += 1
#     return count

# a = [1, 2, 223]
# b = [4, 5, 6432] 
# c = [7, 3, 2] 
# d = [120, 11, 12]
# f = [2,  672, 4543]
# g = [90, 3457, 2]

# print(printer(a, b, c, d, f, g))











######      37-masala       1-usul
# def finder(*args):
#     incresing = 0
#     deecreasing = 0
#     for i in args:
#         if sorted(i) == i:
#             incresing += 1
#         elif sorted(i) == i[::-1]:
#             deecreasing += 1
#     return f"{incresing} ta o'suvchi, {deecreasing} ta kamayuvchi"
    
# a = [1, 2, 223]
# b = [4, 5, 6432] 
# c = [7, 3, 2] 
# d = [120, 21, 11]
# f = [2,  672, 4543]
# g = [90, 3457, 2]

# print(finder(a, b, c, d, f, g))

                            # 2-usul
                            
# def finder(*args):
#     increasing = sum(1 for i in args if i == sorted(i))
#     decreasing = sum(1 for i in args if i == sorted(i, reverse=True))
#     return f"{increasing} ta o'suvchi, {decreasing} ta kamayuvchi"
 
# a = [1, 2, 223]
# b = [4, 5, 6432] 
# c = [7, 3, 2] 
# d = [120, 21, 11]
# f = [2,  672, 4543]
# g = [90, 3457, 2]

# print(finder(a, b, c, d, f, g))








######      38-masala
# def finder(*args):
#     for i in args:
#         if i == sorted(i):
#             print(1)
#         elif i == sorted(i, reverse=True):
#             print(-1)
#         else:
#             print(0)
            
# a = [1, 2, 223]
# b = [4, 5, 6432] 
# c = [7, 3, 2] 
# d = [120, 21, 11]
# f = [2,  672, 4543]
# g = [90, 3457, 2]

# finder(a, b, c, d, f, g)