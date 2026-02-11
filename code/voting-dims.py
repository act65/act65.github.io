import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set aesthetic style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

def plot_precise_political_cube():
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # --- 1. AXIS MAPPING (The Logic) ---
    # We map 0 to the "Left" trait and 1 to the "Right" trait.
    # This ensures the Mainstream Line goes from (0,0,0) to (1,1,1).
    
    # X: TAXES       | 0 = High (Redistribution) | 1 = Low (Market)
    # Y: IMMIGRATION | 0 = Open (Liberal)        | 1 = Restricted (National)
    # Z: WELFARE     | 0 = High (Universal)      | 1 = Low (Minimal)
    
    corners = np.array([[x, y, z] for x in [0,1] for y in [0,1] for z in [0,1]])
    
    # --- 2. DRAW THE FRAMEWORK ---
    # Draw the cube edges
    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            if np.linalg.norm(corners[i]-corners[j]) == 1.0:
                ax.plot([corners[i][0], corners[j][0]], 
                        [corners[i][1], corners[j][1]], 
                        [corners[i][2], corners[j][2]], 
                        color='gray', alpha=0.15, linewidth=1)

    # --- 3. DRAW THE 1D "MAIN" SPECTRUM ---
    # The diagonal line that forces voters to bundle these issues together
    ax.plot([0, 1], [0, 1], [0, 1], 
            color='purple', linestyle='--', linewidth=3, alpha=0.6, 
            label='The 1D Party Line\n(Lossy Compression)')

    # --- 4. PLOT THE 4 KEY ARCHETYPES ---
    
    # We will only label the 4 most relevant corners to keep it clean.
    # The other 4 corners will be smaller gray ghost nodes.
    
    # A. THE STANDARD LEFT (0, 0, 0)
    # High Tax, Open Imm, High Welfare
    ax.scatter(0, 0, 0, color='#E81B23', s=500, edgecolor='k', alpha=1.0, zorder=10)
    ax.text(-0.1, -0.1, -0.05, "THE LEFT\n(Standard Bundle)", 
            color='#E81B23', fontweight='bold', ha='right', fontsize=11)
    
    # B. THE STANDARD RIGHT (1, 1, 1)
    # Low Tax, Restricted Imm, Low Welfare
    ax.scatter(1, 1, 1, color='#003399', s=500, edgecolor='k', alpha=1.0, zorder=10)
    ax.text(1.1, 1.1, 1.05, "THE RIGHT\n(Standard Bundle)", 
            color='#003399', fontweight='bold', ha='left', fontsize=11)

    # C. THE LIBERTARIAN (1, 0, 1)
    # Low Tax (1), Open Imm (0), Low Welfare (1)
    # "Socially Liberal, Fiscally Conservative"
    lib_pt = np.array([1, 0, 1])
    ax.scatter(1, 0, 1, color='#F5A623', s=400, edgecolor='k', alpha=1.0, zorder=10)
    ax.text(1.1, 0, 1.05, "The Libertarian\n(Low Tax, Open Borders)", 
            color='black', fontweight='bold', ha='left', fontsize=9)
    
    # D. THE LEFT-NATIONALIST / POPULIST (0, 1, 0)
    # High Tax (0), Restricted Imm (1), High Welfare (0)
    # "Pro-Worker, Anti-Migration" (e.g. PiS, Wagenknecht, Old Labour)
    pop_pt = np.array([0, 1, 0])
    ax.scatter(0, 1, 0, color='#8B572A', s=400, edgecolor='k', alpha=1.0, zorder=10)
    ax.text(-0.1, 1, -0.05, "The Left-Nationalist\n(High Tax, Closed Borders)", 
            color='black', fontweight='bold', ha='right', fontsize=9)
    
    # --- 5. PLOT THE "GHOST" NODES (The other 4 combinations) ---
    # These represent valid voter profiles that are less common or harder to name,
    # but still prove the "Combinatorial Explosion" point.
    for point in corners:
        # If not one of the 4 above...
        if not (np.array_equal(point, [0,0,0]) or np.array_equal(point, [1,1,1]) or 
                np.array_equal(point, [1,0,1]) or np.array_equal(point, [0,1,0])):
            ax.scatter(point[0], point[1], point[2], color='lightgray', s=100, edgecolor='gray', alpha=0.5)

    # --- 6. VISUALIZE THE "ERROR" (DISENFRANCHISEMENT) ---
    # Draw a dotted line from the Orphan nodes to the Spectrum
    # Project point P onto line passing through A(0,0,0) and B(1,1,1)
    
    # For Libertarian (1,0,1): Average is 0.66. Closest point on line is (0.66, 0.66, 0.66)
    proj_lib = np.array([2/3, 2/3, 2/3])
    ax.plot([1, proj_lib[0]], [0, proj_lib[1]], [1, proj_lib[2]], 
            color='#F5A623', linestyle=':', linewidth=2)
    ax.text(0.8, 0.3, 0.8, "Geometric\nError", color='#F5A623', fontsize=8, ha='center')

    # For Populist (0,1,0): Average is 0.33. Closest point is (0.33, 0.33, 0.33)
    proj_pop = np.array([1/3, 1/3, 1/3])
    ax.plot([0, proj_pop[0]], [1, proj_pop[1]], [0, proj_pop[2]], 
            color='#8B572A', linestyle=':', linewidth=2)

    # --- 7. AXIS LABELS & TICKS ---
    ax.set_xlabel("\n\nTAXES", fontsize=10, fontweight='bold')
    ax.set_ylabel("\n\nIMMIGRATION", fontsize=10, fontweight='bold')
    ax.set_zlabel("\n\nWELFARE", fontsize=10, fontweight='bold')
    
    # Custom Ticks: 0 = Left Trait, 1 = Right Trait
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['High\n(Redistrib.)', 'Low\n(Market)'], fontsize=9)
    
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Open\n(Liberal)', 'Restricted\n(National)'], fontsize=9, ha='left')
    
    ax.set_zticks([0, 1])
    ax.set_zticklabels(['High\n(Universal)', 'Low\n(Minimal)'], fontsize=9)

    # --- 8. CAMERA ANGLE ---
    # Elev=20: Looking slightly down
    # Azim=-60: Standard isometric view usually works best to see the separation
    # We want (0,0,0) bottom-front-left and (1,1,1) top-back-right
    ax.view_init(elev=30, azim=-70)
    
    ax.set_title("Combinatorial Explosion: 3 Binary Issues = 8 Political Identities", fontsize=15, fontweight='bold', pad=20)
    ax.legend(loc='upper left', frameon=True, fancybox=True)

    plt.tight_layout()
    plt.savefig('fig3_political_cube_precise.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    plot_precise_political_cube()