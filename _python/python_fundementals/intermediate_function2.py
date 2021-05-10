# x = [ [5,2,3], [10,8,9] ] 
# x[1][0]=15
# print(x)

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name']='Bryant'
# print(students)

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }


# sports_directory['soccer'][0]='Andres'
# print(sports_directory)


# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(students):
    
#    for i in students:
       
#     print(i)


##iterateDictionary(students)

# def iterateDictionary2(key_name, dic):
#         for i in dic:
    
#             print(i[key_name])



# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
   for key in dict:
       print(len(dict[key]),key.upper())
       for val in dict[key]:
        print(val)


printInfo(dojo)

