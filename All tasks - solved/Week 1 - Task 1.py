cat_a = [1,2,3,4,5]
cat_b = [10,20,30]

def cal_sts(data : list[float]):
    """this function  is to calculate the mean and max of the data"""
    return {"mean":sum(data) /  len(data) ,
     "max": max(data)}

print(cal_sts(cat_a))
print(cal_sts(cat_b))