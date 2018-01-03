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


vasprun = Vasprun("vasprun.xml")
entry = vasprun.get_computed_entry(inc_structure=True)



compatibility = MaterialsProjectCompatibility()
entry = compatibility.process_entry(entry)
#entries = compatibility.process_entries([entry] + mp_entries)