import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

plt.style.use('dark_background')

def simulate_ideal_lensing():
    size = 1000 
    extent = [-200, 200, -200, 200]
    x = np.linspace(extent[0], extent[1], size)
    y = np.linspace(extent[2], extent[3], size)
    x_grid, y_grid = np.meshgrid(x, y)

    s_x, s_y = 0, 0
    
    bulge = 1.0 * np.exp(-((x_grid - s_x)**2 + (y_grid - s_y)**2) / (2 * 5**2))
    envelope = 0.3 * np.exp(-((x_grid - s_x)**2 + (y_grid - s_y)**2) / (2 * 30**2))
    
    source_plane = bulge + envelope

    # The Ideal Single Lens (One Massive Galaxy Only)
    lenses = [
        {'pos': (0, 0), 'RE': 65}
    ]
    
    alpha_x = np.zeros((size, size))
    alpha_y = np.zeros((size, size))
    
    for lens in lenses:
        l_x, l_y = lens['pos']
        dx, dy = x_grid - l_x, y_grid - l_y
        r = np.sqrt(dx**2 + dy**2)
        r[r == 0] = 1e-9 
        
        alpha_x += lens['RE'] * (dx / r)
        alpha_y += lens['RE'] * (dy / r)

    # Ray-Tracing
    beta_x = x_grid - alpha_x
    beta_y = y_grid - alpha_y

    # Mapping coordinates
    coords = np.array([(beta_y - extent[2]) * (size / (extent[3] - extent[2])), 
                       (beta_x - extent[0]) * (size / (extent[1] - extent[0]))])
    lensed_image = map_coordinates(source_plane, coords, order=1)

    # Plotting Comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    
    # Source
    ax1.imshow(source_plane, extent=extent, cmap='magma', origin='lower')
    ax1.set_title("Spherical Galaxy", fontsize=15, pad=15)
    ax1.axis('off')

    # Image
    ax2.imshow(lensed_image, extent=extent, cmap='magma', origin='lower')
    ax2.set_title("Produced Ring (Spherical)", fontsize=15, pad=15)
    ax2.axis('off')

    plt.tight_layout()
    plt.show()

simulate_ideal_lensing()