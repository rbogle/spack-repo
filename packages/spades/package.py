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

from spack import *

class Spades(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://cab.spbu.ru/software/spades/"
    url      = "http://cab.spbu.ru/files/release3.10.1/SPAdes-3.10.1.tar.gz"

    version('3.10.1', 'dcab7d145af81b59cc867562f27536c3')

    def url_for_version(self, version):
	base = "http://cab.spbu.ru/files/"
	release = "release{0}/".format(version)
	archive = "SPAdes-{0}.tar.gz".format(version)
	return base+release+archive

    # SPAdes uses a non-standard cmake configuration so we have to modify
    # the build_dir and root_cmakelists
    @property
    def build_directory(self):
	return join_path(self.stage.source_path, 'spades_build')

    @property
    def root_cmakelists_dir(self):
	return join_path(self.stage.source_path, 'src')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-G', 'Unix Makefiles']
        return args

