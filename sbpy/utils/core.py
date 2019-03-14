# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
sbpy utils module

created on March 12, 2019

"""

__all__ = ['get_bandpass']

import os
from astropy.utils.data import get_pkg_data_filename


def get_bandpass(name):
    """Get filter bandpass from sbpy's internal data.

    A convenience method for use in sbpy's tests.  Requires
    `~synphot`.


    Parameters
    ----------
    name : string
        Name of the bandpass, case insensitive.  See notes for
        available filters.


    Returns
    -------
    bp : `~synphot.SpectralElement`


    Notes
    -----
    Available filters:

    +-----------+---------------------------+
    | Name      | Source                    |
    +===========+===========================+
    | F438W     | HST/WFC3 UVIS, v4 [1]_    |
    +-----------+---------------------------+
    | F606W     | HST/WFC3 UVIS, v4 [1]_    |
    +-----------+---------------------------+
    | Cousins I | STScI CDBS, v4 [1]_       |
    +-----------+---------------------------+
    | SDSS u    | SDSS, dated 2001 [2]_     |
    +-----------+---------------------------+
    | SDSS g    | SDSS, dated 2001 [2]_     |
    +-----------+---------------------------+
    | SDSS r    | SDSS, dated 2001 [2]_     |
    +-----------+---------------------------+
    | SDSS i    | SDSS, dated 2001 [2]_     |
    +-----------+---------------------------+
    | SDSS z    | SDSS, dated 2001 [2]_     |
    +-----------+---------------------------+


    References
    ----------
    .. [1] Space Telescope Science Institute.  Calibration Database
       System.  http://www.stsci.edu/hst/observatory/cdbs .

    .. [2] Sloan Digital Sky Survey.  Camera.
       https://www.sdss.org/instruments/camera

    """

    try:
        import synphot
    except ImportError:
        raise ImportError('synphot is required.')

    name2file = {
        'f438w': 'wfc3_uvis_f438w_004_syn.fits',
        'f606w': 'wfc3_uvis_f606w_004_syn.fits',
        'cousins i': 'cousins_i_004_syn.fits',
        'sdss u': 'sdss-u.fits',
        'sdss g': 'sdss-g.fits',
        'sdss r': 'sdss-r.fits',
        'sdss i': 'sdss-i.fits',
        'sdss z': 'sdss-z.fits',
    }

    fn = get_pkg_data_filename(os.path.join(
        '..', 'photometry', 'data', name2file[name.lower()]))
    bp = synphot.SpectralElement.from_file(fn)
    return bp
