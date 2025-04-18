'''In here, a base class 'Particles' is defined, from which several subclasses
(corresponding to actual particles) inherit.
'''

from typing import Union
from typing import Optional

class Particle:
    '''Base class that can be used to define particles.
    '''
    def __init__(self, mass: Union[int,float], charge: int, name: str, energy: Union[int, float] = None):
        '''Particles have to be initialized with their basic properties.

        Arguments
        ----------

        mass: float or int
            mass of the particle in u

        charge: float or int
            charge of the particle in e

        name: string
            name of the particle

        energy: float, optional
            energy of the particle in MeV


        '''

        if not isinstance(mass, (int, float)):
            raise TypeError("mass must be int or float")
        if not isinstance(charge, int):
            raise TypeError("charge must be int")
        if not isinstance(name, str):
            raise TypeError("name must be string")
        if energy is not None:
            if not isinstance(energy, (int, float)):
                raise TypeError("energy must be int, float or None")


        self.mass = mass
        self.charge = charge
        self.name = name

        if energy:
            self.energy = energy
        else:
            self.energy = None


    def __str__(self):
        '''Print
        '''
        if self.energy is not None:
            return f'{self.__class__.__name__} "{self.name}" (mass {self.mass}, charge {self.charge}, energy {self.energy})'

        return f'{self.__class__.__name__} "{self.name}" (mass {self.mass}, charge {self.charge})'


class Proton:
    '''Child class of Particle that describes protons
    '''

    def __init__(self, energy: Union[int, float] = None):
        '''Proton can be given an energy.

        Arguments
        ---------

        energy: float, optional
            energy of the proton in MeV
        '''
        Particle.__init__(self, mass = 1., charge = 1, name = 'Proton', energy = energy)

    def __str__(self):
        if self.energy is not None:
            return f'{self.__class__.__name__} (energy {self.energy})'
        return f'{self.__class__.__name__}'


class Alpha:
    '''Child class of Particle that describes alpha-particles
    '''

    def __init__(self, energy: Union[int, float] = None):
        '''Alpha-particle can be initialized with an energy

        Arguments
        ----------

        energy: float, optional
            energy of the Alpha-particle in MeV
        '''
        Particle.__init__(self, mass = 4.002, charge = 2, name = 'Alpha', energy = energy)

    def __str__(self):
        if self.energy is not None:
            return f'{self.__class__.__name__} (energy {self.energy})'
        return f'{self.__class__.__name__}'




particle1 = Particle(mass = 1, charge = 0, name = 'whatever')

proton = Proton()
alpha = Alpha(energy = 7)

print(particle1)

print(proton)
print(alpha)
