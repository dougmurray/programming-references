import numpy as np
import matplotlib.pyplot as plt

def elemental_plotter(xvalues, yvalues, plot_type, plot_label, title, xlabel, ylabel, grid=None, xscale=None, yscale=None):
    """ Plots with all my favorite elements.
    Example usage:
    noise_plot, plot_axs = elemental_plotter(freqs, psd, 'loglog', 'output noise', 'Title', 'Freq (Hz)', 'Voltage Noise ($\mu V/\sqrt{Hz}$)', grid=True, yscale=1e-6)

    Then to add or change plot properties by adding to plot_axs:
    plot_axs.loglog(freqs2, psd2, label='another plot')
    plot_axs.set_ylim(10e-9, 100e-6)
    plot_axs.axes.axhline(y=200e-9, label='200 nV/sqrt(Hz)')
    plot.axs.legend(loc='upper left')

    And save plot fig by using the savefig method of noise_plot:
    noise_plot.savefig('figures/noise-plots.jpg', dpi=300)

    Args:
        xvalues: can be an array
        yvalues: can be an array
        plot_type: type of plot, ie 'loglog', 'plot', etc.
        plot_label: name of plotted elements
        title: name of graph
        xlabel: name of xvalues
        ylabel: name of yvalues
        grid: flag to show x/y grid or not
        xscale: optional, if xvalues need to be scaled on plot
        yscale: optional, if yvalues need to be scaled on plot

    Returns:
        fig: matplotlib figure object
        ax: matplotlib axes, use this to add to plot
    """
    fig, ax = plt.subplots()

    if plot_type == 'plot':
        ax.plot(xvalues, yvalues, linewidth=0.5, label=plot_label)
    elif plot_type == 'loglog':
        ax.loglog(xvalues, yvalues, linewidth=0.5, label=plot_label)

    if xscale:
        # Change scale of plot
        ticks_x = plt.FuncFormatter(lambda x, pos: '{0:g}'.format(x/xscale))
        ax.xaxis.set_major_formatter(ticks_x)
 
    if yscale:
        ticks_y = plt.FuncFormatter(lambda x, pos: '{0:g}'.format(x/yscale))
        ax.yaxis.set_major_formatter(ticks_y)

    if grid:
            ax.grid(which='both', linewidth=0.5)
    else:
            pass

    ax.autoscale(tight=True)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc='lower right')

    return fig, ax
