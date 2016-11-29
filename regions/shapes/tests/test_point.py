# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from astropy.coordinates import SkyCoord
from ...core import PixCoord
from ..point import PointPixelRegion, PointSkyRegion
from .utils import ASTROPY_LT_13


class TestPointPixelRegion:
    def setup(self):
        center = PixCoord(3, 4)
        self.reg = PointPixelRegion(center)

    def test_str(self):
        expected = 'PointPixelRegion\ncenter: PixCoord(x=3, y=4)'
        assert str(self.reg) == expected


class TestPointSkyRegion:
    def setup(self):
        center = SkyCoord(3, 4, unit='deg')
        self.reg = PointSkyRegion(center)

    def test_str(self):

        if ASTROPY_LT_13:
            expected = 'PointSkyRegion\ncenter: <SkyCoord (ICRS): (ra, dec) in deg\n    (3.0, 4.0)>'
        else:
            expected = 'PointSkyRegion\ncenter: <SkyCoord (ICRS): (ra, dec) in deg\n    ( 3.,  4.)>'

        assert str(self.reg) == expected
