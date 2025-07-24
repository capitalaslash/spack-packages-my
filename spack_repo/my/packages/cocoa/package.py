# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cocoa(CMakePackage):
    """CoCoA: Code Coupling for generic Applications."""

    homepage = "https://github.com/capitalaslash/cocoa.git"
    url = "https://github.com/capitalaslash/cocoa.git"
    git = "https://github.com/capitalaslash/cocoa.git"

    maintainers("capitalaslash")

    license("GPL-2.0-or-later", checked_by="capitalaslash")

    version("main", branch="main")

    variant("medcoupling", default=False, description="Enable MEDCoupling interface")
    variant("proxpde", default=False, description="Enable ProXPDE interface")
    variant("python", default=False, description="Build python bindings")

    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("fmt")
    depends_on("salome-medcoupling", when="+medcoupling")
    depends_on("proxpde@master", when="+proxpde")
    depends_on("py-pybind11", when="+python")

    def cmake_args(self):
        args = [
            self.define_from_variant("COCOA_ENABLE_MEDCOUPLING", "medcoupling"),
            self.define_from_variant("COCOA_ENABLE_PROXPDE", "proxpde"),
            self.define_from_variant("COCOA_ENABLE_PYTHON", "python"),
        ]
        if "+medcoupling" in self.spec:
            args.append(self.define("MEDCoupling_DIR", self.spec["salome-medcoupling"].prefix + "/cmake_files"))

        return args
