# Creating Lambda functions

lambda_add_two_nums = lambda num1,num2: num1 + num2
print(lambda_add_two_nums(7,5))

## Write a lambda expression to concatinate two strings

lambda_concatinate_two_strings =  lambda str1, str2: str1 + str2
print(lambda_concatinate_two_strings("Hello"," World"))

## lambda to find the max of two nums

lambda_max_of_two_nums = lambda num1, num2: num1 if num1 >= num2 else num2
print(lambda_max_of_two_nums(4,2))
