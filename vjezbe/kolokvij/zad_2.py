import projectiledrop

p1 = projectiledrop.ProjectileDrop()
p1.__init__()   
p1.set_initial_conditions(2.5, 1.6)
p1.novavisina(4)
p1.novabrzina(2)

p2 = projectiledrop.ProjectileDrop()
p2.__init__()    
p2.set_initial_conditions(2.5, 1.6)
p2.novavisina(1)
p2.novabrzina(0.5)