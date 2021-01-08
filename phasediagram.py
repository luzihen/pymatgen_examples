#http://pymatgen.org/examples.html
from pymatgen.core import *
from pymatgen.io.vasp.sets import *
from pymatgen import Lattice, Structure, Molecule
from pymatgen.io.vasp.sets import MPRelaxSet

from pymatgen import MPRester, Composition, Element
from pymatgen.io.vasp import Vasprun
from pymatgen.analysis.phase_diagram import CompoundPhaseDiagram, GrandPotentialPhaseDiagram, PDPlotter, PhaseDiagram
import palettable
import matplotlib as mpl


rester = MPRester('5TxDLF4Iwa7rGcAl') #Generate your own key from materials project..
mp_entries = rester.get_entries_in_chemsys(["Li", "Fe", "O","S"])



pd = PhaseDiagram(mp_entries)
plotter = PDPlotter(pd)
plotter.show()
