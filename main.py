import sys
from input_proc import proc_inputfile
from materials import mat_dict
from initialize import initialize
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print('Usage: python main.py [opts] inputfile')
        sys.exit()
    inputfile = args[-1]
    sim = proc_inputfile(inputfile)
    sim.printInfo()
    mat = mat_dict[sim.material]
    mat.printInfo()
    if not(os.path.exists(sim.init_dir)):
        os.mkdir(sim.init_dir)
    initialize(mat, sim)
    print('done.')

