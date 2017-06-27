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


class Hbase(Package):
    """ Use Apache HBase when you need random,
        realtime read/write access to your Big Data.
        This project's goal is the hosting of very large tables
        -- billions of rows X millions of columns
        -- atop clusters of commodity hardware. """

    homepage = "https://hbase.apache.org/"
    url      = "http://apache.cs.utah.edu/hbase/1.2.6/hbase-1.2.6-bin.tar.gz"

    version('1.2.6', 'e2b28a6a0bb1699f853bd9ad9a813b2c')

    depends_on('jdk', type='run')
    depends_on('hadoop', type='run')

    def install(self, spec, prefix):
        def install_dir(dirname):
            install_tree(dirname, join_path(prefix, dirname))

        install_dir('bin')
        install_dir('conf')
        install_dir('docs')
        install_dir('lib')
        install_dir('hbase-webapps')
