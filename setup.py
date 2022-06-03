import setuptools

setuptools.setup(
    name='pydynet',
    version='0.0.3',
    description=
    'Neuron network(DNN, CNN, RNN, etc) implementation using Numpy based on autodiff',
    author_email="191300064@smail.nju.edu.cn",
    packages=['pydynet'],
    license='MIT License',
    install_requires=['numpy'],
    long_description=open('README.md', encoding='utf-8').read(),
    url='https://github.com/Kaslanarian/PyDyNet',
)