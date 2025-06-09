import numpy as np

# Input data points
data = np.array([[30, 0], [30, 10], [10, 10], [20, 20], [20, 30], [10, 30], [10, 40]])

# Calculate the mean of the data
mean = np.mean(data, axis=0)

# Center the data by subtracting the mean
centered_data = data - mean

# Calculate the covariance matrix
covariance_matrix = np.cov(centered_data, rowvar=False)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# Find the eigenvector corresponding to the largest eigenvalue
principal_component = eigenvectors[:, np.argmax(eigenvalues)]

print("Principal Component:", principal_component)

# Find the eigenvector corresponding to the largest eigenvalue
principal_component = eigenvectors[:, np.argmax(eigenvalues)]
variance = eigenvalues[np.argmax(eigenvalues)]

print("Principal Component:", principal_component)
print("Variance:", variance)
point = np.array([10, 20])
centered_point = point - mean
reduced_value = np.dot(centered_point, principal_component)

print("Reduced value of (10,20):", reduced_value)

reconstructed_point = reduced_value * principal_component + mean
error = np.linalg.norm(centered_point - (reduced_value * principal_component))

print("Reconstruction error for (10,20):", error)