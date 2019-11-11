import numpy as np 
import matplotlib.pyplot as plt 
  
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 


def rent_at_month(n, c, m):
    return m*n+c
    
def main(): 
    # observations 
    monthCount = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    x = monthCount
    houseRent = np.array([14500, 14500, 14000, 15000, 16000, 16000, 16000,16500, 16500, 18000, 18000, 18500]) 
    y =  houseRent 
    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients c and m : ")

    print (b[0])
    print (b[1])

    print("\n")

    print ("price at jan 20 : " )
    
    rent = rent_at_month(13, b[0], b[1])
    
    print (rent )
    
    print ("price at june 20 : " )
    
    rent2 = rent_at_month(19, b[0], b[1])
    
    print (rent2 )

    # plotting regression line 
    plot_regression_line(x, y, b) 
  
if __name__ == "__main__": 
    main()
