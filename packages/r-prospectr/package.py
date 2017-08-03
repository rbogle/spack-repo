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
#     spack install r-prospectr
#
# You can edit this file again by typing:
#
#     spack edit r-prospectr
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class RProspectr(RPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://cran.r-project.org/web/packages/prospectr/index.html"
    url      = "https://cran.r-project.org/src/contrib/prospectr_0.1.3.tar.gz"

    version('0.1.3', 'f4bed91a86fb050e603b403e34f69cc4')
    version('0.1.1', '20866211d5e7816e5d374d71c94c469a')
    version('0.1',   '1c7bfe4fd2963ed227fba17664e7cd5b')

    depends_on('r-iterators')
    depends_on('r-foreach')
    depends_on('r-rcpp')
    depends_on('r-rcpparmadillo')
 

