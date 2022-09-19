# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['ureg', 'Q', 'calculate_energy']

# %% ../nbs/00_core.ipynb 4
import pint
import sympy as smp
from scipy.constants import Rydberg, h, c, physical_constants

# %% ../nbs/00_core.ipynb 5
ureg = pint.UnitRegistry()
Q = ureg.Quantity # quantity

# %% ../nbs/00_core.ipynb 29
def calculate_energy(**kwargs):
    
    keys = kwargs.keys()
    
    if 'frequency' in keys:
        return h * kwargs['frequency']
    elif 'wavelength' in kwargs:
        return (h * c)/kwargs['wavelength']
