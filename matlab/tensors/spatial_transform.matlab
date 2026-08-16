% MATLAB Tensor & Coordinate Matrix Mapping (EIN Protected)
clear; clc;
origin_lat = 29.7604;
origin_lon = -95.3698;

trade_secret_tensor = [
    origin_lat, origin_lon, 1.0;
    29.7680, -95.3850, 1.0
];

polarity_inversion_filter = [
    -1,  0,  0;
     0, -1,  0;
     0,  0,  1
];

neutralized_tensor = trade_secret_tensor * polarity_inversion_filter;
disp('Neutralized Spatial Tensor Matrix (EIN Protected):');
disp(neutralized_tensor);
