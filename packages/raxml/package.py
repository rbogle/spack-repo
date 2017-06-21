##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install raxml
#
# You can edit this file again by typing:
#
#     spack edit raxml
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import os.path

class Raxml(Package):
    """RAxML genetics package """


    homepage = "https://github.com/stamatak/standard-RAxML"
    url      = "https://github.com/stamatak/standard-RAxML.git"

    version('8.2.10', git=url, tag='v8.2.10')

    depends_on('openmpi')
    
    parallel=False

    variant('MPI', default=True, description='compile mpi version')
    variant('HYBRID', default=True, description='compile hybrid version')
    variant('PTHREADS', default=True, description='compile pthreads version')
    variant('SSE3', default=True, description='compile SSE3 flags')
    variant('AVX2', default=True, description='compile AVX2 flags')
    variant('AVX', default=True, description='compile AVX flags')

    @run_before('install')
    def config_names(self):
        self.flags = ['SSE3','AVX','AVX2']
        self.algs = ['MPI','HYBRID','PTHREADS']
        self.makefiles = ["Makefile.gcc"]
        self.exe = ["raxmlHPC"]
        for name,val in self.spec.variants.iteritems():
            if not val:
                if name in self.flags:
                    self.flags.remove(name)
                if name in self.algs:
                    self.algs.remove(name)
        for a in self.algs:
            self.makefiles.append("Makefile.{0}.gcc".format(a))
            self.exe.append("raxmlHPC-{0}".format(a))
        for f in self.flags:
            self.makefiles.append("Makefile.{0}.gcc".format(f))
            self.exe.append("raxmlHPC-{0}".format(f))
            for a in self.algs:
                self.makefiles.append("Makefile.{0}.{1}.gcc".format(f,a))
                self.exe.append("raxmlHPC-{0}-{1}".format(a,f))

    def install(self, spec, prefix):
        for mf in self.makefiles:
            if os.path.isfile(mf):
                make('-f', mf)
        mkdirp(prefix.bin)
        for exe in self.exe:
            if os.path.isfile(exe):
                install(exe, prefix.bin)
