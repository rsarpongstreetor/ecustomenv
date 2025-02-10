from setuptools import setup, find_packages

    setup(
        name='customenv', 
        version='0.1.0',  # Update with your version
        packages=find_packages(), 
        install_requires=['benchmarl', 'torchrl', 'tensordict', 'torch_geometric', 'pyyaml'],  # Add other dependencies
    )
