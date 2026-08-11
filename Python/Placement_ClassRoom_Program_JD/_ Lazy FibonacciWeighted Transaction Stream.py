def fibonacci():
    a=1;
    b=1;
    while True:
        yield a
        a,b=b,a+b
def weigth_transaction_stream(transcation):
    fib=fibonacci()
    for amount in transcation:
        wegith=next(fib)
        yield amount*wegith
transcation=[100,200,150,50,400,90,60]
threhold=500;
weighted=weigth_transaction_stream(transcation)
filtered = (value for value in weighted if value > threhold)
result=[]

for i in range(3):
     result.append(next(filtered))
print(result)
    
    