'''In here, a base class 'Particles' is defined, from which several subclasses
(corresponding to actual particles) inherit.
'''


class Particle:
    '''Base class that can be used to define particles.
    '''
    def __init__(self, mass, charge, name, energy = None):
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
            return f'{self.__class__.__name__}"{self.name}"(mass {self.mass}, charge {self.charge}, energy {self.energy})'

        return f'{self.__class__.__name__}"{self.name}"(mass {self.mass}, charge {self.charge})'


class Proton:
    '''Child class of Particle that describes protons
    '''

    def __init__(self, energy = None):
        '''Proton can be given an energy.

        Arguments
        ---------

        energy: float, optional
            energy of the proton in MeV
        '''
        Particle.__init__(self, mass = 1., charge = 1, name = 'Proton', energy = energy)

    def __str__(self):
        if self.energy is not None:
            return f'{self.__class__.__name__}(energy {self.energy})'
        return f'{self.__class__.__name__}'





particle1 = Particle(mass = 1, charge = 0, name = 'whatever')

proton = Proton()

print(particle1)

print(proton)
