clear;
dw=38;
adf='data_o3_v2.mat';
ads='sitedb_gen.mat';
ad='.\sitedata\gen';
filename='.\sitedata\gen\num.mat';

sii.start=1;
data=load(adf);
los=unique(data.lo,'rows','stable');
if isfolder(ad)
    rmdir(ad,'s');
end
mkdir(ad);

num=0;
lof1=[];lof2=[];
lom1=[];lom2=[];
nop=[];
for i=1:dw-15:3600
    for j=1:dw-15:7200
        dx1=min(i-1,dw);
        dx2=min(3600-i,dw);
        dy1=min(j-1,dw);
        dy2=min(7200-j,dw);
        lob11=i-dx1;lob12=i+dx2;
        lob21=j-dy1;lob22=j+dy2;
        index1=los(:,1)<=lob12&los(:,1)>=lob11;
        index2=los(:,2)<=lob22&los(:,2)>=lob21;
        index=index1&index2;
        ccount=sum(index);
        if ccount~=0
            nf=0;
            nums='num_count';
            nums=strrep(nums,'count',num2str(ccount));
            tii=sort((los(index,1)-1)*7200+los(index,2));
            if isfield(sii,nums)
                siit=sii.(nums);
                ns=size(siit,2);
                for kk=1:ns
                    sub=sum(tii-siit(:,kk));
                    if sub==0
                        nf=1;
                        break;
                    end
                end
                if nf==1
                    continue;
                end
                siit(:,ns+1)=tii;
                sii.(nums)=siit;
            else
                sii.(nums)=tii;
            end
            intrep=0;
            lof=los(index,:);
            log1=i;
            log2=j;
            inputf=[];
            yf=[];
            lot1=0;lot2=0;
            for k=1:size(lof,1)
                indexf=data.lo(:,1)==lof(k,1)&data.lo(:,2)==lof(k,2);
                inputf=cat(1,inputf,data.input(indexf,:));
                yf=cat(1,yf,data.y(indexf,:));
                nc=sum(indexf);
                lot1=lot1+lof(k,1)*nc;
                lot2=lot2+lof(k,2)*nc;
            end
            lyf=size(yf,1);
            lot1=lot1/lyf;
            lot2=lot2/lyf;
            if lyf<80
                continue;
            end
            if lyf<300
                intrep=1;
            end
            num=num+1;
            lof1(num)=log1;lof2(num)=log2;
            lom1(num)=lot1;lom2(num)=lot2;
            nop(num)=lyf;
            filename_t=replace(filename,'num',num2str(num));
            save(filename_t,'inputf','yf','log1','log2','lot1','lot2','ccount','intrep');
        end
    end
end
save(ads,'lof1','lof2','lom1','lom2','nop');