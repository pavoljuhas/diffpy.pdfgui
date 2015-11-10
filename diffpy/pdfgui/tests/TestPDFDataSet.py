#!/usr/bin/env python
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2008 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

"""Unit tests for pdfdataset.py
"""


import os
import unittest

from diffpy.pdfgui.control.pdfdataset import PDFDataSet

# useful variables
thisfile = locals().get('__file__', 'TestPDFDataSet.py')
tests_dir = os.path.dirname(os.path.abspath(thisfile))
testdata_dir = os.path.join(tests_dir, 'testdata')


##############################################################################
class TestPDFDataSet(unittest.TestCase):

    def setUp(self):
        self.pdfds = PDFDataSet('test data set')
        return

    def tearDown(self):
        self.pdfds = None
        return

#   def test___init__(self):
#       """check PDFDataSet.__init__()
#       """
#       return
#
#   def test_clear(self):
#       """check PDFDataSet.clear()
#       """
#       return
#
#   def test_setvar(self):
#       """check PDFDataSet.setvar()
#       """
#       return
#
#   def test_getvar(self):
#       """check PDFDataSet.getvar()
#       """
#       return
#
    def test_read(self):
        """check PDFDataSet.read()
        """
        # neutron data -------------------------------------------------
        fn_550K = os.path.join(testdata_dir, '550K.gr')
        self.pdfds.read(fn_550K)
        self.assertEqual('N', self.pdfds.stype)
        self.assertEqual(32.0, self.pdfds.qmax)
        # there are 2000 points in the file
        npts = len(self.pdfds.robs)
        self.assertEqual(2000, npts)
        # drobs are all zero
        self.assertEqual(npts*[0.0], self.pdfds.drobs)
        # dGobs should be defined
        self.failUnless(min(self.pdfds.dGobs) > 0)
        # x-ray data ---------------------------------------------------
        fx_Ni = os.path.join(testdata_dir, 'Ni_2-8.chi.gr')
        self.pdfds.read(fx_Ni)
        self.assertEqual('X', self.pdfds.stype)
        self.assertEqual(40.0, self.pdfds.qmax)
        # there are 2000 points in the file
        npts = len(self.pdfds.robs)
        self.assertEqual(2000, npts)
        # drobs are all zero
        self.assertEqual(npts*[0.0], self.pdfds.drobs)
        # dGobs should be defined
        self.failUnless(min(self.pdfds.dGobs) > 0)
        return

    def test_readStr(self):
        """check PDFDataSet.readStr()
        """
        # read Ni xray data, but invalidate the last dGobs
        fx_Ni = os.path.join(testdata_dir, 'Ni_2-8.chi.gr')
        sNi = open(fx_Ni).read()
        lastdGobs = sNi.rstrip().rindex(' ')
        sNi_no_dGobs = sNi[:lastdGobs] + " -1.3e-3"
        self.pdfds.readStr(sNi_no_dGobs)
        # there are 2000 points in the file
        npts = len(self.pdfds.robs)
        self.assertEqual(2000, npts)
        # dGobs should be all zero
        self.assertEqual(npts*[0.0], self.pdfds.dGobs)
        return

#   def test_write(self):
#       """check PDFDataSet.write()
#       """
#       return
#
#   def test_writeStr(self):
#       """check PDFDataSet.writeStr()
#       """
#       return
#
#   def test_copy(self):
#       """check PDFDataSet.copy()
#       """
#       return
#
#   def test_close(self):
#       """check PDFDataSet.close()
#       """
#       return

# End of class TestPDFDataSet


if __name__ == '__main__':
    unittest.main()

# End of file