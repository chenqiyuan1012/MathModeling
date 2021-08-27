
function [result2]=pic
k=1;
min_result=0;
min_ts=0;
for tp=0.28:0.001:0.29
        [p,result]=module(100,0.85,1000,tp,50);
        x(k)=tp;
        y(k)=result;
        if(result<min_result | min_result==0)
            min_result=result;
            %min_ts=ts;
        end
        k=k+1;
end
[m,i]=min(y);
plot(x,y)
result2=0.27+i*0.0001;
min_ts
end
