import matplotlib.pyplot as plt
import projectiledrop 

p1 = projectiledrop.ProjectileDrop()
p1.__init__()    
p1.set_initial_conditions(2, 200)
p1.move(20,0.01)
p1.vrijeme_trajanja()
p1.meta(2,0,3)