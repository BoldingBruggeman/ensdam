# cython: language_level=3
# cython: profile=True

cimport cython
import tempfile
import atexit
import os

cimport numpy
import numpy
cdef extern void c_crps_score_global(int nstate, int nens, double* crps, double* reliability, double* resolution, double* ens, double* verif) nogil

cdef extern void c_rcrv_score_global(int nstate, int nens, double* ens_bias, double* ens_spread, double* ens, double* verif) nogil

cdef extern void c_compute_ranks(int nstate, int nens, double* ens, double* verif, int* ranks) nogil
cdef extern void c_compute_ranks_histogram(int nstate, int nens, double* ens, double* verif, int* ranks, int* rank_histogram) nogil

# From score_crps
#KB crps_missing_value = score_crps.ensdam_score_crps.crps_missing_value

def crps_score_global(ens not None, verif not None):
    cdef double[:,::1] ens_ = ens
    cdef double[::1] verif_ = verif

    cdef double crps
    cdef double reliability
    cdef double resolution

    c_crps_score_global(<int>ens_.shape[0], <int>ens_.shape[1], &crps, &reliability, &resolution, &ens_[0][0], &verif_[0])
    return crps, reliability, resolution

def rcrv_score_global(ens not None, verif not None):
    cdef double[:,::1] ens_ = ens
    cdef double[::1] verif_ = verif

    cdef double ens_bias
    cdef double ens_spread

    c_rcrv_score_global(<int>ens_.shape[0], <int>ens_.shape[1], &ens_bias, &ens_spread, &ens_[0][0], &verif_[0])
    return ens_bias, ens_spread

def compute_ranks(ens not None, verif not None, histogram=False):
    cdef double[:,::1] ens_ = ens
    cdef double[::1] verif_ = verif

    ranks = numpy.zeros((<int>ens_.shape[0]), dtype=numpy.intc)
    cdef int[::1] ranks_ = ranks

    rank_histogram = numpy.zeros((<int>ens_.shape[1]+1), dtype=numpy.intc)
    cdef int[::1] rank_histogram_ = rank_histogram

    if histogram:
        c_compute_ranks_histogram(<int>ens_.shape[0], <int>ens_.shape[1], &ens_[0][0], &verif_[0], &ranks_[0], &rank_histogram_[0])
        return ranks, rank_histogram
    else:
        c_compute_ranks(<int>ens_.shape[0], <int>ens_.shape[1], &ens_[0][0], &verif_[0], &ranks_[0])
        return ranks


# https://cython.readthedocs.io/en/stable/src/userguide/memoryviews.html#coercion-to-numpy
#    cdef double[::1] arr_memview = arr
#    multiply_by_10_in_C(&arr_memview[0], arr_memview.shape[0])
    
