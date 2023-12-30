import random
original_list=[1,"apple",3.14,"banana",42,"orange"]
shuffled_list=random.sample(original_list,len(original_list))
print("original list:",original_list)
print("shuffled list:",shuffled_list)
