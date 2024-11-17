import numpy as np  
 

def generate_random_points_in_cartesian(x0, y0, x1, y1, num_points, z):
    points = []
    for _ in range(num_points):
        # Random angle between 0 and 2*pi 
        
        # Convert polar coordinates to Cartesian coordinates
        x = np.random.uniform(x0, x1)
        y = np.random.uniform(y0, y1)
        
        points.append((x, y, z))
    
    return points

# Example usage
d = 0.00325
x0 = -0.0375 + d/2
x1 =  0.0375 - d/2
y0 = -0.115 + d/2
y1 =  0.115 - d/2

num_points = 125  # Number of points to generate
nz = 95
zs = np.linspace(d/2,0.46,nz)

filename = 'random_points.txt'
with open(filename, 'w') as file: 
    for z in zs:
        points = generate_random_points_in_cartesian(x0, y0, x1, y1, num_points, z)
        for point in points:
            file.write(f'({point[0]} {point[1]} {point[2]})\n')


    






'''
# Extract x and y coordinates from points
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Plot the circle boundary
circle = plt.Circle((0, 0), r, color='blue', fill=False, linestyle='--')

# Create a plot
fig, ax = plt.subplots()

# Plot the random points
ax.scatter(x_coords, y_coords, color='red', marker='o')

# Add the circle to the plot
ax.add_artist(circle)

# Set equal scaling so the circle isn't distorted
ax.set_aspect('equal', 'box')

# Set axis limits
ax.set_xlim([-r, r])
ax.set_ylim([-r, r])

# Display the plot
plt.title(f'Random Points within a Circle of Radius {r}')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
'''
