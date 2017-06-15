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
#     spack install perl-xml-simple
#
# You can edit this file again by typing:
#
#     spack edit perl-xml-simple
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PerlXmlSimple(PerlPackage):
    """Installs the perl Xml::Simple package"""

    homepage = "https://github.com/grantm/xml-simple"
    url      = "http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-Simple-2.24.tar.gz"

    depends_on('perl')

    version('2.24', '1cd2e8e3421160c42277523d5b2f4dd2')
    version('2.23', '5b29e3809e6841c4fe5dca9e9245881d')
    version('2.22', '0914abddfce749453ed89b54029f2643')
    version('1.08', 'ddad9f53e1bb97863b0ec89e27e529c8')
