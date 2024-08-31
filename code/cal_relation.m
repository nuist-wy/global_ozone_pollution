clear;
maxr=3600;
factor=4;
num=10;
r=25;
adf='o3_ind.mat';
ads='sitedb_ind.mat';
ad='.\testdata\ind';
filenamet='.\testdata\ind\num.mat';
filenamet_='.\sitedata\ind\num.mat';
for ind=1:5
    adf_=strrep(adf,'ind',num2str(ind));
    ads_=strrep(ads,'ind',num2str(ind));
    ad_=strrep(ad,'ind',num2str(ind));
    filename=strrep(filenamet,'ind',num2str(ind));
    load(adf_);
    load(ads_);
    if isfolder(ad_)
        rmdir(ad_,'s');
    end
    mkdir(ad_);
    los=unique(lotest,'rows','stable');
    for k=1:length(los)
        dis=(lof1-los(k,1)).^2+(lof2-los(k,2)).^2;
        [dis,inx]=sort(dis);
        se=inx(1:num);
        dis=dis(1:num);
        weights=exp(-(dis/r^2));
        tow=sum(weights);
        weights=weights/tow;
        if dis(num)>maxr
            flag=0;
            if dis(num)<maxr*factor
                flag=1;
                sub1=dis(num)-maxr;
                sub2=maxr*factor-dis(num);
                nw1=sub2/(sub1+sub2);
                nw2=sub1/(sub1+sub2);
            else
                nw1=nan;
                nw2=nan;
            end
        else
            flag=2;
            nw1=nan;
            nw2=nan;
        end
        index=lotest(:,1)==los(k,1)&lotest(:,2)==los(k,2);
        inputf=teindata(index,:);
        yf=teoutdata(index);
        coord=lotest(index,:);
        yymm=tstest(index,1:2);
        filename_t=replace(filename,'num',num2str(k));
        save(filename_t,'inputf','yf','coord','yymm','se','weights','flag','nw1','nw2');
    end
end