#!/usr/bin/env python
"""Provide error classes for risk_cohort_rnaseq."""

# Imports
import logging
log = logging.getLogger(__name__)


# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"




class RiskCohortRnaseqError(Exception):

    """Base error class for risk_cohort_rnaseq."""


class ValidationError(RiskCohortRnaseqError):

    """Raise when a validation/sanity check comes back with unexpected value."""
