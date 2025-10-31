# Find the y value of line of best fit

'''
Find line of best fit via scipy'.stats.linregress. 
Return y value of best fit.

Input:

    x: x data
    (need not be numeric, but assumed equally spaced and increasing.
    Only the indices are used for fitting)

    y: y data 

    flg_return=False: whether to return more fit results default false

output:
    y_fit: y value of line of best fit at each x location
    
    (if flg_return is True)
    poly: the polynomial of line of best fit [m, b], y = m*x + b 
    r: r value 
    p_value: p-value testing if the gradient is 0
'''

import numpy as np
import scipy.stats

def find_line_of_best_fit(x,y, flg_return=False):
    
    x_indices = np.arange(len(x))
    
    # perform linear regression
    reg_result = scipy.stats.linregress(x_indices, y)
    
    # gradient and y-intercept of line of best fit [gradient, y-intercept]
    poly = [reg_result[0], reg_result[1]]
    
    # y value of best fit line
    y_fit = np.polyval(poly, x_indices)
    
    # r
    r = reg_result[2]
    
    # p-value testing if the gradient is 0
    p_value = reg_result[3]
    
    if flg_return == True:
        return y_fit, poly, r, p_value
    else:
        return y_fit
    
    
