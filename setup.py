from setuptools import setup
from setuptools import find_packages

# Load the README file.
with open(file='README.md', mode='r') as readme_handle:
    long_description = readme_handle.read()

# Load the __version__ script.
with open('./cnosolar/version.py', mode='r') as f:
    exec(f.read()) 
    
setup(
    # Define the library name, this is what is used along with `pip install`.
    name = 'cnosolar',

    # Define the author of the repository.
    author = 'Consejo Nacional de Operación',

    # Define the Author's email, so people know who to reach out to.
    author_email = 'angonzal@uniandes.edu.co',

    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version = __version__

    # Here is a small description of the library. This appears
    # when someone searches for the library on https://pypi.org/search.
    description='Protocolos para el cálculo de la CEN, ENFICC y Modelo Recurso-Potencia del Acuerdo Específico 5 al convenio marco CNO-UNIANDES.',

    # I have a long description but that will just be my README
    # file, note the variable up above where I read the file.
    long_description=long_description,

    # This will specify that the long description is MARKDOWN.
    long_description_content_type='text/markdown',

    # Here is the URL where you can find the code, in this case on GitHub.
    url='https://github.com/andresgm/cno_solar',

    # These are the dependencies the library needs in order to run.
    install_requires=['cftime==1.4.0',
                      'ipython==7.8.0',
                      'ipywidgets==7.5.1',
                      'jupyter==1.0.0',
                      'matplotlib==3.1.1',
                      'netCDF4==1.5.5.1',
                      'numpy==1.19.2',
                      'openpyxl==3.0.0',
                      'pandas==0.25.1',
                      'pvfactors==1.5.1',
                      'pvlib==0.9.0',
                      'pytest==5.2.1',
                      'pytz==2019.3',
                      'requests==2.22.0',
                      'scikit-learn==0.24.2',
                      'scipy==1.3.1',
                      'seaborn==0.9.0',
                      'siphon==0.8.0',
                      'tqdm==4.36.1',
                      'traitlets==4.3.3'],

    # Here are the keywords of my library.
    keywords='solar energy', 'pvlib', 'GUI',

    # here are the packages I want "build."
    packages=find_packages(include=['cnosolar', 'cnosolar.*']),

    # I also have some package data, like photos and JSON files, so
    # I want to include those as well.
    include_package_data=True,

    # Here I can specify the python version necessary to run this library.
    python_requires='>=3.7',

    # Additional classifiers that give some characteristics about the package.
    # For a complete list go to https://pypi.org/classifiers/.
    classifiers=[
        # I can say what phase of development my library is in.
        'Development Status :: 3 - Alpha',

        # Here I'll add the audience this library is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',

        # Here I'll define the license that guides my library.
        'License :: OSI Approved :: MIT License',

        # Here I'll note that package was written in English.
        'Natural Language :: English',

        # Here I'll note that any operating system can use it.
        'Operating System :: OS Independent',

        # Here I'll specify the version of Python it uses.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',

        # Here are the topics that my library covers.
        'Topic :: Education',
        'Topic :: Office/Business',
        'Topic :: Scientific/Engineering']
)