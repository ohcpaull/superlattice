'''
 Magnetic fitting for 15 superlattice measure on Platypus in 0T field
Program: Refl1D Program

Version 0.1
Author Jackson Wong

Structure values are taken from 0T fitting.
Canting of the magnetic layers are done in this program.
Canting is defined with reference to LNO layer.
ThetaM 270 is set for LNO and LSMO is canted above and below it. 
Based on original paper canting between LSMO layers can go as high as 110 degrees.
Magnetism twist needs to be added to LNO layer, LSMO is presumed uniform.
'''

from refl1d.names import *
from refl1d.probe import *


LNO = SLD(name = 'LaNiO3', rho = 6.359, irho=0)
LSMO = SLD(name = 'LaSrMnO3', rho = 3.7, irho=0)
STO = SLD (name = 'SrTiO3', rho = 3.54, irho=0)

#Model

Fifthteen = (STO (0, 1.5) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | LSMO (35.9, 1, magnetism=Magnetism(rhoM=1, thetaM=270)) | LNO(11.5, 1) 
                | air)


# Define the fittable parameters as usual, including the magnetism attributes.

x = 1
while x < 31:
    #Choose fitting parameters

    Fifthteen[x].thickness.pmp(12)
    Fifthteen[x].interface.range(0.5,1.5)
    #Fifthteen[x].magnetism.rhoM.pmp(50)
    #Fifthteen[x].magnetism.thetaM.range(150, 390)
    x += 1


x = 1
while x < 31:
    #LSMO layer only
    Fifthteen[x].magnetism.rhoM.pmp(50)
    Fifthteen[x].magnetism.thetaM.range(150, 390)
    x += 2

# Load the data

#Oliver needs to double check if instrument needs to be replaced by platypus. Platypus doesn't have load.magnetic feature
# current instrument is stock from refl1d examples.

instrument = NCNR.NG1(slits_at_Tlo=0.5)
probe = instrument.load_magnetic(["n101Gc1.reflA", None, "n101Gc1.reflC", "n101Gc1.reflD"])


experiment = Experiment(probe=probe, sample=Fifthteen, dz=0.3, dA=None)
problem = FitProblem(experiment)
