#SETSSSS
#unique_numbers =[1,2,2,3,4,4,5]
#print (unique_numbers)
#new_set=set(unique_numbers)
#new_list=list(new_list)
#print(list(set(unique_numbers)))
#print (new_list)
#sets are desgined to contaim unique elements hence is a number is duplicated only one of the duplicates is seen
#number_string="12345"
#number_set=set(number_string)

#print(number_set)
#the response is false since the number_set has strings not an integer
#print(1 in number_set)
#response is true since 1 is a string in the set
#print('1' in number_set)

# number_range =(1,8)
# here the output is {1, 6, 7, 8, 9, 10} since the range is the number 1 and 8
# but if it was number_range =range(1,8)- this means the range is between 1 and 8 so 
# the output will be {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# numbers_set = set(number_range)

# numbers_set2 = {6, 7, 8, 9, 10}
# numbers_combined = numbers_set.union(numbers_set2)
# print(numbers_combined)
#SETSSS
numbers = [1, 2, 3, 4, 5]
numbers_set = set(numbers)
# Combine two sets
numbers_set2 = {6, 7, 8, 9, 10}
numbers_combined = numbers_set.union(numbers_set2)
print(numbers_combined)

# Find the intersection of two sets
numbers_intersection = numbers_set.intersection(numbers_set2)
print(numbers_intersection)