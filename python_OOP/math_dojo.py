class MathDojo(object):
    def __init__(self):
        self.x = 0
    
    def add(self, *args):
        flattened = flatten(args,0,[])
        for y in flattened:
          self.x += y
        return self

    def subtract(self, *args):
        flattened = flatten(args,0,[])
        for y in flattened:
          self.x -= y
        return self

    def result(self):
        return self.x


def flatten(arr, i , newArr):
    if i == len(arr):
        return newArr
    if isinstance(arr[i],tuple):
        flatten(list(arr[i]),0,newArr)
    elif isinstance(arr[i],list):
        #return newArr.append(flatten(arr[i],0,newArr))
        flatten(arr[i],0,newArr)
    else:
        newArr.append(arr[i])
    return flatten(arr,i+1,newArr)

#print math_dojo().add(2).add(2, 5).subtract(3, 2).result()

#print MathDojo().subtract(2,[2,4,[5,6]]).result()

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, (2,3), [1.1, 2.3]).result()


print MathDojo().add((2,1)).result()