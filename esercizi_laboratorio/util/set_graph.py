import matplotlib.pyplot as plt


def make_fine(axObj):
    
    #disegno degli assi
    axObj.axhline( 0, color='grey', linestyle=(0, (1, 3)) );  # Horizontal axis
    axObj.axvline( 0, color='grey', linestyle=(0, (1, 3)) );  # Vertical axis
    
    axObj.legend()
    axObj.grid()
    
    return axObj


def set_style(fontSize=10, markerSize=6):
    
    plt.rcParams['axes.titlesize']  = fontSize;      # Set title size
    plt.rcParams['axes.labelsize']  = fontSize+7;    # Set label size
    plt.rcParams['legend.fontsize'] = fontSize-4
    
    plt.rcParams['lines.markersize'] = markerSize;  # Reset to the default value
    
    
    plt.tight_layout()
    
    
    # Enable LaTeX rendering
    plt.rcParams['text.usetex'] = False
    
    return


