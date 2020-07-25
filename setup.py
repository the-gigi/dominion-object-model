from setuptools import setup

setup(name='dominion-object-model',
      version='1.1.0',
      url='https://github.com/the-gigi/dominion-object-model',
      license='MIT',
      author='Gigi Sayfan',
      author_email='the.gigi@gmail.com',
      description='abstract classes for implementing dominion players and clients',
      packages=['dominion_object_model'],
      python_requires='>=3.8',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      zip_safe=False)
