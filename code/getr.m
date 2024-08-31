clear;
ad1='\match_o3\input_c\';
ad2='.\site_output_v2\';
ad3='.\site_result_v2\';
filepaths = dir(fullfile(ad1, '*.mat'));
len=length(filepaths);
for nn=1:len
    re=ones(3600,7200)*nan;
    ad_t1=fullfile(ad1, filepaths(nn).name);
    ad_t2=fullfile(ad2, filepaths(nn).name);
    ad_t3=fullfile(ad3, filepaths(nn).name);
    load(ad_t1,'bound');
    load(ad_t2);
    ll=size(bound,1);
    for i=1:ll
        re(bound(i,1),bound(i,2))=ypredf(i);
    end
    save(ad_t3,'re');
end