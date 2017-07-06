
def making_tuples(dict):
    tuple_list = []
    for key,data in dict.iteritems():
        tuple_list.append((key,data))
    return tuple_list

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

tuple_list=making_tuples(my_dict)
print tuple_list