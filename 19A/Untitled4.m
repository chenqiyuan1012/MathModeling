format long
dsolve('Dp*x=(0.02893*p^2+3.077*p+1572)','p(0.85)=100','x')

function r=ro(x)
r=(17*exp((2000*172443911^(1/2)*atan((2893*172443911^(1/2)*x)/8622195550 + (3077*172443911^(1/2))/172443911))/172443911)*exp(-(2000*172443911^(1/2)*atan((8863*172443911^(1/2))/172443911))/172443911))/20
end

function r=R_t(t,pt,tp)
t0=tp+10
p0=100
ro0=ro(0)
for k=0:99
    temp=0.85*0.49*pi*(((2*p0-2*pt)/ro0)^0.5)*(t>k*t0 & t<=k*t0+tp)+0*(t<=(k+1)*t0 & t>k*t0+tp)
    if temp~=0
        r=temp
        return
    end
end
end

function q=Q_t(t,ts)
t1=100
for k=0:99
    temp=100*(t-k*t1)*(t>ts+k*t1 & t<=ts+k*t1+0.2)+20*(t>ts+k*t1+0.2 & t<=ts+k*t1+2.2)+((-100)*t+240)*(t>ts+k*t1+2.2 & t<=ts+k*t1+2.4)
    if temp~=0
        q=temp
        return
    end
end
end

function p_u=P(u,tp,ts)
p0=100
delta_t=0.01
tmp=p0
for j=0:u-1
    tmp=tmp+(0.02893*P(j,tp,ts)*P(j,tp,ts)+3077*P(j,tp,ts)+1572)/(P(j,tp,ts)*12500)*delta_t*(0.85*R_t(j,P(j,tp,ts),tp)-ro(P(j,tp,ts))*Q_t(j,ts))
end
p_u=tmp
end