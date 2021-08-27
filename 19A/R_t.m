function r=R_t(t,pt,tp)
t0=tp+10;
p0=100;
ro0=0.871
for k=0:99
	if (t>k*t0 & t<=k*t0+tp)
        r=0.85*0.49*pi*(((2*p0-2*pt)/ro0)^0.5);
    elseif (t>k*t0+tp & t<k*t0+t0)
        r=0;
    end
end
end
