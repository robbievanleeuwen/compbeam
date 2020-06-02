class CompBeam:
    """a

    :cvar sections: A list of composite section objects
    :cvar float l_ef: The effective span of the composite beam which 'shall be taken as the
        approximate distance between points of zero bending moment'
    :cvar sfd: Shear force diagram
    :cvar bmd: Bending moment diagram
    """

    def __init__(self, l_ef):
        """Inits the CompBeam class."""

        self.l_ef = l_ef

    def define_sections(self):
        """a"""

        pass
