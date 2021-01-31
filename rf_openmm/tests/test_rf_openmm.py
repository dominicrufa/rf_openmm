"""
Unit and regression test for the rf_openmm package.
"""

# Import package, test suite, and other packages as needed
import rf_openmm
import pytest
import sys

def test_rf_openmm_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "rf_openmm" in sys.modules
