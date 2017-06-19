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
#     spack install py-ls-bsr
#
# You can edit this file again by typing:
#
#     spack edit py-ls-bsr
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class LsBsr(Package):
    """LS-BSR python package """
    # We tried to build this as a PythonPackage but the
    # structure of the repo wouldn't behave well between
    # setup.py, pythonpath, and spack. So we do a generic install.

    homepage = "https://github.com/jasonsahl/LS-BSR"
    url      = "https://github.com/jasonsahl/LS-BSR.git"

    version('current', git=url)

    depends_on('py-biopython', type='run')
    depends_on('vsearch', type='run')
    depends_on('cd-hit', type='run')
    depends_on('blast-plus', type='run')
    depends_on('blat', type='run')
    depends_on('prodigal', type='run')

#    @run_before('install')
#    def edit(self):
#        orig = "long_description=long_description"
#        mod = orig+",\n      scripts=[\'ls_bsr.py\',\'igs_logging.py\']"
#        filter_file(orig,mod,'setup.py')

    def install(self,spec,prefix):
        chmod = which('chmod')
        pkg_path=join_path(prefix.bin, 'ls_bsr')
        mkdirp(prefix.bin)
        mkdirp(pkg_path)
        chmod('a+x', 'ls_bsr.py')
        install('ls_bsr.py', prefix.bin)
        install('igs_logging.py', prefix.bin)
        install('ls_bsr/util.py', pkg_path)
        install('ls_bsr/__init__.py', pkg_path)
