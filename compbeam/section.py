class CompSection:
    """a

    :cvar comp_beam: Composite beam object that the section is used in
    :vartype comp_beam: :class:`~compbeam.beam.CompBeam`
    :cvar float b0: Distance between the centres of the outstand shear connectors
    :cvar float b1: Left centre-to-centre spacing of adjacent beams or distance from centre of
        steel beam to edge of slab outstand
    :cvar float b2: Right centre-to-centre spacing of adjacent beams or distance from centre of
        steel beam to edge of slab outstand
    :cvar float rib_angle: Angle the composite ribs make with the steel beam axis in degrees
    """

    def __init__(self, b0, b1, b2, rib_angle):
        """Inits the CompSection class."""

        self.comp_beam = None
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.rib_angle = rib_angle

    def set_comp_beam(self, comp_beam):
        """Sets the CompBeam attribute.

        :param comp_beam: CompBeam object that the sections is used in
        :type comp_beam: :class:`~compbeam.beam.CompBeam`
        """

        self.comp_beam = comp_beam

    def calculate_effective_width(self):
        """Calculates the effective width of the composite beam section.

        :returns: Effective width of the composite beam
        :rtype: float
        """

        be1 = self.b1 - self.b0
        be2 = self.b2 - self.b0

        return self.b0 + min(self.comp_beam.l_ef / 8, be1) + min(self.comp_beam.l_ef / 8, be2)
