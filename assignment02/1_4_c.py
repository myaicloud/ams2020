from scipy import optimize

# values
x1 = 15.833
y1 = 42.556
x2 = 64.039
y2 = 49.128
d1 = 37.892
d2 = 42.926

# sat 1
def func1(x, y):
    return pow(x1 - x, 2) + pow(y1 - y, 2) - d1

# sat 2
def func2(x, y):
    return pow(x2 - x, 2) + pow(y2 - y, 2) - d2

result_yr = optimize.root(func1, 0.3, 0.3)
#print(result_yr)
yr = result_yr.x[0]

result_xr = optimize.root(func2, 0.1, 0.1)
#print(result_xr)
xr = result_xr.x[0]

print([xr, yr])
# result: [64.06073181878837, 15.8859375]