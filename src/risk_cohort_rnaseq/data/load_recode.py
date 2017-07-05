#!/usr/bin/env python
"""Provide logic to import, parse, and recode project data into usable structures for analysis."""

# Imports
import os
from pathlib import Path
import logging

import pandas as pd
import numpy as np

from munch import Munch, munchify, unmunchify

import GEOparse

import risk_cohort_rnaseq.errors as e

# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"


# Functions
def load_gse(geo=None, filepath=None, destdir=None, how='full', annotate_gpl=False, geotype=None, include_data=False, silent=True):
    
    gse = GEOparse.get_GEO(geo=geo, filepath=filepath, destdir=destdir,
                           how=how, annotate_gpl=annotate_gpl, geotype=geotype,
                           include_data=include_data,
                           silent=silent)
    
    # Make the `dict` attrs Munch types for ease of use in Jupyter
    gse.gpls = Munch(gse.gpls)
    gse.gsms = Munch(gse.gsms)
    
    munchify_geoobjs(geos=gse.gpls)
    munchify_geoobjs(geos=gse.gsms)
    
    
    gse.relations = Munch(gse.relations)
    gse.metadata = Munch(gse.metadata)
    
    
    return gse

def munchify_geoobjs(geos):
    
    for geo in geos.values():
        geo.relations = Munch(geo.relations)
        geo.metadata = Munch(geo.metadata)
    