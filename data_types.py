#Numeric types - int, float, complex
a = 10 #int
b = 1.0 #float
c = 2 + 3j # complex number

print(type(a))
print(type(b))
print(type(c))

#Text type
d = "hello" 
e = 'world'
print (d + e)


#Boolean type
is_valid = True
is_not_valid = False

print(type(is_valid))


#Sequence type (list, tuple and range)
[1,2,3] #list - ordered, mutable/modifiable collection
(2,3,4) #tuple - ordered, immutable collection 
range(5) # range
print(range(5))

config_file = ['dbString','thread']
print(config_file.__len__())
config_file.append('password')
print(config_file)

colors = ('red', 'blue', 'green')

#range(start(optional), stop(required), step (option)))
range(5)
for i in range(2,5):
    print(i)


#Set types, set, frozenset
# set - unordered, mutable, unique element
# frozenset -  unordered, immutable

my_set = {1,2,2,3}
print(my_set)

my_frozenset = frozenset([7,4,5,5])
print(my_frozenset)

#mapping type - dict - {key: value}
person = {
            "name": "Gary",
            "age": 30
          }

print(type(person))


#Binary types - bytes, bytearray and memoryview - File upload, download
