import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

plt.style.use('dark_background')

def simulate_capstone_comparison():
    size = 1000 
    extent = [-200, 200, -200, 200]
    x = np.linspace(extent[0], extent[1], size)
    y = np.linspace(extent[2], extent[3], size)
    x_grid, y_grid = np.meshgrid(x, y)

    # 2. The "Research" Source (Bulge + Envelope)
    s_x, s_y = 0, 0 # Slight offset from center for better arcs
    
    # Central Bulge: Tight and bright
    bulge = 1.0 * np.exp(-((x_grid - s_x)**2 + (y_grid - s_y)**2) / (2 * 5**2))
    # Extended Envelope: Wide and diffuse
    envelope = 0.3 * np.exp(-((x_grid - s_x)**2 + (y_grid - s_y)**2) / (2 * 30**2))
    
    source_plane = bulge + envelope

    # 3. The "Clumped" Dark Matter Field (Lenses)
    lenses = [
        {'pos': (0, 0), 'RE': 65},      # Main massive galaxy
        {'pos': (90, 80), 'RE': 25},    # Clump A (Satellite)
        {'pos': (-100, -50), 'RE': 20}, # Clump B (Sub-halo)
        {'pos': (30, -120), 'RE': 15}   # Clump C (Sub-halo)
    ]
    
    alpha_x = np.zeros((size, size))
    alpha_y = np.zeros((size, size))
    
    for lens in lenses:
        l_x, l_y = lens['pos']
        dx, dy = x_grid - l_x, y_grid - l_y
        r = np.sqrt(dx**2 + dy**2)
        r[r == 0] = 1e-9 
        
        # Deflection vector calculation
        alpha_x += lens['RE'] * (dx / r)
        alpha_y += lens['RE'] * (dy / r)

    # 4. Ray-Tracing (The Lens Equation)
    beta_x = x_grid - alpha_x
    beta_y = y_grid - alpha_y

    # Map the coordinates from source space to image space
    coords = np.array([(beta_y - extent[2]) * (size / (extent[3] - extent[2])), 
                       (beta_x - extent[0]) * (size / (extent[1] - extent[0]))])
    lensed_image = map_coordinates(source_plane, coords, order=1)

    # 5. Side-by-Side Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    
    # Left: The Source (Unlensed)
    ax1.imshow(source_plane, extent=extent, cmap='magma', origin='lower')
    ax1.set_title("Galaxy with Substructure and Dark Matter Clumps", fontsize=15, pad=15)
    ax1.axis('off')

    # Right: The Lensed Image (Reality)
    ax2.imshow(lensed_image, extent=extent, cmap='magma', origin='lower')
    ax2.set_title("Produced Ring (Brightness Anomalies, Bent Arcs, Asymmetries)", fontsize=15, pad=15)
    ax2.axis('off')
    
    # Overlay indicators for where the invisible lenses are on the right plot
    for lens in lenses:
        ax2.plot(lens['pos'][0], lens['pos'][1], 'w+', alpha=0.15, markersize=8)

    plt.tight_layout()
    plt.show()

simulate_capstone_comparison()