# -*- coding: utf-8 -*-

# Imports ###########################################################

import os
from setuptools import setup


# Functions #########################################################

def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


# Main ##############################################################

setup(
    name='xblock-group-project',
    version='0.1.2',
    description='XBlock - Group Project',
    packages=['group_project'],
    install_requires=[
        'XBlock>=1.1',
    ],
    entry_points={
        'xblock.v1': 'group-project = group_project:GroupProjectBlock',
    },
    package_data=package_data("group_project", ["static", "templates", "public", "res"]),
)
