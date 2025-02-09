from setuptools import setup, find_packages

   setup(
       name='customenv',
       version='0.1.0',  # Choose your version number
       packages=find_packages(where='/content/BenchMARL/benchmarl/environments/'),
       install_requires=[
           # Add any dependencies your package needs
           # Example: 'torch>=1.10.0'
       ],
   )