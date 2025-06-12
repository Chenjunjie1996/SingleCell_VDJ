import setuptools
from celescope.__init__ import __VERSION__, ASSAY_LIST

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fp:
    install_requires = fp.read()

entrys = [
    "celescope=celescope.celescope:main",
]
for assay in ASSAY_LIST:
    entrys.append(f"multi_{assay}=celescope.{assay}.multi_{assay}:main")
entry_dict = {
    "console_scripts": entrys,
}


setuptools.setup(
    name="singlecell_vdj",
    version=__VERSION__,
    author="chenjunjie",
    author_email="cjj26163@gmail.com",
    description="Single-Cell/Bulk VDJ Analysis Pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chenjunjie1996/SingleCell_VDJ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    include_package_data=True,
    entry_points=entry_dict,
    install_requires=install_requires,
)
