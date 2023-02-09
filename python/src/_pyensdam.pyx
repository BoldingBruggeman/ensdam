# cython: language_level=3
# cython: profile=True

cimport cython
import tempfile
import atexit
import os

cimport numpy
import numpy
cdef extern void c_crps_score_global(int nstate, int nens, double* crps, double* reliability, double* resolution, double* ens, double* verif) nogil

def crps_score_global(crps not None, reliability, resolution, ens not None, verif not None):
    cdef double crps_ = crps
    cdef double reliability_ = reliability
    cdef double resolution_ = resolution
    cdef double[:,::1] ens_ = ens
    cdef double[::1] verif_ = verif
    c_crps_score_global(<int>ens_.shape[0], <int>ens_.shape[1], &crps_, &reliability_, &resolution_, &ens_[0][0], &verif_[0])


#def crps_score_global(double crps, double reliability, double resolution, double[:,::1] ens not None, const double[::1] verif not None):
#    c_crps_score_global(<int>ens.shape[0], <int>ens.shape[1], &crps, &reliability, &resolution, &ens[0][0], &verif[0])


# https://cython.readthedocs.io/en/stable/src/userguide/memoryviews.html#coercion-to-numpy
#    cdef double[::1] arr_memview = arr
#    multiply_by_10_in_C(&arr_memview[0], arr_memview.shape[0])
    

