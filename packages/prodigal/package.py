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
#     spack install prodigal
#
# You can edit this file again by typing:
#
#     spack edit prodigal
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Prodigal(Package):
    """PRODIGAL (PROkaryotic DynamIc Programming Genefinding ALgorithm)"""

    homepage = "http://www.example.com"
    url      = "https://github.com/hyattpd/Prodigal/archive/v2.6.3.tar.gz"

    version('2.6.3', '5181809fdb740e9a675cfdbb6c038466')
    version('2.6.2', 'c12a36c451042adc9c3e5ec378c4e406')
    version('2.6.1', '2f73eb2cf04c912ae828f54f077a4e73')

    parallel = False

    def install(self, spec, prefix):
        filter_file(r'INSTALLDIR  = /usr/local/bin',
		      'INSTALLDIR = {0}'.format(self.prefix.bin),
		      'Makefile')
    	mkdirp(prefix.bin)
    	make()
        make('install')
