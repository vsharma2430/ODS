#NOMOGRAPH OCTAGON
#START E/D - 0.3 , END E/D - 0.5 , STEP - 0.005

import numpy as np
import matplotlib.pyplot as plt

eDivD_octagon_diagonal = np.array([0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.06,0.065,0.07,0.075,0.08,0.085,0.09,0.095,0.1,0.105,0.11,0.115,0.12,0.125,0.13,0.135,0.14,0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3,0.305,0.31,0.315,0.32,0.325,0.33,0.335,0.34,0.345,0.35,0.355,0.36,0.365,0.37])
L_octagon_diagonal = np.array([1, 1.04, 1.08125, 1.12, 1.1625, 1.2, 1.24375, 1.275, 1.325, 1.35, 1.406, 1.43, 1.487, 1.5, 1.568, 1.6, 1.65, 1.7, 1.73125, 1.76, 1.8125, 1.84106, 1.89375, 1.93032, 1.98745, 2.04957, 2.0717, 2.11883, 2.16596, 2.21809, 2.27021, 2.33447, 2.37872, 2.43298, 2.48723, 2.57149, 2.61574, 2.66, 2.70426, 2.75851, 2.81277, 2.86489, 2.92702, 2.98915, 3.06666, 3.1334, 3.22553, 3.33766, 3.42979, 3.50149, 3.6, 3.65745, 3.8333, 3.88926, 4.0666, 4.07106, 4.3, 4.33287, 4.6, 4.61468, 4.9, 4.93693, 5.2, 5.29462, 5.7, 5.72231, 6.2, 6.45, 6.7, 6.95, 7.2, 7.5, 7.8, 8.25, 8.7 ]) 
k_octagon_diagonal = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.055, 0.07, 0.09, 0.11, 0.125, 0.14, 0.155, 0.17, 0.185, 0.2, 0.215, 0.23, 0.245, 0.26, 0.275, 0.29, 0.305, 0.32, 0.335, 0.35, 0.365, 0.38, 0.3925, 0.405, 0.4175, 0.43, 0.4425, 0.455, 0.4675, 0.48, 0.4925, 0.505, 0.5175, 0.53, 0.5425, 0.555, 0.5675, 0.58, 0.595, 0.61, 0.6225, 0.635, 0.6475, 0.66, 0.6725, 0.685, 0.6975, 0.71])
    
def nomograph_value(x_val,ed_array,L_array,k_array):
    x_interp = x_val
    y_interp_1 = np.interp(x_interp, ed_array, L_array)
    y_interp_2 = np.interp(x_interp, ed_array, k_array)
    within_nomograph = True if x_interp < ed_array.max() else False
    return [y_interp_1,y_interp_2,within_nomograph]

def nomomgraph_value_octagon_diagonal(x_val):
    return nomograph_value(x_val,eDivD_octagon_diagonal,L_octagon_diagonal,k_octagon_diagonal)

def show_octagon_nomograph(ed_array,L_array,k_array):
    
    fig, plt1 = plt.subplots()
    # generate evenly spaced values between the minimum and maximum x values
    x_interp = np.linspace(ed_array.min(), ed_array.max(), 100)

    # interp() to interpolate y values
    y_interp_1 = np.interp(x_interp, ed_array, L_array)
    y_interp_2 = np.interp(x_interp, ed_array, k_array)

    color_1 = 'tab:blue'
    color_2 = 'tab:green'
    # plot the original data points and the interpolated values
    plt1.set_xlabel("e/D")
    plt1.set_ylabel("L")
    plt1.plot(ed_array, L_array, 'bo')
    plt1.plot(x_interp, y_interp_1,'-r', color = color_1)

    plt2 = plt1.twinx()
    plt2.set_ylabel("k")
    plt2.plot(ed_array, k_array, 'bo')
    plt2.plot(x_interp, y_interp_2,'-r')

    fig.tight_layout() 
    plt.show()

#show_octagon_nomograph(eDivD_octagon_diagonal,L_octagon_diagonal,k_octagon_diagonal)

print(nomomgraph_value_octagon_diagonal(0.25))



#ARRAYS FOR LARGE ECCENTRICITIES PIP TABLE
    #x = np.array([0.3,0.305,0.31,0.315,0.32,0.325,0.33,0.335,0.34,0.345,0.35,0.355,0.36,0.365,0.37,0.375,0.38,0.385,0.39,0.395,0.4,0.405,0.41,0.415,0.42,0.425,0.43,0.435,0.44,0.445,0.45,0.455,0.46,0.465,0.47,0.475,0.48,0.485,0.49,0.495])
    #k = np.array([0.4935,0.5065,0.5195,0.5323,0.545,0.5577,0.5703,0.5828,0.5951,0.6074,0.6196,0.6317,0.6438,0.6557,0.6676,0.6794,0.6912,0.703,0.7149,0.7267,0.7387,0.7507,0.7628,0.7749,0.7872,0.7995,0.8119,0.8244,0.8369,0.8496,0.8625,0.8754,0.8885,0.9017,0.9151,0.9287,0.9424,0.9564,0.9707,0.9852]) 
    #L = np.array([4.503,4.656,4.819,4.991,5.174,5.369,5.576,5.797,6.032,6.284,6.553,6.842,7.152,7.485,7.844,8.233,8.654,9.113,9.615,10.167,10.775,11.45,12.203,13.046,13.998,15.08,16.32,17.754,19.432,21.421,23.812,26.742,30.411,35.138,41.452,50.304,63.601,85.785,130.192,263.487]) 
