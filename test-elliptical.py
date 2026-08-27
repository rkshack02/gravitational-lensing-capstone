import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

plt.style.use('dark_background')

def simulate_elliptical_source():
    size = 1000 
    extent = [-200, 200, -200, 200]
    x = np.linspace(extent[0], extent[1], size)
    y = np.linspace(extent[2], extent[3], size)
    x_grid, y_grid = np.meshgrid(x, y)

    # Ellipticity Parameters
    q = 0.5
    s_x, s_y = 0, 0
    
    sigma_bulge = 6
    bulge = 1.0 * np.exp(-( ((x_grid - s_x)**2 / (2 * sigma_bulge**2)) + 
                            ((y_grid - s_y)**2 / (2 * (sigma_bulge * q)**2)) ))
    
    sigma_env = 35
    envelope = 0.3 * np.exp(-( ((x_grid - s_x)**2 / (2 * sigma_env**2)) + 
                               ((y_grid - s_y)**2 / (2 * (sigma_env * q)**2)) ))
    
    source_plane = bulge + envelope

    # The Lens (Elliptical Source Galaxy)
    re = 70
    r = np.sqrt(x_grid**2 + y_grid**2)
    r[r == 0] = 1e-9 
    
    alpha_x = re * (x_grid / r)
    alpha_y = re * (y_grid / r)

    # Ray-Tracing
    beta_x = x_grid - alpha_x
    beta_y = y_grid - alpha_y

    coords = np.array([(beta_y - extent[2]) * (size / (extent[3] - extent[2])), 
                       (beta_x - extent[0]) * (size / (extent[1] - extent[0]))])
    lensed_image = map_coordinates(source_plane, coords, order=1)

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    
    # Source
    ax1.imshow(source_plane, extent=extent, cmap='magma', origin='lower')
    ax1.set_title(f"Elliptical Galaxy (q={q})", fontsize=15)
    ax1.axis('off')

    # Image
    ax2.imshow(lensed_image, extent=extent, cmap='magma', origin='lower')
    ax2.set_title("Produced Ring ( Elliptical Arcs, Varying Brightness)", fontsize=15)
    ax2.axis('off')

    plt.tight_layout()
    plt.show()

simulate_elliptical_source()