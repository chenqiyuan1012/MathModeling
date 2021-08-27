function q=Q_t(t,ts)
t1=100;
for k=0:99
	if (t>ts+k*t1 & t<=ts+k*t1+0.2)
		temp=100*(t-k*t1-k*ts);
	elseif (t>ts+k*t1+0.2 & t<=ts+k*t1+2.2)
        temp=20;
	elseif (t>ts+k*t1+2.2 & t<=ts+k*t1+2.4)
		temp=(-100)*(t-ts-k*t1)+240;
	else
        temp=0;
    end
end
q=temp;
end