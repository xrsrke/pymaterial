pymaterial
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` sh
pip install pymaterial
```

### Why Material Science?

How do we know what material to use?

### Example 1: Why… $\mathrm{H}_2\mathrm{O}$?

``` python
attractive_force = AttractiveForce()
```

``` python
charge_1 = Q(25, 'ncoulomb')
```

``` python
charge_2 = Q(-75, 'ncoulomb')
```

``` python
interatomic_separation = Q(3, 'centimeter')
```

``` python
charge_1, charge_2, interatomic_separation
```

    (25 <Unit('nanocoulomb')>, -75 <Unit('nanocoulomb')>, 3 <Unit('centimeter')>)

The attractive Force between charge 1 and charge 2

``` python
attractive_force.magnitude(charge_1, charge_2, interatomic_separation)
```

0.018724066233877443 newton

``` python
attractive_force.constant_a(charge_1, charge_2)
```

4.325770410640756×10<sup>-43</sup> coulomb<sup>2</sup> meter<sup>2</sup> newton

The attractive energy $E_A$ between charge 1 and charge 2

``` python
attractive_energy = AttractiveEnergy()
```

``` python
attractive_energy.magnitude(charge_1, charge_2, interatomic_separation)
```

-1.4419234702135854e-41 coulomb<sup>2</sup> meter newton
