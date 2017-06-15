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
#     spack install kakadu
#
# You can edit this file again by typing:
#
#     spack edit kakadu
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import platform
from shutil import copyfile,copytree

class Kakadu(MakefilePackage):
    """Builds the commercial licensed product Kakadu a jpeg2000 implementation"""

    # TODO: You will need to modify the url and version hash below to fit your enviro.
    homepage = "http://www.kakadusoftware.com"
    url      = "http://gold.wr.usgs.gov/postinstall/pkgs/common/kakadu-7.9.1.zip"

    version('7.9.1', 'dfe33cb66309039f7b3c4d861d50dfde')

    depends_on('jdk', type='build')

    def build_directory(self):
	return 'make'
    
    build_targets = ['all']
    parallel = False

    # We make a proper Makefile in ./make based on the platform
    # We are ignoring 32bit and PPC for now. 
    def edit(self, spec, prefix):
	makefile_out = join_path(self.build_directory(), 'Makefile')
	system = platform.system()
        makefile_in = join_path(self.build_directory(), 'Makefile-Linux-x86-64-gcc')
	self.build_dest = 'Linux-x86-64-gcc'
	if system == "Darwin" :
	  makefile_in = join_path(self.build_directory(), "Makefile-MAC-x86-all-gcc")
	  self.build_dest = "Mac-x86-64-gcc"	
	# copy the platform specific file to generic
        copyfile(makefile_in, makefile_out)

    def install(self, spec, prefix):
	copytree(join_path('./bin',self.build_dest),prefix.bin)
	copytree(join_path('./lib',self.build_dest),prefix.lib)
	copytree('./apps', join_path(prefix,'apps'))
	copytree('./coresys', join_path(prefix,'coresys'))
