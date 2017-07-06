def draw_list(list):
    for x in list:
        if isinstance(x,int):
            print '*'*x
        if isinstance(x,basestring):
            ch = x[0].lower()
            print ch * len(x)

x = [4, 6, 1, 3, 5, 7, 25]
draw_list(x)

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_list(y)