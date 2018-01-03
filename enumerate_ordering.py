from pymatgen import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.transformations.advanced_transformations import EnumerateStructureTransformation
from pymatgen.io.vasp.sets import batch_write_input, MPRelaxSet
from pymatgen.io.vasp.sets import batch_write_input, MPRelaxSet

structure = Structure.from_file("1.cif")

structure[0]={"Fe2+":1/3,"Li+":2/3}
structure[1]={"Fe2+":1/3,"Li+":2/3}
structure[2]={"Fe2+":1/3,"Li+":2/3}
structure[3]={"S2-":1}
structure[4]={"O2-":1}
structure

structure.make_supercell([2,2,2])
structure


enum = EnumerateStructureTransformation()
enumerated = enum.apply_transformation(structure, return_ranked_list=100)  # return no more than 100 structures
structures = [d["structure"] for d in enumerated]  
print("%d structures returned." % len(structures))

from pymatgen.analysis.energy_models import EwaldElectrostaticModel
ed=EwaldElectrostaticModel()
#ed.get_energy(structures[1])

structures20=structures[:20]
batch_write_input(elect_stru, vasp_input_set=MPRelaxSet)

# elect_stru=structures20=structures[::10]

# for st in elect_stru:
    # print(ed.get_energy(st))


# from pymatgen.transformations.standard_transformations import PartialRemoveSpecieTransformation       
# vac_list=[]

# for ii in range (1,11):
    # strut=structures[ii]
    # temp=[]
    # for noLi in range(0,17):
        # Pd_mv = PartialRemoveSpecieTransformation("Li+", noLi/16, algo=0)
        # temp.append(Pd_mv.apply_transformation(strut, return_ranked_list=5))
        # print(noLi)
        
    # vac_list.append(temp)


# defect_strs=[]    
# iii=1    
# for start in vac_list:
     # temp=[]
     
     # for no_Li in start:
         # for count in no_Li:
             # temp.append(count["structure"])
         
    
     # defect_strs.append(temp)
     # iii=iii+1
     # batch_write_input(temp, vasp_input_set=MPRelaxSet,output_dir="start"+str(iii))
     # print(iii)

     
     
     
     
     
# #
# for x in range(0,24):
    # structure[x]={"Fe2+":1/3,"Li+":15/24}
