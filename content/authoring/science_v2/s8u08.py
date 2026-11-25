from science_v2.k import Unit
U = Unit("s8u08")

U.q("R", "8.1", "O1", "A car travels 120 km in 2 hours. What is its average speed?", ("60 km/h", "Speed = distance ÷ time."), [("240 km/h", "That multiplies."), ("122 km/h", "That adds.")])
U.q("P", "8.2", "O2", "On a distance–time graph, what does a flat (horizontal) line show?", ("The object is not moving", "Distance does not change."), [("The object is moving fast", "A steep line shows fast movement."), ("The object is speeding up", "That would be a curve.")])
U.q("E", "8.3", "O3", "A ball is thrown upwards. Zoe says the force from her hand keeps pushing it up. What is wrong?", ("Once released, only gravity (and air resistance) act on it", "The hand's force stops when contact ends."), [("Nothing", "Contact forces stop when contact ends."), ("There are no forces on it", "Gravity still acts.")])
U.q("R", "8.4", "O4", "Why is a door handle placed far from the hinges?", ("A larger distance gives a bigger turning effect for the same force", "Moment = force × distance."), [("To look nicer", "The physics reason is the moment."), ("It makes the door lighter", "Mass does not change.")])
V2 = U.V2
