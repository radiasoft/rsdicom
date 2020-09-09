# -*- coding: utf-8 -*-
"""Process DICOM files.

:copyright: Copyright (c) 2020 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function

from pykern.pkcollections import PKDict
from pykern.pkdebug import pkdp

def get_canonical_names():
    compatible_chars = ['_', '-', '^', '+', '=', '!', '~']
    incompatible_chars = [
        '<',
        '>',
        ':',
        '"',
        '\'',
        '/',
        '\\',
        '|',
        '?',
        '*',
        '.',
        '(',
        ')',
        '&',
        '#',
        '$',
    ]
    interpreted_types = PKDict(
        roi=[
            'avoidance',
            'bolus',
            'cavity',
            'contrast_agent',
            'ctv',
            'external',
            'gtv',
            'irrad_volume',
            'organ',
            'ptv',
            'registration',
            'treated_volume',
        ],
        poi=[
            'marker',
            'isocenter',
        ],
        brachytherapy=[
            'brach_channel',
            'brachy_accessory',
            'brachy_src_app',
            'brachy_chnl_shld',
        ],
    )
    import pdfquery
    pdf = pdfquery.PDFQuery('/vagrant/RPT_263.pdf')
    pdf.load()
    pdf.tree.write('x.xml', pretty_print=True)
    print(pdf.pq('LTTextLineHorizontal:in_bbox("366.711, 298.95, 409.578, 307.95")').text())


def nonconformant_names():
    import pydicom
    f = [
        # '/vagrant/ucla-140/ct/2.16.840.1.114362.1.11775105.22699029554.543997656.413.2799.dcm',
        '/vagrant/ucla-140/rtst/2.16.840.1.114362.1.11775105.22699029554.543997669.1030.3153.dcm',
        # '/vagrant/ucla-140/rtdose/2.16.840.1.114362.1.11775105.22699029554.543997671.684.3155.dcm ',
        # '/vagrant/ucla-140/rtplan/2.16.840.1.114362.1.11775105.22699029554.543997669.1026.3146.dcm',
    ]
    for n in f:
        r = pydicom.dcmread(n)[0x3006,0x0020]
        for e in r:
            pkdp('{}', e[0x3006,0x0026].value)
