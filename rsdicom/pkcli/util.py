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
    ucla_140 = [
        # '/vagrant/ucla-140/ct/2.16.840.1.114362.1.11775105.22699029554.543997656.413.2799.dcm',
        # This file defines the structures referenced elsewhere
        # Reference
        # (300c, 0060)  Referenced Structure Set Sequence   1 item(s) ----
        #     (0008, 1150) Referenced SOP Class UID            UI: RT Structure Set Storage
        #     (0008, 1155) Referenced SOP Instance UID         UI: 2.16.840.1.114362.1.11775105.22699029554.543997669.1030.3153
        # Definition
        # (3006, 0020)  Structure Set ROI Sequence   39 item(s) ----
        #   (3006, 0022) ROI Number                          IS: "20"
        #   (3006, 0024) Referenced Frame of Reference UID   UI: 1.2.840.113619.2.55.3.1678399520.770.1570458748.26.16755.5
        #   (3006, 0026) ROI Name                            LO: 'spaceoar'
        #   (3006, 0036) ROI Generation Algorithm            CS: 'MANUAL'
        '/vagrant/ucla-140/rtst/2.16.840.1.114362.1.11775105.22699029554.543997669.1030.3153.dcm',
        # '/vagrant/ucla-140/rtdose/2.16.840.1.114362.1.11775105.22699029554.543997671.684.3155.dcm',
        # '/vagrant/ucla-140/rtplan/2.16.840.1.114362.1.11775105.22699029554.543997669.1026.3146.dcm',
    ]
    coh_001 = [
        # '/vagrant/coh-001/mr/MR.1.2.840.113619.2.312.4120.8419387.12268.1570466843.312.dcm',
        # '/vagrant/coh-001/ct/1.2.840.113619.2.55.3.1678399520.770.1570458748.195.1.dcm',
        # '/vagrant/coh-001/re/RE.1.2.246.352.205.4966208310047637890.17210857757822690998.dcm',
        '/vagrant/coh-001/rtst/RS.1.2.246.352.205.4827533863638583198.10720857379728702625.dcm',
        # '/vagrant/coh-001/rtdose/RD.1.2.246.352.210.5759530306837972759.9703294823693431997.dcm',
    ]
    # for n in ucla_140:
    for n in coh_001:
        print(pydicom.dcmread(n))
    #     r = pydicom.dcmread(n)[0x3006,0x0020]
    #     for e in r:
    #         pkdp('{}', e[0x3006,0x0026].value)
