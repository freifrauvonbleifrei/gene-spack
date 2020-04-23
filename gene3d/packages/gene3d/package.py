from spack import *


class Gene3d(CMakePackage):
    """GENE (Gyrokinetic Electromagnetic Numerical Experiment) 
    is an open source plasma microturbulence code which can be used 
    to efficiently compute gyroradius-scale fluctuations and the 
    resulting transport coefficients in magnetized fusion/astrophysical plasmas."""

    homepage = "http://genecode.org/"
    url      = "https://gitlab.mpcdf.mpg.de/GENE/gene3d-dev"
    git      = "https://gitlab.mpcdf.mpg.de/GENE/gene3d-dev.git"

    version('master', branch='master')
    version('for-exahd-adaptive', commit='29efaeecf7fc5d1f77c306e5451879d3e4f87f03')
    patch('gene3d-adaptive.patch', when='@for-exahd-adaptive')

    #TODO use   
    variant('futils', default=False, description='Enable FUTILS')
    variant('gvec', default=True, description='Enable GVEC')
    variant('utests', default=False, description='Enable Unit-Tests with pFUnit')
    variant('python', default=False, description='Enable Python binding to libraries')
    variant('shared', default=True, description='Enable shared library for GENE3D')

    depends_on('futils', when='+futils')

    depends_on('pfunit', when='utests')

    extends('python', when='+python')
    depends_on('python', when='+python')

    depends_on('slepc@3.7.4', when='@for-exahd-adaptive')
    depends_on('petsc@3.7.6.2 +shared +mpi +complex +fftw', when='@for-exahd-adaptive')
    depends_on('slepc', when='@master')
    depends_on('petsc +shared +mpi +complex +fftw', when='@master')


    def cmake_args(self):
        spec = self.spec
        options = []

        options.append(self.define_from_variant('ENABLE_FUTILS', 'futils'))
        options.append(self.define_from_variant('ENABLE_GVEC', 'gvec'))
        options.append(self.define_from_variant('ENABLE_UTESTS', 'utests'))
        options.append(self.define_from_variant('ENABLE_PYTHON_BYNDINGS', 'python'))
        options.append(self.define_from_variant('ENABLE_SHARED_GENE3D_LIB', 'shared'))



        return options


 
