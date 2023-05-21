
# IDEA #


























## Mathematics ##




The trajectory of a charged particle in a magnetic field is described by the Lorentz force equation, which is:

F = q(v x B)


where:

F is the force experienced by the charged particle
q is the charge of the particle
v is the velocity of the particle
B is the magnetic field
The cross product v x B gives a vector that is perpendicular to both v and B, and its magnitude is proportional to the product of the magnitudes of v and B, and the sine of the angle between them.

The force F causes the particle to undergo circular motion, with a radius given by:

r = mv/qB

where m is the mass of the particle.

The trajectory of the particle can be expressed in terms of the position vector r as a function of time t:

r(t) = r<sub>0</sub> + vt + (q/m)(v x B)t

where r<sub>0</sub>  is the initial position of the particle at t=0.

**This equation describes a helical path, with a circular _component in the plane perpendicular to the magnetic field, and a linear component along the direction of the magnetic field_**. The helix has a pitch given by:

***p = 2πmv / (qB)***

which is the distance along the direction of the magnetic field that the particle travels in one complete revolution around the circular component of the trajectory.




## Differential Equation##

As Maths enthusiasts we progressed our findings little further and used concepts of Differntial Equations and Vector Calculus to formulaize the results 

To derive the differential equation of the trajectory of a charged particle in a magnetic field, we start with the Lorentz force equation:

F = q(v x B)

To obtain the differential equation, we differentiate the position vector r with respect to time:

d<sup>2</sup>r / dt<sup>2</sup> = (q/m) d/dt (v x B)

Using the vector identity **_d/dt (v x B) = (dv/dt) x B + v x (dB/dt)_**, we can write:

d<sup>2</sup>r / dt<sup>2</sup> = (q/m) [(d/dt v) x B + v x (dB/dt)]

The first term on the right-hand side is the acceleration of the particle, which is given by the Lorentz force equation:

d/dt v = (q/m) (v x B)

Substituting this into the above equation, we get:

d<sup>2</sup>r / dt<sup>2</sup> = (q/m) [(q/m)(v x B)xB + vx(dB/dt)]

Using the vector identity (a x b) x c = b(a · c) - c(a · b), we can simplify the first term on the right-hand side:

(q/m) [(q/m) (v x B) x B] = (q<sup>2</sup>/m<sup>2</sup>) [B (v · B) - v (B · B)]

Since the magnetic field is perpendicular to the velocity, we have v · B = 0 and B · B = |B|^2, so the first term simplifies to:

(q^2/m^2) |B|<sup>2</sup>v

Substituting this and the expression for the magnetic field gradient (d/dt B) into the differential equation, we obtain:

d<sup>2</sup>r / dt<sup>2</sup>= (q^2/m^2) |B|<sup>2</sup> v + (q/m) v x (d/dt B)
