import time
start_time=time.time()
for i  in range(5):
    print(i*i)
    for j in range(5000):
        for k in range(5000):
            l=k*k
end_time=time.time()
print('%.2f'%(end_time-start_time))