# Project Name: Prob_Set_4
# Author: Khang Vo
# Date Created: 10/30/2021
# Date Last Modified: 11/03/2021
# Python Version: 3.9

import os
import time

import setup
import FTCS
import LAX
import Staggered_Leapfrog


def main():
    root = os.getcwd() + "/files"
    os.chdir(root)

    # Physical Parameters
    w = 80  # width of domain
    vel = -10  # velocity
    nx = 151  # number of nodes
    dx = w / (nx - 1)
    nt = 350  # number of timesteps
    dt = 1e-2  # timestep/s

    # Initial Gaussian Temperature Perturbation
    xc = 40
    sigma = 2
    ampl = 2

    # Problem Initialization
    setup.initialize(w, nx, dx, nt, dt, xc, sigma, ampl)

    # FTCS Method
    FTCS.solve(vel, xc, sigma, ampl)
    FTCS.plot()

    # LAX Method
    LAX.solve(vel, xc, sigma, ampl)
    LAX.plot()

    # Staggered Leapfrog Method
    Staggered_Leapfrog.solve(vel, xc, sigma, ampl)
    Staggered_Leapfrog.plot()


if __name__ == "__main__":
    # Timer Start
    time_start = time.perf_counter()

    main()

    # Timer End
    time_end = time.perf_counter()
    time_total = time_end - time_start
    print("Elapsed Time: " + str(time_total) + " seconds")
