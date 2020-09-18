# -*- coding: utf-8 -*-
"""Process DICOM files.

:copyright: Copyright (c) 2020 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function

from pykern.pkcollections import PKDict
from pykern.pkdebug import pkdp

def default_command():
    import pydicom
    # The rtst files seem to be the ones with ROI in them
    ucla_140 = '/vagrant/ucla-140/rtst/2.16.840.1.114362.1.11775105.22699029554.543997669.1030.3153.dcm'
    coh_001 = '/vagrant/coh-001/rtst/RS.1.2.246.352.205.4827533863638583198.10720857379728702625.dcm'

    # 0x3006,0x0020 is the location in the dicom where the ROI structure set is
    # What is a structure set? => http://dicom.nema.org/dicom/2013/output/chtml/part03/sect_C.8.html#sect_C.8.8.5
    # Where are locations of other interesting data? => https://dicom.innolitics.com/ciods/rt-dose/structure-set/30060020
    r = pydicom.dcmread(ucla_140)[0x3006,0x0020]
    for e in r:
        pkdp('{}', e[0x3006,0x0026])
