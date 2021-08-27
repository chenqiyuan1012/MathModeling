for tp=2:1:100
    for ts=50:0.5:97.6
        p0=100;
        delta_t=0.01;
        T=100*(tp+10);
        u=T/delta_t;
        tmp=100;
        jihe=[];
        for j=1:u
            t_j=(j-1)*delta_t;
            tmp=tmp+(0.02893*tmp*tmp+3077*tmp+1572)/(ro(tmp)*12500)*delta_t*(0.85*R_t(t_j,tmp,tp)-ro(tmp)*Q_t(t_j,ts));
            jihe=[jihe,tmp];
        end
        jihe;
        sum=0;
        xl=[];
        mini=100000;
        for v=1:u
            sum=sum+abs(jihe(v)-100);
            if (sum<mini)
                mini=sum;
                tp_final=tp;
                ts_final=ts;
            end
        end
        mini
        tp_final
        ts_final
    end
end