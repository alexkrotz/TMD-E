from grid import Monkhorst_Pack, k_to_q
import numpy as np
def initialize(mat, sim):
    k = Monkhorst_Pack(sim.res)
    print('# of points in full grid: ', len(k))
    K_points_order = np.array([1, 3, 5, 0, 2, 4])
    K_points = 4.0 * np.pi / 3.0 * np.column_stack(
        (np.cos(K_points_order / 3. * np.pi), np.sin(K_points_order / 3. * np.pi)))
    K_points_tau = np.power(-1, K_points_order)
    found = 0
    for K in K_points:
        found += np.sum(np.all(np.round(k, 6) == np.round(K, 6), axis=1))
    if found == 0:
        print('Grid does not contain K points')
        print('Stopping calculation')
        exit()
    else:
        print('Grid has K points')
    np.savetxt(sim.init_dir + '/k.csv', k, delimiter=',')
    if sim.e_model == 'tb':
        q, tau = k_to_q(k, K_points, K_points_tau)
        from twobandmodel import two_band, two_band_params
        params = two_band_params(sim.material)

    return
