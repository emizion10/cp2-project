#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# generate energy & spin vs distance plot from data


# define fit function, Morse potential


def morse(x, d, b):
    result = d*(1-np.exp(-b*x))**2
    return result


# function which extracts D_e F_max and r_max without fit for a defined region of the plot, use this when fit fails


def parameters(e_list, d_list):
    end = d_list[(e_list.index(max(e_list)))]
    e_list = [e_list[i] for i in range(len(e_list)) if d_list[i] <= end]
    d_list = [d_list[i] for i in range(len(d_list)) if d_list[i] <= end]
    dissociation = e_list[-1]
    diff_quot = [(e_list[i+1]-e_list[i])/(d_list[i+1]-d_list[i]) for i in range(len(e_list)-1)]
    distance = d_list[diff_quot.index(max(diff_quot))]
    force = (dissociation * distance / 2) * 60.22 ** (-1)
    return [dissociation, distance, force]


# function which makes the plot


def make_plot(filename, cleavage_type, fit):
    with open(filename, 'r') as file:                                           # read energies and displacements
        for line_number, line in enumerate(file):
            if line_number == 0:
                line = line.split()
                energies = line
            elif line_number == 1:
                line = line.split()
                bond_length = line
    file.close()
    # if cleavage_type == 'hom':
    #     with open(filename_spin, 'r') as file:                                      # read spins and displacements
    #         for line_number, line in enumerate(file):
    #             if line_number == 0:
    #                 line = line.split()
    #                 spins = line
    #             elif line_number == 1:
    #                 line = line.split()
    #                 bond_length = line
    #     spins = [float(spins[i]) for i in range(len(spins))]

    # x and y values
    energies = [(float(i) - float(energies[0]))*2625 for i in energies]         # convert E in kj/mol
    # energies = np.array(energies)                                         # convert to np.array (nicer maths)
    bond_length = [float(bond_length[i]) for i in range(len(energies))]         # make sure x & y have same length

    # fit
    if fit == 'fit':
        popt, pcov = curve_fit(morse, bond_length, energies)                        # optimal fit parameters
        perr = np.sqrt(np.diag(pcov))                                               # errors of fit parameters

    # plot
    fig2, ax5 = plt.subplots(1, 1, figsize=(15, 7))
    ax5.plot(bond_length, energies, color='r', label='Energy')                                          # energy
    if fit == 'fit':
        ax5.plot(bond_length, morse(np.array(bond_length), popt[0], popt[1]), color='b', linestyle='-.',    # fit
                 label='Morse potential fit: $D_e = $'
                       + str(round(popt[0], 1)) + ' kJ/mol')
        ax5.fill_between(bond_length, morse(np.array(bond_length), popt[0] + perr[0], popt[1] + perr[1]),   # errors of fit
                         morse(np.array(bond_length), popt[0] - perr[0], popt[1] - perr[1]), alpha=0.2)
        ax5.axvline(np.log(2) / popt[1], color='k',  # point of max F
                    label='Point of maximum force: ' + str(round(np.log(2) / popt[1], 2))
                          + ' $\AA$, $F_{max} = $'
                          + str(round((popt[0] * popt[1] / 2) * 60.22 ** (-1), 2)) + ' nN')
        ax5.grid(color='k', linestyle='--', linewidth=1, alpha=0.2)  # grid
    else:
        values = parameters(energies, bond_length)
        ax5.axvline(values[1], color='k',  # point of max F
                    label='Point of maximum force: ' + str(round(values[1], 2))
                          + ' $\AA$, $F_{max} = $'
                          + str(round(values[2], 2)) + ' nN, $D_e = $' + str(round(values[0], 1)) + ' kJ/mol')
    ax5.set_xlabel(r'$r-r_0$ $[\AA]$')                                                                  # labels
    ax5.set_ylabel(r'$E-E_0$ [kJ/mol]')
    # if cleavage_type == 'hom':
    #     ax6 = ax5.twinx()                                                                               # 2nd y axis
    #     ax6.plot(bond_length, spins, color='g', label=r'$<S^2>$')                                       # spin
    #     ax6.set_ylabel(r'$<S^2>$ [$(\hbar/2)^2$]')                                                      # labels
    #     ax6.set_xlabel(r'$r-r_0$ $[\AA]$')
    #     ax6.legend(loc='center right')                                                                  # legend
    ax5.legend(loc='lower right')                                                                       # legend
    plt.tight_layout()                                                                                  # tight layout
    if cleavage_type == 'het':                                                                          # give filename
        plt.savefig(filename[:-4] + '_het_plot.png', bbox_inches='tight')
    elif cleavage_type == 'hom':
        plt.savefig(filename[:-4] + '_hom_plot.png', bbox_inches='tight')


if __name__ == '__main__':
    file = input('Filename energy?')
    # file_spin = input('Filename spin?')
    cleavage = input('Type of bond cleavage? (het, hom)')
    fit_true = input('Fit? (fit/empty)')
    make_plot(file, cleavage, fit_true)


