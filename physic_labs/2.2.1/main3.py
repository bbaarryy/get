import matplotlib.pyplot as plt
import math

file1 = open("./physic_labs/2.2.1/6_37.1.csv", "r")

names = ["37.1 мм рт ст", "78 мм рт ст", "121.9 мм рт ст", "159.7 мм рт ст"]
# file5 = open("./physic_labs/2.2.1/5.csv", "r")
# file6 = open("./physic_labs/2.2.1/6.csv", "r")

files = [file1]

def fun(arrx,arry):
    x = arrx
    y = arry

    xy_av = 0
    x_2_av = 0
    y_2_av = 0
    x_av=0
    y_av = 0

    for i in range(len(arrx)):
        x_av += x[i]
        y_av += y[i]
        xy_av += x[i] * y[i]
        x_2_av += x[i] * x[i]
        y_2_av += y[i] * y[i]
    
    x_av /= len(x)
    y_av /= len(y)
    xy_av /= len(x)
    x_2_av /= len(x)
    y_2_av /= len(x)

    b = (xy_av - x_av * y_av)/(x_2_av - x_av ** 2)
    a = y_av - b * x_av
   
    sigma_b = 1/(len(x))**0.5 * ( (y_2_av - y_av**2) / (x_2_av - x_av ** 2) - b**2) ** 0.5
    #print("sigma_b: ", sigma_b)
    
    hi = 0
    for i in range(len(arrx)):
        hi += (arry[i] - (b*arrx[i]+a))**2 / (0.001)**2
    
    print("HI", (hi**0.5, len(arrx)))
    return(sigma_b, b,a)

def main(file,ch):
    arrx = []
    arry = []
    for i in file:
        curr_x, curr_y = map(float, i.split(','))
        curr_y = math.log(curr_y)
        arrx.append(curr_x)
        arry.append(curr_y)
        #print(curr_x,curr_y)

    qa, a,b = fun(arrx,arry)
    D= 1550 * 5.3 / (2) * a
    print("!!!", ((20/1550)**2 + (0.1/5.3)**2 + (qa/a)**2)  ** 0.5)
    plt.plot([0,100],[b,a*100+b])

    plt.plot(arrx, arry, label = str(ch))

for i in range(1):
    main(files[i],names[i])

plt.ylabel("ln(U)",fontsize=20)
plt.xlabel("Время, секунды",fontsize=20)
plt.legend()
plt.grid()
plt.show()