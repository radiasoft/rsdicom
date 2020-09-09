# -*- coding: utf-8 -*-
"""Process DICOM files.

:copyright: Copyright (c) 2020 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function


def default_command():
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
        '',
        '',
        '',
        '',
        '',
    ]
    print('hello')
    import pdfquery
    pdf = pdfquery.PDFQuery('samplepdf1.pdf')
    pdf.load()
