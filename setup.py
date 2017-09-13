from setuptools import setup, find_packages

setup(
    name='copernicus_download',
    version='0.2',
    description='Download from land.copernicus.vgt.vito.be/PDF/datapool',
    author='Jonas Solvsteen',
    author_email='josl@dhigroup.com',
    url='https://www.dhi-gras.com',
    packages=find_packages(),
    install_requires=[
        'wget_provider'],
    dependency_links=[
        'https://github.com/DHI-GRAS/wget_provider/archive/v0.1.tar.gz#egg=wget_provider-0.1'])
