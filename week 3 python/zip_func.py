user_id = ['user1', 'user2', 'user3']
names = ['harshit', 'mohit','rohit']
last_name = ['vashistha', 'sarpal', 'sharma']
# in  name ko combkine karna ha
# we use zip olbject
# jaise hi shoti list khata ho jayegi zip khatam ho zayegi
print(list(zip(user_id,names)))



# nicche dayi  gayi list me tuple ha har tuple    ko dict me convert kar sakte ha

example = [('a', 1), ('b',2),]
print(dict(example))