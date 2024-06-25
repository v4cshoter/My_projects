from data import pigeons

my_tuple = ()
my_list = []
# кортеж в кортеже
for i in range(0, len(pigeons), 2):
    if i + 1 < len(pigeons):
        my_tuple = (pigeons[i], pigeons[i + 1])
    else:
        my_tuple = (pigeons[i],)
    my_list.append(my_tuple)
print(my_list)

# список в списке
my_list2 = []
for i in range(0, len(pigeons), 2):
    my_list2.append(pigeons[i:i + 2])
print(my_list2)
