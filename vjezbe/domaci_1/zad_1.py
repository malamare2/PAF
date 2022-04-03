import particle as prt 
p1 = prt.Particle(0, 0, 30, 10, 0.01)
p1.set_initial_conditions(0, 0, 30, 10, 0.01)

print(p1.total_time())
print(p1.max_speed())
print(p1.velocity_to_hit_target(5, 1, 4, 20))
print(p1.angle_to_hit_target(5, 1, 2, 20))