clear;
[cc,rr]=ndgrid(1:3600,1:7200);
cc=cc(:);rr=rr(:);
maxr=3600;
factor=4;
num=10;
r=25;

ads='sitedb_gen.mat';
filename_='.\sitedata\gen\num.mat';

sdb=load(ads);

se=ones(3600,7200,10)*nan;
weights=ones(3600,7200,10)*nan;
flag=ones(3600,7200)*nan;
nw1=ones(3600,7200)*nan;
nw2=ones(3600,7200)*nan;
for k=1:length(cc)
    dis=(sdb.lof1-cc(k)).^2+(sdb.lof2-rr(k)).^2;
    [dis,inx]=sort(dis);
    se(cc(k),rr(k),:)=inx(1:num);
    dis=dis(1:num);
    weightst=exp(-(dis/r^2));
    tow=sum(weightst);
    weights(cc(k),rr(k),:)=weightst/tow;
    if dis(num)>maxr
        flagt=0;
        if dis(num)<maxr*factor
            flagt=1;
            sub1=dis(num)-maxr;
            sub2=maxr*factor-dis(num);
            nw1t=sub2/(sub1+sub2);
            nw2t=sub1/(sub1+sub2);
        else
            nw1t=nan;
            nw2t=nan;
        end
    else
        flagt=2;
        nw1t=nan;
        nw2t=nan;
    end
    flag(cc(k),rr(k))=flagt;
    nw1(cc(k),rr(k))=nw1t;
    nw2(cc(k),rr(k))=nw2t;
end
save('gen_template.mat','se','weights','flag','nw1','nw2');