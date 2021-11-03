# Module Name: Staggered_Leapfrog
# Author: Khang Vo
# Date Created: 11/02/2021
# Date Last Modified: 11/03/2021
# Python Version: 3.9

import os
import glob

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def solve(vel, xc, sigma, ampl):

    file_list = sorted(glob.glob("initial*.txt"))

    for file in file_list:
        t = pd.read_csv(file, sep="\t", index_col=0, header=0)
        t.index = t.index.astype(float)
        t.columns = t.columns.astype(float)
        t.iloc[1, :] = t.iloc[0, :]
        nt = len(t.index)
        nx = len(t.columns)

        # velocity profile
        vx = vel * np.ones(len(t))
        # constant used in discretization
        dt = t.index[1] - t.index[0]
        dx = t.columns[1] - t.columns[0]

        print("alpha = " + str(np.abs(vx[0]) * (dt / dx)))

        tanl = pd.DataFrame(index=t.index, columns=t.columns)

        for n in range(1, nt - 1):
            for i in range(1, nx - 1):
                t.iloc[n + 1, i] = (-vx[i] * (t.iloc[n, i + 1] - t.iloc[n, i - 1]) / (2 * dx)) * (2 * dt) + \
                                   t.iloc[n - 1, i]

            time = n * dt
            # analytical solution at this time
            xn = xc + vel * time
            tanl.iloc[n, :] = ampl * np.exp(-1 * ((t.columns - xn) ** 2 / sigma ** 2))

        t.to_csv("Staggered_Leapfrog" + file[10:-4] + ".txt", sep="\t")
        tanl.to_csv("T_Analytical.txt", sep="\t")


def plot():
    file_list = sorted(glob.glob("Staggered_Leapfrog*.txt"))
    t = dict()

    for file in file_list:
        t[file] = pd.read_csv(file, sep="\t", index_col=0, header=0)
        t[file].index = t[file].index.astype(float)
        t[file].columns = t[file].columns.astype(float)

    tanl = pd.read_csv("T_Analytical.txt", sep="\t", index_col=0, header=0)
    tanl.index = tanl.index.astype(float)
    tanl.columns = tanl.columns.astype(float)

    keys_list = t.keys()
    for count in range(0, len(tanl.index)):
        if count | 0 and count % 3 == 0:
            plt.gca().cla()  # clear any previous plot axes
            plt.plot(tanl.columns, tanl.iloc[count, :], color="gray", label="analytical", linewidth=1.5)
            for keys in keys_list:
                plt.plot(t[keys].columns, t[keys].iloc[count, :], label="numerical (" + keys[18:-4] + ")",
                         linewidth=1.5)
            plt.title("Staggered Leapfrog")
            plt.ylabel("T")
            plt.xlabel("x")
            plt.legend()
            plt.draw()
            plt.pause(0.1)
            plt.savefig("Staggered_Leapfrog.png")


# if __name__ == "__main__":
#     root = os.getcwd() + "/files"
#     os.chdir(root)
