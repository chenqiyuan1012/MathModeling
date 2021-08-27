import numpy as np
import pandas as pd
from math import exp
from math import atan
from math import pi
from math import sqrt


def ro(x):
    return (17*exp((sqrt(2000*172443911)*atan((sqrt(2893*172443911)*x)/8622195550 + sqrt((3077*172443911))/172443911))/172443911)*exp(-(sqrt(2000*172443911)*atan(sqrt(8863*172443911)/172443911))/172443911))/20


def Q(t, ts):
    t1 = 100
    for k in range(100):
        if (t > ts+k*t1 and t <= ts+k*t1+0.2):
            return 100*(t-k*t1-ts)
        elif (t > ts+k*t1+0.2 and t <= ts+k*t1+2.2):
            return 20
        elif (t > ts+k*t1+2.2 and t <= ts+k*t1+2.4):
            return (-100)*(t-ts-k*t1)+240
        elif ((t > ts+k*t1+2.4 and t <= ts+k*t1+t1) or t <= ts):
            return 0


def R(t, pt, tp):
    t0 = tp+100
    p0 = 160
    ro0 = 0.871
    for k in range(100):
        if (t >= k*t0 and t <= k*t0+tp):
            return 0.85*0.49*pi*(sqrt(abs(2*p0-2*pt)/ro0))
        elif(t > k*t0+tp and t < k*t0+t0):
            return 0


def find():
    min_sum = 0
    for tp in np.arange(0.01, 3, 0.01):
        for ts in range(50, 100, 1):
            p0 = 100
            delta_t = 1
            T = int(100*(tp+10))
            u = int(T/delta_t)
            tmp = 100
            ls = []
            for j in range(1, u+1):
                t_j = (j-1)*delta_t
                # print(t_j)
                #print(R(t_j, tmp, tp))
                # print(tp)
                tmp = tmp+(0.02893*tmp*tmp+3.077*tmp+1572)/(ro(tmp)*12500) * \
                    delta_t*(0.85*R(t_j, tmp, tp)-ro(tmp)*Q(t_j, ts))
                ls.append(tmp)
            # print(ls)
            sum = 0

            for v in range(0, u):
                sum = sum+abs(ls[v]-100)

            if(sum < min_sum or min_sum == 0):
                min_sum = sum
                tp_final = tp
                ts_final = ts
                print(min_sum)
                print(tp_final)
                print(ts_final)


find()
