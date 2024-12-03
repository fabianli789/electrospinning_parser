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

from nomad.config import config
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.parsing.parser import MatchingParser
from runschema.run import Run, Program
from runschema.calculation import Calculation
from electrospinning_parser.schema_packages.schema_package import ElectrospinningCalculation, ElectrospinningInput, ElectrospinningOutput

configuration = config.get_plugin_entry_point(
    'electrospinning_parser.parsers:parser_entry_point'
)

def DetailedParser(filepath, archive):
    run = Run()
    archive.run.append(run)
    run.program = Program(name="Ka Chun Chan electrospinning parser")

    with open(str(filepath.parent) + r'/input_electrospinning.data') as input_file:
        calculation = ElectrospinningCalculation()
        run.calculation.append(calculation)

        electrospinninginput = ElectrospinningInput()
        calculation.electrospinning_input = electrospinninginput
        for i, line in enumerate(input_file):
            line = line.strip('\n').strip(' ').strip('\t')
            if not re.search(r'\d', line):
                continue
            if re.search(r'h_sys', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.h_sys = float(parts[1])

            if re.search(r'r0', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.r0 = float(parts[1])
            if re.search(r'd_fi', line.lower()):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.d_fi = float(parts[1])
            if re.search(r'vel', line.lower()):
               parts1, parts2 = line.split('#')
               parts = parts1.split('= ')
               electrospinninginput.vel = float(parts[1])
            if re.search(r'd_drum', line.lower()):
               parts1, parts2 = line.split('#')
               parts = parts1.split('= ')
               electrospinninginput.d_drum = float(parts[1])
            if re.search(r'w_rot', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.w_rot = float(parts[1])

            if re.search(r'epsi_r', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.epsi_r = float(parts[1])
            if re.search(r'K_e', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.K_e = float(parts[1])
            if re.search(r'K_a', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.K_a = float(parts[1])
            if re.search(r'mu_e', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.mu_e = float(parts[1])
            if re.search(r'mu_a', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.mu_a = float(parts[1])
            if re.search(r'D_e', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.D_e = float(parts[1])
            if re.search(r'D_a', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.D_a = float(parts[1])
            if re.search(r'Qt', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.Qt = float(parts[1])
            if re.search(r'Ptr', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.Ptr = float(parts[1])
            if re.search(r'Pde', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.Pde = float(parts[1])
            if re.search(r'V0', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.V0 = float(parts[1])
            if re.search(r'Vh', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.Vh = float(parts[1])
            if re.search(r'rho0', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.rho0 = float(parts[1])
            if re.search(r'width', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.width = float(parts[1])
            if re.search(r'sd', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.sd = float(parts[1])
            if re.search(r'num_itr', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.num_itr = float(parts[1])
            if re.search(r'eps', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.eps = float(parts[1])
            if re.search(r'barr', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.barrier = float(parts[1])
            if re.search(r'dx', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.dx = float(parts[1])
            if re.search(r'dt', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.dt = float(parts[1])
            if re.search(r't_max', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.t_max = float(parts[1])
            if re.search(r't_out', line):
                parts1, parts2 = line.split('#')
                parts = parts1.split('= ')
                electrospinninginput.t_out = float(parts[1])

    _surface = np.load(str(filepath.parent) + r'/surface_electrospinning.npy')

    electrospinningoutput = ElectrospinningOuput()
    calculation.electrospinning_output = electrospinningoutput

    electrospinningoutput.surface = _surface

class NewParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info('NewParser.parse', parameter=configuration.parameter)

        archive.workflow2 = Workflow(name='test')

        mainfile = Path(mainfile)
        DetailedParser(mainfile, archive)