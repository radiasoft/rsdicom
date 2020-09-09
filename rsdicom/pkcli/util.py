# -*- coding: utf-8 -*-
"""Process DICOM files.

:copyright: Copyright (c) 2020 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function

from pykern.pkcollections import PKDict

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


def nonconformant_names(file='/vagrant/ucla-140/ct/2.16.840.1.114362.1.11775105.22699029554.543997656.413.2799.dcm'):
    import pydicom
