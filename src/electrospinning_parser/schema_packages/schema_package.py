from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

import numpy as np
from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.metainfo import Quantity, SchemaPackage, Section, MSection, SubSection
from runschema.run import Run
from runschema.calculation import Calculation

configuration = config.get_plugin_entry_point(
    'electrospinning_parser.schema_packages:schema_package_entry_point'
)

m_package = SchemaPackage()

class ElectrospinningOutput(MSection):
    surface = Quantity(type=np.float64, shape=['*', 5], description="""Arrays consisting of 5 values each. 1st value is total time in ms,
                                                                     2nd value is surface index, 3rd value is charge density at surface
                                                                     in C*um-1, 4th value is surface voltage in V, 5the value is
                                                                     electric field at surface in kV/um.""")
class ElectrospinningInput(MSection):
    m_def = Section(validate=False)
    h_sys = Quantity(type=float, description='Separation between the fixed point and the grounded cylinder in microns.')
    r0 = Quantity(type=float, description='Radius of the cylinder in microns.')
    d_fi = Quantity(type=float, description='Diameter of the nanofiber in microns.')
    vel = Quantity(type=float, description='Printing speed in cm s^-1.')
    d_drum = Quantity(type=float, description='Diameter of rotating drum in cm.')
    w_rot = Quantity(type=float, description='Rotational speed in radians^-1.')
    epsi_r = Quantity(type=float, description='Dielectric constant.')
    K_e = Quantity(type=float, description='Conductivity of electron in dielectric material in S/m.')
    K_a = Quantity(type=float, description='Conductivity of electron in air in S/m.')
    mu_e = Quantity(type=float, description='Mobility of electron in dielectric material in 10^-8 cm^2 V^-1 s^-1.')
    mu_a = Quantity(type=float, description='Mobility of electron in air in cm^2 V^-1 s^-1.')
    D_e = Quantity(type=float, description='Diffusivity opf electron in dielectric material in cm^2 s^-1.')
    D_a = Quantity(type=float, description='Diffusivity of electron in air in cm^2 s^-1.')
    Qt = Quantity(type=float, description='Density of trapped state in microns^-1.')
    Ptr = Quantity(type=float, description='Transfer rate from mobile state to trapped state in ms^-1.')
    Pde = Quantity(type=float, description='Transfer  rate from trapped state to mobile state in ms^-1.')
    V0 = Quantity(type=float, description='Voltage at nozzle in kV.')
    Vh = Quantity(type=float, description='Voltage at substrate in kV.')
    rho0 = Quantity(type=float, description='Charge density in C micron^-1.')
    width = Quantity(type=float, description='Width of gaussian.')
    sd = Quantity(type=float, description='Standard deviation of gaussian.')
    num_itr = Quantity(type=float, description='Number of iteration.')
    eps = Quantity(type=float, description='The convergence for the iteration.')
    barrier = Quantity(type=float, description='Barrier height in eV')
    dx = Quantity(type=float, description='Resolution in microns.')
    dt = Quantity(type=float, description='Time step in ms.')
    t_max = Quantity(type=float, description='max time step in ms.')
    t_out = Quantity(type=float, description='Output time step in ms.')
class ElectrospinningCalculation(Calculation):
    m_def = Section(validate=False, extends_base_section=False)

    electrospinning_input = SubSection(sub_section=ElectrospinningInput.m_def)
    electrospinning_output = SubSection(sub_section=ElectrospinningOutput.m_def)


m_package.__init_metainfo__()
