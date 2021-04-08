
print("Hi, I'm a simple game based on game theory. I have been created by Nik and I'm here to help you to decide between 2 possibilies. Give me 2 inputs. E.g: studying in London and studying in Paris. Now give me 3 possibile outcomes for the 1st and 2nd input/choice. E.g: friends, fun, love. Finally, assign a value from 1 to 10 to the 3 outcomes, \nand I will give you the best choice according to Game Theory. Have fun!")


first_choice=str(input("Enter your first choice: "))
second_choice=str(input("Enter your second choice: "))


outcomes_a = input("Please enter three possible consequences that could result from your first choice (choose only one word and separate the three outcomes with a space): ")

list  = outcomes_a
a = outcomes_a

outcomes_b = input("Please enter three possible consequences that could result from your second choice (choose only one word and separate the three outcomes with a space): ")

list  = outcomes_b
b = outcomes_b
#print (list)

outcomesvalues_a = input("Assign a value from 1 to 10 to the 3 possible outcomes of your 1st choice (separate the values only with one space): ")
outcomes_values_1  = outcomesvalues_a.split(",")

list  = outcomesvalues_a.split()
#print (list)

outcomesvalues_b = input("Assign a value from 1 to 10 to the 3 possible outcomes of your 2nd choice (separate the values only with one space): ")
outcomes_values_2  = outcomesvalues_b.split(",")

list  = outcomesvalues_b.split()
for i,x in enumerate(outcomesvalues_b):
    if '\t' in x:
        outcomesvalues_b[i] = x[:x.index('\t')]

list = outcomes_a + outcomesvalues_a
choice_a = outcomes_a + outcomesvalues_a 
#print (list) 

list = outcomes_b + outcomesvalues_b
choice_b = outcomes_b + outcomesvalues_b
#print (list)
 
dict_a = {first_choice : outcomesvalues_a.split()}
#print(dict_a)

max_value_a = max(dict_a.values())
#print(max(max_value_a))

dict_b = {second_choice : outcomesvalues_b.split()}
#print(dict_b)


max_value_b = max(dict_b.values()) 
#print(max(max_value_b))

final_dic_a = {first_choice : max(max_value_a)}
#print(final_dic_a)

final_dic_b = {second_choice : max(max_value_b)}
#print(final_dic_b)

#merge the two dictionaries

final_dic = {**final_dic_a, **final_dic_b}
#print(final_dic)

final_choice = max(final_dic, key=final_dic.get)
print("According to game theory you should choose: {}".format(final_choice))

input('Press ENTER to exit') 