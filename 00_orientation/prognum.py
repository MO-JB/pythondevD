#フィボナッチ数列を計算する関数

def fibo(i):
    if i == 1:
        return 1
    if i == 2:
        return 1
    else:
        return fibo(i-1) + fibo(i-2)
    

