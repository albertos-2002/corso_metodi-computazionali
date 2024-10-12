import matplotlib.pyplot as plt

def make_fine(axObj):
    
    #disegno degli assi
    axObj.axhline( 0, color='grey', linestyle=(0, (1, 3)) ); # Horizontal axis
    axObj.axvline( 0, color='grey', linestyle=(0, (1, 3)) );  # Vertical axis
    
    axObj.legend()
    axObj.grid()
    
    return axObj


def set_style(fontSize):
    
    plt.rcParams['axes.titlesize'] = fontSize+2;  # Set title size
    plt.rcParams['axes.labelsize'] = fontSize;    # Set label size
    plt.tight_layout()
    


