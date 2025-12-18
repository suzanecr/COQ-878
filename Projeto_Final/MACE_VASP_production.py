import os
import time

t1 = time.time()

os.environ['VASP_PP_PATH'] = '/home/public/Programs/vasp.6.5.1/pp'
os.environ['ASE_VASP_COMMAND'] = 'mpirun -np 2 vasp_std'                 
os.environ['NO_STOP_MESSAGE'] = '1' 

from ase.calculators.vasp import Vasp

import numpy as np
import matplotlib.pyplot as plt

from ase import Atoms, Atom
from ase.build import molecule, surface, bulk, add_adsorbate
from ase.io import write, read
from ase.visualize.plot import plot_atoms
from ase.constraints import FixAtoms
from ase.spacegroup import crystal
from ase.build import make_supercell


os.makedirs("MACE", exist_ok=True)
os.makedirs("MACE/EtOH_HAP", exist_ok=True)

# Criando a calculadora do VASP com ibrion=-1

vasp_calc = Vasp(
    directory='MACE/EtOH_HAP',
    xc='PBE',
    encut=400,
    ivdw=12, vdw_radius = 10, vdw_cnradius = 10,         
    ismear=0, sigma=0.1,
    ediff=1e-4,       
    isym=0,
    ibrion=-1, nelm=100,                           
    lreal = 'Auto', lwave=False, lcharg=False, lvtot=False
)

from tqdm import tqdm
print("Evaluating MACE configurations with VASP")
traj = read('frame_900_product.xyz', ':')

for at in tqdm(traj[::20]): 
    at.calc = vasp_calc
    at.info['energy_vasp'] = at.get_potential_energy()
    at.arrays['forces_vasp'] = at.get_forces()
    at.calc = None  


write('MACE/HAP_EtOH_100passos.xyz', traj[::20]) 
