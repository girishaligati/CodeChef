def powerset(xs):
    result = [[]]
    for x in xs:
        newsubsets = [subset + [x] for subset in result]
        print('newsubsets'+str(newsubsets))
        print('result'+ str(result))
        result.extend(newsubsets)
    return result

print(powerset([1,2,3]))
print("Second code")

li = [1,2,3]
def powerset2(xs):
    result = [[]]
    for x in xs:
        for subset in result:
            newsubsets = [subset + [x]]
            print(newsubsets)
		    #newsubsets = [subset + [x] for subset in result]
        result.extend(newsubsets)
    return result
print(powerset2(li))
