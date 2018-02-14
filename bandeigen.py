#bandata[kpoint][band]['energy'/'occupation'/'kposition']

import os.path
if os.path.exists('OUTCAR'):
    f = open('OUTCAR',"r") #opens file with name of "test.txt"
    data = f.readlines()
    f.close()
    #print('OUTCAR is loaded')
else:
    print('OUTCAR do not exist')


bandata_up=[]
bandata_down=[]

for n, line in enumerate(data):
    if 'ISPIN' in line:
        ispin = int(line.split()[-4])
    
    if 'E-fermi' in line:
        nonspinline=n
    if 'spin component 1' in line:
        spinupline=n
    if 'spin component 2' in line:
        spindownline=n
    if 'NBANDS' in line:
        nkpoints = int(line.split()[3]) #number of kpoints
        nbands = int(line.split()[-1])  #number of bands
        #print('nband')

        
        
if ispin == 1: #non-spin
    print('non-spin-polarized VASP OUTCAR, access data from bandata')
    bandata=[]
    for ikpoint in range(1,nkpoints+1):
        kpoint_position_temp=data[(ikpoint-1)*(3+nbands)+nonspinline+3].split()
        kpoint_position=[kpoint_position_temp[-3],kpoint_position_temp[-2],kpoint_position_temp[-1]]
        bandkpoints_tmp=[]
        for iband in range(1,nbands+1):
            data_tmp=data[(ikpoint-1)*(3+nbands)+iband+nonspinline+4].split() #core, check the math....
            occupancy_tmp=float(data_tmp[-1])
            energy_tmp=float(data_tmp[-2])
            bandkpoints_tmp.append({'energy':energy_tmp,'occupation':occupancy_tmp,'kposition':kpoint_position})
                    
        bandata.append(bandkpoints_tmp)
            
            

  
if ispin == 2: #spin
    bandata_up=[]
    print('non-spin-polarized VASP OUTCAR, access data from bandata_up and bandata_down')
    for ikpoint in range(1,nkpoints+1):
        kpoint_position_temp=data[(ikpoint-1)*(3+nbands)+spinupline+2].split()
        kpoint_position=[kpoint_position_temp[-3],kpoint_position_temp[-2],kpoint_position_temp[-1]]
        bandkpoints_tmp=[]
        for iband in range(1,nbands+1):
            data_tmp=data[(ikpoint-1)*(3+nbands)+iband+spinupline+3].split() #core, check the math....
            occupancy_tmp=float(data_tmp[-1])
            energy_tmp=float(data_tmp[-2])
            bandkpoints_tmp.append({'energy':energy_tmp,'occupation':occupancy_tmp,0:energy_tmp,1:occupancy_tmp,'kposition':kpoint_position})
                    
        bandata_up.append(bandkpoints_tmp)
    bandata_up=[]
    
    bandata_down=[]
    for ikpoint in range(1,nkpoints+1):
        kpoint_position_temp=data[(ikpoint-1)*(3+nbands)+spindownline+2].split()
        kpoint_position=[kpoint_position_temp[-3],kpoint_position_temp[-2],kpoint_position_temp[-1]]
        bandkpoints_tmp=[]
        for iband in range(1,nbands+1):
            data_tmp=data[(ikpoint-1)*(3+nbands)+iband+spindownline+3].split() #core, check the math....
            occupancy_tmp=float(data_tmp[-1])
            energy_tmp=float(data_tmp[-2])
            bandkpoints_tmp.append({'energy':energy_tmp,'occupation':occupancy_tmp,0:energy_tmp,1:occupancy_tmp,'kposition':kpoint_position})
                    
        bandata_down.append(bandkpoints_tmp)        


print('access band info with the following syntex')
