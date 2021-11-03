# Module Name: setup
# Author: Khang Vo
# Date Created: 10/30/2021
# Date Last Modified: 11/01/2021
# Python Version: 3.9

import os

import pandas as pd
import numpy as np


def initialize(w, nx, dx, nt, dt, xc, sigma, ampl):

    file_list = os.listdir()
    for file in file_list:
        os.remove(file)

    if type(dt) == int or type(dt) == float:
        dt = [dt]

    for index in range(len(dt)):
        # grid array
        x_nodes = np.arange(0, w + dx, dx)
        t_nodes = np.arange(0, (nt * dt[index] + dt[index]), dt[index])
        t = pd.DataFrame(index=t_nodes, columns=x_nodes)
        t.iloc[0, :] = ampl * np.exp(-1.0 * ((x_nodes - xc)**2 / sigma**2))
        t.iloc[:, 0] = t.iloc[0, 0]
        t.iloc[:, -1] = t.iloc[0, -1]
        t.fillna(0)

        t.to_csv("initial_T_" + str(dt[index]) + ".txt", sep="\t")


# if __name__ == "__main__":
#     root = os.getcwd() + "/files"
#     os.chdir(root)
