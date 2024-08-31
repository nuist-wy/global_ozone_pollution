function [s]=count_dis(lat1,lon1,lat2,lon2)
lat1=lat1*pi/180.0;
lat2=lat2*pi/180.0;
a=lat1-lat2;
b=(lon1-lon2)*pi/180.0;
s=2*asin(sqrt(sin(a/2.0).^2+cos(lat1).*cos(lat2).*sin(b/2.0).^2));
s=s*6378.137;