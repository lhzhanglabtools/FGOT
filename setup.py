from setuptools import Command, find_packages, setup

__lib_name__ = "FGOT"
__lib_version__ = "1.0.0"
__description__ = "Interpretable data integration for single cell and spatial multi-omics"
__url__ = "https://github.com/lhzhanglabtools/FGOT"
__author__ = "Lihua Zhang"
__author_email__ = "zhanglh@whu.edu.cn"
__license__ = "MIT"
__keywords__ = ["single cell", "data integration", "optimal transport", "regulatory link"]
__requires__ = ["requests",]

setup(
    name = __lib_name__,
    version = __lib_version__,
    description = __description__,
    url = __url__,
    author = __author__,
    author_email = __author_email__,
    license = __license__,
    packages = ['FGOT'],
    install_requires = __requires__,
    zip_safe = False,
    include_package_data = True,
)

