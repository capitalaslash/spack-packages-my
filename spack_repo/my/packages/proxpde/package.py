# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Proxpde(CMakePackage):
    """ProXPDE - Prototyping with eXpression Templates for Partial Differential Equations."""

    homepage = "https://github.com/capitalaslash/proxpde.git"
    url = "https://github.com/capitalaslash/proxpde.git"
    git = "https://github.com/capitalaslash/proxpde.git"

    maintainers("capitalaslash")

    license("GPL-2.0-or-later", checked_by="capitalaslash")

    version("master", branch="master")

    variant("dof_interleaved", default=True, description="Set default dof mapping to interleaved")
    variant("second_deriv", default=False, description="Enable shape function second derivatives")

    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("eigen@3.4.0:")
    depends_on("fmt@11.2.0:")
    depends_on("ginkgo@1.9.0:~mpi+openmp")
    depends_on("hdf5@1.10.3:~mpi")
    depends_on("pugixml@1.14:")
    depends_on("suite-sparse@5.13:")
    depends_on("yaml-cpp@0.7.8:")

    def cmake_args(self):
        args = [
            self.define_from_variant("PROXPDE_DOF_INTERLEAVED", "dof_interleaved"),
            self.define_from_variant("PROXPDE_ENABLE_SECONDDERIV", "second_deriv"),
        ]
        return args

