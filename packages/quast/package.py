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
#     spack install quast
#
# You can edit this file again by typing:
#
#     spack edit quast
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Quast(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/ablab/quast"
    url      = "https://github.com/ablab/quast/archive/quast_4.5.tar.gz"

    version('4.5', '1f7c12a99714041b0a621e8ac18602fd')
    version('4.4', '045bcfd2db2c1de35184135b351d5ac2')
    version('4.3', 'e066b9ef106d0850fcc6e966eff68f5f')
    version('4.2', '80a659a278fd74b28b5223dce2fd2c74')
    version('4.1', '911559fa8f8fc017f929e416ef3a9ef3')
    version('4.0', '3a864c4ecd20abfeb5869ad5c46abe6c')

    depends_on('python@2.7.13')
    depends_on('py-matplotlib')
    #depends_on('boost@1.56.0')

    def install(self, spec, prefix):
	import subprocess,shutil
	try:
		subprocess.check_call(['./install_full.sh'])
	except subprocess.CalledProcessError as e:
		print e
	mkdirp(join_path(prefix.bin))
	install('quast.py', join_path(prefix.bin))
	install('icarus.py', join_path(prefix.bin))
	install('metaquast.py', join_path(prefix.bin))
	try:
		shutil.copytree('./quast_libs', join_path(prefix.bin,'quast_libs'))
		shutil.copytree('./test_data', join_path(prefix.bin,'test_data'))
	except shutil.Error as e:
		for (s,d,m) in e.args[0]:
			print "file %s failed to copy to %s: %s" %(s,d,m) 

