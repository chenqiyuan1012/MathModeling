
function [result2]=testt
k=1;
min_result=0;
min_ts=0;
for ts=50:1:70
    for tp=0.27:0.0001:0.29
        [p,result]=module(100,0.85,1000,tp,ts);
        y(k)=result;
        if(result<min_result | min_result==0)
            min_result=result;
            min_ts=ts;
        end
        k=k+1;
    end
end
[m,i]=min(y);
%result2=i*0.001;
result2=0.27+i*0.0001;
min_ts
end
