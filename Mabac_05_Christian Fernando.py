import numpy as np

# Data baru
alternatives = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
criteria_weights = np.array([0.25, 0.35, 0.15, 0.25])
decision_matrix = np.array([
    [20, 60, 40, 80],
    [30, 50, 70, 90],
    [60, 30, 50, 60],
    [70, 40, 20, 70],
    [40, 90, 60, 50],
    [50, 70, 30, 40],
    [30, 80, 50, 60],
    [20, 60, 40, 20],
    [60, 70, 20, 80],
    [50, 50, 30, 90]
])

# ormalisasi matriks
def normalize_matrix(matrix):
    norm_matrix = np.zeros(matrix.shape)
    for j in range(matrix.shape[1]):
        column = matrix[:, j]
        norm_matrix[:, j] = (column - column.min()) / (column.max() - column.min())
    return norm_matrix

# untuk menghitung matriks tertimbang
def weighted_matrix(matrix, weights):
    return matrix * weights

# Menghitung matriks area perkiraan batas
def boundary_matrix(matrix, weights):
    return np.prod(matrix * weights, axis=1) ** (1 / len(weights))

# Menghitung matriks jarak alternatif dari daerah perkiraan perbatasan
def distance_matrix(matrix, boundary):
    return matrix - boundary[:, np.newaxis]

# Menghitung nilai preferensi alternatif
def preference_score(matrix, distance):
    return np.sum(distance, axis=1)

# Menghitung perankingan alternatif
def ranking(alternatives, scores):
    return np.argsort(scores)[::-1]

# Menghitung nilai preferensi alternatif
norm_matrix = normalize_matrix(decision_matrix)
weighted_matrix = weighted_matrix(norm_matrix, criteria_weights)
boundary = boundary_matrix(weighted_matrix, criteria_weights)
distance = distance_matrix(weighted_matrix, boundary)
scores = preference_score(distance, criteria_weights)
rank_indices = ranking(alternatives, scores)

# Menampilkan hasil
print("Nilai Preferensi untuk setiap alternatif:")
for alt, score in zip(alternatives, scores):
    print(f"{alt}: {score:.4f}")

print("\nRanking alternatif:")
for rank, idx in enumerate(rank_indices, start=1):
    print(f"{rank}. {alternatives[idx]}")

print(f"\nAlternatif terbaik adalah: {alternatives[rank_indices[0]]}")
