import numpy as np




def Monkhorst_Pack(res):
    lattice_vec_1 = 2 * np.pi / np.sqrt(3.0) * np.array([np.sqrt(3.0), -1.0])
    lattice_vec_2 = 4 * np.pi / np.sqrt(3.0) * np.array([0.0, 1.0])
    grid = []
    for res_id_1 in range(res):
        p = res_id_1 + 1
        up = (2 * p - res - 1) / (2.0 * res)
        for res_id_2 in range(res):
            r = res_id_2 + 1
            ur = (2 * r - res - 1) / (2.0 * res)
            grid.append(up * lattice_vec_1 + ur * lattice_vec_2)
    return np.array(grid)


def k_to_q(k, K_points, K_points_tau):
    mask = np.zeros(k.shape[0], dtype=int)
    for k_id in range(k.shape[0]):
        mask[k_id] = np.argmin(
            np.around(np.apply_along_axis(np.linalg.norm, 1, k[k_id] - K_points), decimals=4))
    return k - K_points[mask], K_points_tau[mask]
