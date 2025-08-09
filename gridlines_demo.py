# gridlines_demo.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def plot_gridlines_demo(save_png: bool = False):
    """
    Plot two distinct curves on the same axes and showcase
    clearly differentiated major vs. minor gridlines.

    Parameters
    ----------
    save_png : bool, optional
        If True, saves an image named 'gridlines_demo.png' in the
        current directory.
    """
    x = np.linspace(-2 * np.pi, 2 * np.pi, 600)
    # Distinct from the assignment functions
    y1 = np.cos(1.2 * x) * np.exp(-0.1 * x**2)                # decaying cosine
    y2 = 0.4 * np.sin(0.8 * x + 1.0) + 0.2 * np.cos(2.2 * x)  # mixed harmonics

    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.patch.set_facecolor('#fafafa')

    ax.plot(x, y1, '--', color='#1565c0', linewidth=2, label='Decaying Cosine')
    ax.plot(x, y2, '-.o', markevery=30, markersize=4, color='#ef6c00', linewidth=1.75, label='Mixed Harmonics')

    # Axis limits
    ax.set_xlim(-2 * np.pi, 2 * np.pi)
    ax.set_ylim(-1.4, 1.4)

    # Major/minor locators
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=np.pi))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=np.pi / 4))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

    # Label major x ticks as multiples of π
    def pi_formatter(val, _pos):
        k = val / np.pi
        if np.isclose(k, 0):
            return '0'
        # Format integers nicely, else show as fraction with π
        if np.isclose(k, np.round(k)):
            k = int(np.round(k))
            return f"{k}π" if k != 1 and k != -1 else ("π" if k == 1 else "-π")
        return f"{k:.1f}π"

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

    # Grid styling (distinct colors/styles for major/minor)
    ax.grid(True, which='major', axis='both', color='#2e7d32', alpha=0.6, linestyle='-')
    ax.grid(True, which='minor', axis='both', color='#d32f2f', alpha=0.3, linestyle=':')

    # Tick style
    ax.tick_params(axis='both', which='major', direction='out', length=9, width=1.5, color='black', labelcolor='0.25')
    ax.tick_params(axis='both', which='minor', direction='inout', length=5, width=1)

    ax.set_title('Major/Minor Gridlines Demo', fontsize=14)
    ax.set_xlabel('Angle (radians)')
    ax.set_ylabel('Amplitude')
    ax.legend(loc='upper right', framealpha=0.85)

    plt.tight_layout()
    if save_png:
        plt.savefig('gridlines_demo.png', dpi=160, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    # Set save_png=True to auto-save an image for your README
    plot_gridlines_demo(save_png=False)
