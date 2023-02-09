#---------------------------------------------------------------------
# Copyright: CNRS - Universite Grenoble Alpes
#
# Contributors : Jean-Michel Brankart
#
# Jean-Michel.Brankart@univ-grenoble-alpes.fr
#
# This software is governed by the CeCILL license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
#---------------------------------------------------------------------
"""
EnsDAM: Ensamble Data Assimilation modules

Available modules:
    ensdam.ensanam : ensemble anamorphosis transformation
    ensdam.ensaugm : ensemble augmentation
    ensdam.ensscores : ensemble scores
    ensdam.ensstat : ensemble statistics
    ensdam.ensupdate : ensemble observational update
    ensdam.interptools : interpolation tools
    ensdam.obserror : observation error
    ensdam.stochtools : stochastic tools
    ensdam.transpho : scale separation (by projection on the spherical harmonics)
"""
import numpy as np
import pyensdam

class ensscores:
    """
    The purpose of EnsScores is to provide tools
    to compute probabilistic scores of ensemble simulations.
    The scores evaluates the reliability, resolution and optimality
    of the simulation by comparison to verification data.

    Available variables:
    crps_missing_value,mpi_comm_score_crps,mpi_comm_score_rcrv,
    rcrv_number_of_quantiles,rcrv_with_anamorphosis,rcrv_missing_value,
    mpi_comm_score_entropy,score_entropy_base

    Available functions:
    compute_ranks(),crps_score(),crps_cumul(),crps_final(), rcrv_score(),rcrv_cumul(),
    optimality_score(),optimality_cumul(),events_score(),events_relative_entropy(),
    events_cross_entropy(),events_entropy(),events_probability()
    """

    @staticmethod
    def compute_ranks(ens,verif):
        """
        ranks,rank_histogram = compute_ranks(ens,verif)

        Compute ranks and rank histogram

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        verif : input rank-1 array('d') with bounds (size(ens,1))

        Returns
        -------
        ranks : rank-1 array('d') with bounds (f2py_crps_d0)
        rank_histogram : rank-1 array('d')
        """

        # Apply requested function
        api_ens = _iarraydouble(ens)
        api_verif = _iarraydouble(verif)
        ranks,rank_histogram = score_ranks.ensdam_score_ranks.compute_ranks(api_ens,api_verif)

        return ranks,rank_histogram

    @staticmethod
    def crps_score(ens,verif,partition=()):
        """
        crps,reliability,resolution = crps_score(ens,verif,partition)

        Compute CRPS score (with option to partition the data)

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        verif : input rank-1 array('d') with bounds (size(ens,1))
        partition : input rank-1 array('i') with bounds (size(ens,1))

        Returns
        -------
        crps : rank-1 array('d') with bounds (f2py_crps_d0)
        reliability : rank-1 array('d') with bounds (size(crps,1))
        resolution : rank-1 array('d') with bounds (size(crps,1))
        """
        # Update module public variables
        score_crps.ensdam_score_crps.crps_missing_value = crps_missing_value
        if mpi:
            score_crps.ensdam_score_crps.mpi_comm_score_crps = mpi_comm_score_crps

        # Apply requested function
        if partition == ():
            api_ens = _iarraydouble(ens)
            api_verif = _iarraydouble(verif)
            crps,reliability,resolution =  score_crps.ensdam_score_crps.crps_score_global(api_ens,api_verif)
        else:
            api_ens = _iarraydouble(ens)
            api_verif = _iarraydouble(verif)
            api_parttion = _iarraydouble(parttion)
            crps,reliability,resolution =  score_crps.ensdam_score_crps.crps_score_partition(api_ens,api_verif,api_parttion)

        return crps,reliability,resolution

    @staticmethod
    def crps_cumul(ens,a,aa,bb):
        """
        crps_cumul(ens,a,aa,bb)

        Accumulate data to prepare the final computation of the score

        Parameters
        ----------
        ens : input rank-1 array('d') with bounds (f2py_ens_d0)
        a : input float
        aa : in/output rank-1 array('d') with bounds (1)
        bb : in/output rank-1 array('d') with bounds (1)
        """
        # Update module public variables
        score_crps.ensdam_score_crps.crps_missing_value = crps_missing_value
        if mpi:
            score_crps.ensdam_score_crps.mpi_comm_score_crps = mpi_comm_score_crps

    @staticmethod
    def crps_final(aa,bb):
        """
        reli,resol,crps = crps_final(aa,bb)

        Compute final score from accumulated data

        Parameters
        ----------
        aa : in/output rank-1 array('d') with bounds (1)
        bb : in/output rank-1 array('d') with bounds (1)

        Returns
        -------
        reli : float
        resol : float
        crps : float
        """
        # Update module public variables
        score_crps.ensdam_score_crps.crps_missing_value = crps_missing_value
        if mpi:
            score_crps.ensdam_score_crps.mpi_comm_score_crps = mpi_comm_score_crps

    @staticmethod
    def rcrv_score(ens,verif,partition=()):
        """
        ens_bias,ens_spread = rcrv_score_partition(ens,verif,partition)

        Compute RCRV score (with option to partition the data)

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        verif : input rank-1 array('d') with bounds (size(ens,1))
        partition : input rank-1 array('i') with bounds (size(ens,1))

        Returns
        -------
        ens_bias : rank-1 array('d') with bounds (f2py_ens_bias_d0)
        ens_spread : rank-1 array('d') with bounds (size(ens_bias,1))
        """
        # Update module public variables
        score_rcrv.ensdam_score_rcrv.rcrv_number_of_quantiles = rcrv_number_of_quantiles
        score_rcrv.ensdam_score_rcrv.rcrv_with_anamorphosis = rcrv_with_anamorphosis
        score_rcrv.ensdam_score_rcrv.rcrv_missing_value = rcrv_missing_value
        if mpi:
            score_rcrv.ensdam_score_rcrv.mpi_comm_score_rcrv = mpi_comm_score_rcrv

        # Apply requested function
        if partition == ():
            api_ens = _iarraydouble(ens)
            api_verif = _iarraydouble(verif)
            ens_bias,ens_spread =  score_rcrv.ensdam_score_rcrv.rcrv_score_global(api_ens,api_verif)
        else:
            api_ens = _iarraydouble(ens)
            api_verif = _iarraydouble(verif)
            api_parttion = _iarraydouble(parttion)
            ens_bias,ens_spread =  score_rcrv.ensdam_score_rcrv.rcrv_score_partition(api_ens,api_verif,api_parttion)

        return ens_bias,ens_spread

    @staticmethod
    def rcrv_cumul(e,a,idx,mean,sqrs):
        """
        rcrv_cumul(e,a,idx,mean,sqrs)

        Accumulate data to prepare the final computation of the score

        Parameters
        ----------
        e : input rank-1 array('d') with bounds (f2py_e_d0)
        a : input float
        idx : input int
        mean : in/output rank-0 array(float,'d')
        sqrs : in/output rank-0 array(float,'d')
        """
        # Update module public variables
        score_rcrv.ensdam_score_rcrv.rcrv_number_of_quantiles = rcrv_number_of_quantiles
        score_rcrv.ensdam_score_rcrv.rcrv_with_anamorphosis = rcrv_with_anamorphosis
        score_rcrv.ensdam_score_rcrv.rcrv_missing_value = rcrv_missing_value
        if mpi:
            score_rcrv.ensdam_score_rcrv.mpi_comm_score_rcrv = mpi_comm_score_rcrv

    @staticmethod
    def optimality_score(ens,obs,cdf_obs,cdf_obs_extra_args=(),partition=()):
        """
        ens_optimality,ens_optimality_bias,ens_optimality_spread = optimality_score(ens,obs,cdf_obs,[cdf_obs_extra_args,partition])

        Compute optimality score (with option to partition the data)

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        obs : input rank-1 array('d') with bounds (f2py_obs_d0)
        cdf_obs : call-back function => callback_cdf_obs

        Other Parameters
        ----------------
        cdf_obs_extra_args : input tuple, optional
            Default: ()
        partition : input rank-1 array('i') with bounds (f2py_partition_d0)

        Returns
        -------
        ens_optimality : rank-1 array('d') with bounds (f2py_ens_optimality_d0)
        ens_optimality_bias : rank-1 array('d') with bounds (f2py_ens_optimality_bias_d0)
        ens_optimality_spread : rank-1 array('d') with bounds (f2py_ens_optimality_spread_d0)

        Notes
        -----
        Call-back functions::

          def callback_cdf_obs(o,y,obs_idx): return callback_cdf_obs
          Required arguments:
            o : input float
            y : input float
            obs_idx : input int
          Return objects:
            callback_cdf_obs : float
        """

    @staticmethod
    def optimality_cumul(e,o,idx,mean,sqrs,cdf_obs,cdf_obs_extra_args=()):
        """
        optimality_cumul(e,o,idx,mean,sqrs,cdf_obs,[cdf_obs_extra_args])

        Accumulate data to prepare the final computation of the score

        Parameters
        ----------
        e : input rank-1 array('d') with bounds (f2py_e_d0)
        o : input float
        idx : input int
        mean : in/output rank-0 array(float,'d')
        sqrs : in/output rank-0 array(float,'d')
        cdf_obs : call-back function => callback_cdf_obs

        Other Parameters
        ----------------
        cdf_obs_extra_args : input tuple, optional
            Default: ()

        Notes
        -----
        Call-back functions::

          def callback_cdf_obs(o,y,obs_idx): return callback_cdf_obs
          Required arguments:
            o : input float
            y : input float
            obs_idx : input int
          Return objects:
            callback_cdf_obs : float
        """

    @staticmethod
    def events_score(ens,pref,events_outcome,events_outcome_extra_args=()):
        """
        score = events_score(ens,pref,events_outcome,[events_outcome_extra_args])

        Compute ensemble score for the required events

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        pref : input rank-2 array('d') with bounds (f2py_pref_d0,f2py_pref_d1)
        events_outcome : call-back function

        Other Parameters
        ----------------
        events_outcome_extra_args : input tuple, optional
            Default: ()

        Returns
        -------
        score : rank-1 array('d') with bounds (f2py_score_d0)

        Notes
        -----
        Call-back functions::

          def events_outcome(member): return outcome
          Required arguments:
            member : input rank-1 array('d') with bounds (:)
          Return objects:
            outcome : rank-1 array('i') with bounds (:)
        """
        # Update module public variables
        score_entropy.ensdam_score_entropy.score_entropy_base = score_entropy_base
        if mpi:
            score_entropy.ensdam_score_entropy.mpi_comm_score_entropy = mpi_comm_score_entropy

    @staticmethod
    def events_relative_entropy(ens,pref,events_outcome,events_outcome_extra_args=()):
        """
        relative_entropy = events_relative_entropy(ens,pref,events_outcome,[events_outcome_extra_args])

        Compute relative entropy between ensemble distribution and reference distribution

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        pref : input rank-2 array('d') with bounds (f2py_pref_d0,f2py_pref_d1)
        events_outcome : call-back function

        Other Parameters
        ----------------
        events_outcome_extra_args : input tuple, optional
            Default: ()

        Returns
        -------
        relative_entropy : rank-1 array('d') with bounds (f2py_relative_entropy_d0)

        Notes
        -----
        Call-back functions::

          def events_outcome(member): return outcome
          Required arguments:
            member : input rank-1 array('d') with bounds (:)
          Return objects:
            outcome : rank-1 array('i') with bounds (:)
        """
        # Update module public variables
        score_entropy.ensdam_score_entropy.score_entropy_base = score_entropy_base
        if mpi:
            score_entropy.ensdam_score_entropy.mpi_comm_score_entropy = mpi_comm_score_entropy

    @staticmethod
    def events_cross_entropy(ens,pref,events_outcome,events_outcome_extra_args=()):
        """
        cross_entropy,entropy = events_cross_entropy(ens,pref,events_outcome,[events_outcome_extra_args])

        Compute cross entropy between ensemble distribution and reference distribution

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        pref : input rank-2 array('d') with bounds (f2py_pref_d0,f2py_pref_d1)
        events_outcome : call-back function

        Other Parameters
        ----------------
        events_outcome_extra_args : input tuple, optional
            Default: ()

        Returns
        -------
        cross_entropy : rank-1 array('d') with bounds (f2py_cross_entropy_d0)
        entropy : rank-1 array('d') with bounds (f2py_entropy_d0)

        Notes
        -----
        Call-back functions::

          def events_outcome(member): return outcome
          Required arguments:
            member : input rank-1 array('d') with bounds (:)
          Return objects:
            outcome : rank-1 array('i') with bounds (:)
        """
        # Update module public variables
        score_entropy.ensdam_score_entropy.score_entropy_base = score_entropy_base
        if mpi:
            score_entropy.ensdam_score_entropy.mpi_comm_score_entropy = mpi_comm_score_entropy

    @staticmethod
    def events_entropy(ens,events_outcome,number_outcome,events_outcome_extra_args=()):
        """
        entropy = events_entropy(ens,events_outcome,number_outcome,[events_outcome_extra_args])

        Compute entropy of ensemble distribution for the required events

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        events_outcome : call-back function
        number_outcome : input int

        Other Parameters
        ----------------
        events_outcome_extra_args : input tuple, optional
            Default: ()

        Returns
        -------
        entropy : rank-1 array('d') with bounds (f2py_entropy_d0)

        Notes
        -----
        Call-back functions::

          def events_outcome(member): return outcome
          Required arguments:
            member : input rank-1 array('d') with bounds (:)
          Return objects:
            outcome : rank-1 array('i') with bounds (:)
        """
        # Update module public variables
        score_entropy.ensdam_score_entropy.score_entropy_base = score_entropy_base
        if mpi:
            score_entropy.ensdam_score_entropy.mpi_comm_score_entropy = mpi_comm_score_entropy

    @staticmethod
    def events_probability(ens,events_outcome,events_outcome_extra_args=()):
        """
        pens = events_probability(ens,events_outcome,[events_outcome_extra_args])

        Compute events marginal probability distributions from the ensemble

        Parameters
        ----------
        ens : input rank-2 array('d') with bounds (f2py_ens_d0,f2py_ens_d1)
        events_outcome : call-back function

        Other Parameters
        ----------------
        events_outcome_extra_args : input tuple, optional
            Default: ()

        Returns
        -------
        pens : rank-2 array('d') with bounds (f2py_pens_d0,f2py_pens_d1)

        Notes
        -----
        Call-back functions::

          def events_outcome(member): return outcome
          Required arguments:
            member : input rank-1 array('d') with bounds (:)
          Return objects:
            outcome : rank-1 array('i') with bounds (:)
        """
        # Update module public variables
        score_entropy.ensdam_score_entropy.score_entropy_base = score_entropy_base
        if mpi:
            score_entropy.ensdam_score_entropy.mpi_comm_score_entropy = mpi_comm_score_entropy

