print ("Введите колво школьников - ", end = " ")
n = int(input())
print ("Введите колво яблок - ", end = " ")
k = int(input())
print(f"{n}  школьников делят {k} яюлок поровну, неделящийся остаток остается в корзинке .") 
a = int(k / n)
print(f"у кажого школьника {a} яблок .") 
a = k % n 
print(f"останется в корзинке {a} яблок .")