from pathlib import Path
from setuptools import setup, find_packages

version_info = {}
version_path = Path(__file__).parent / "view8/__version__.py"
exec(version_path.read_text(), version_info)

setup(
    name="View8",
    version=version_info["__version__"],
    description="View8 is a static analysis tool designed to decompile serialized " \
                "V8 bytecode objects (JSC files) into high-level readable code.",
    long_description=open("README.md", "r").read(),
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        'console_scripts': [
            'view8=view8.view8:main'
        ],
    },
)