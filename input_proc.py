class simulation:
    def __init__(self, material, res, rad, e_model, ph_model, init_dir):
        self.material = material
        self.res = res
        self.rad = rad
        self.e_model = e_model
        self.ph_model = ph_model
        self.init_dir = init_dir
    def printInfo(self):
        print("#### SIMULATION INFO ####")
        print('Material: ',self.material)
        print('resolution: ', self.res)
        print('truncation radius (2pi/a): ', self.rad)
        print('e model: ', self.e_model)
        print('ph model: ', self.ph_model)
        print('init dir: ', self.init_dir)
        print("#########################")
        return

def proc_inputfile(inputfile):
    with open(inputfile) as f:
        for line in f:
            exec(str(line),locals())
    sim = simulation(material=locals()['material'],\
                     res=locals()['res'],\
                     rad=locals()['rad'],\
                     e_model=locals()['e_model'],\
                     ph_model=locals()['ph_model'],\
                     init_dir=locals()['init_dir'])
    return sim