import numpy as np

# Input data points (from Question 1)
data = np.array([[30, 0], [30, 10], [10, 10], [20, 20], [20, 30], [10, 30], [10, 40]])

# Calculate the mean of the data
mean = np.mean(data, axis=0)

# Center the data by subtracting the mean
centered_data = data - mean

# Calculate the covariance matrix
covariance_matrix = np.cov(centered_data, rowvar=False)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# Find the principal component (Question 1)
principal_component = eigenvectors[:, np.argmax(eigenvalues)]
print("Principal Component:", principal_component)

# Variance of the principal component (Question 2)
variance = eigenvalues[np.argmax(eigenvalues)]
print("Variance:", variance)

# Reduced value of point (10,20) (Question 3)
point = np.array([10, 20])
centered_point = point - mean
reduced_value = np.dot(centered_point, principal_component)
print("Reduced value of (10,20):", reduced_value)

# Reconstruction error for point (10,20) (Question 4)
reconstructed_point = reduced_value * principal_component + mean
error = np.linalg.norm(centered_point - (reduced_value * principal_component))
print("Reconstruction error for (10,20):", error)


# Candidate points for Question 5
candidate_points = np.array([[10, 40], [10, 10], [10, 30], [30, 0]])

min_error = float('inf')
point_with_min_error = None

for point in candidate_points:
    centered_point = point - mean
    reduced_value = np.dot(centered_point, principal_component)
    reconstructed_point = reduced_value * principal_component + mean
    error = np.linalg.norm(centered_point - (reduced_value * principal_component))

    if error < min_error:
        min_error = error
        point_with_min_error = point

print("Point with minimum reconstruction error:", point_with_min_error)
print("Minimum reconstruction error:", min_error)


# Question 6 (Conceptual, no code needed):  min_dist = 0.1 is likely the best answer.
