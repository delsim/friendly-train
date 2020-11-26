#!/usr/bin/env python

from setuptools import setup, find_packages

with open('friendly_train/version.py') as f:
    exec(f.read())

with open('README.md') as f:
    long_description = f.read()

setup(
    name="friendly-train",
    version=__version__,
    url="https://github.com/GibbsConsulting/jupyter-plotly-dash",
    description="Network port forwarding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gibbs Consulting",
    author_email="friendly_train@gibbsconsulting.ca",
    license='MIT',
    packages=find_packages(),
    classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    ],
    keywords='netcat',
    project_urls = {
    'Source': "https://github.com/GibbsConsulting/friendly-train",
    'Tracker': "https://github.com/GibbsConsulting/friendly-train/issues",
    'Documentation': 'http://friendly-train.readthedocs.io/',
    },
    install_requires = ['aiohttp',
                        ],
    python_requires=">=3.6",
    #data_files = [
    #("etc/jupyter/jupyter_notebook_config.d", [
    #"jupyter-config/jupyter_notebook_config.d/jupyter-plotly-dash.json"
    #])
    #],
    include_package_data = True,
    zip_safe = False,
    )

