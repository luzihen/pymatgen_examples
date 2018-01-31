#http://pymatgen.org/examples.html
from pymatgen.core import *
from pymatgen.io.vasp.sets import *
from pymatgen import Lattice, Structure, Molecule
from pymatgen.io.vasp.sets import MPRelaxSet

from pymatgen import MPRester, Composition, Element
from pymatgen.io.vasp import Vasprun
from pymatgen.phasediagram.maker import PhaseDiagram, CompoundPhaseDiagram
from pymatgen.phasediagram.analyzer import PDAnalyzer
from pymatgen.phasediagram.plotter import PDPlotter
from pymatgen.entries.computed_entries import ComputedEntry
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.util.plotting_utils import get_publication_quality_plot
from pymatgen.phasediagram.maker import *
import json
import re
import palettable
import matplotlib as mpl

def get_most_stable_entry(formula,all_entries):
    relevant_entries = [entry for entry in all_entries if entry.composition.reduced_formula == Composition(formula).reduced_formula]
    relevant_entries = sorted(relevant_entries, key=lambda e: e.energy_per_atom)
    return relevant_entries[0]

def get_comp_entries(formula,all_entries):
    relevant_entries = [entry for entry in all_entries if entry.composition.reduced_formula == Composition(formula).reduced_formula]
    return relevant_entries

def find_entry_index(formula,all_entries):
    entry_index = [all_entries.index(entry) for entry in all_entries if entry.composition.reduced_formula == Composition(formula).reduced_formula]
    return entry_index

#rester = MPRester('5TxDLF4Iwa7rGcAl') #Generate your own key from materials project..
#mp_entries = rester.get_entries_in_chemsys(["Li", "Fe", "O","S"])



structure = Structure.from_file("LMO.cif")
v = MPRelaxSet(structure)
v.write_input("MyInputFiles")

#or use the following to generate a list of input
# ciflist = ['1.cif', '2.cif', '3.cif']
# structures=[]
# for x in ciflist:
    # structures.append(Structure.from_file(x))

# batch_write_input(structures, vasp_input_set=MPRelaxSet, output_dir="vasp_inputs")

