from setuptools import setup

setup(
    name='cdk_constructs',
    version='0.2',    
    description='test construct modules',
    author='Irene Jia',
    author_email='irene.jia@stelligent.com',
    license='MIT',
    packages=['cdk_constructs'],
    install_requires=['aws-cdk-lib==2.0.0',
                      'constructs>=10.0.0,<11.0.0']
)