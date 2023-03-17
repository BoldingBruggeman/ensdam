module ensscore

use iso_c_binding, only: c_ptr, c_int, c_double, c_char, c_loc, c_f_pointer, C_NULL_CHAR, C_NULL_PTR

use ensdam_score_crps
use ensdam_score_rcrv
use ensdam_score_ranks

implicit none

contains

subroutine c_crps_score_global(nstate, nens, crps, reliability, resolution, ens, verif) bind(c)
   integer(c_int), intent(in), value :: nstate
   integer(c_int), intent(in), value :: nens
   real(c_double), intent(out) :: crps
   real(c_double), intent(out) :: reliability
   real(c_double), intent(out) :: resolution
   real(c_double), intent(in) :: ens(nstate,nens)
   real(c_double), intent(in) :: verif(nstate)

   call crps_score_global(crps, reliability, resolution, ens, verif)
end subroutine

#if 0
subroutine c_crps_score_partition(nstate, nens, crps, reliability, resolution, ens, verif, partition) bind(c)
   integer(c_int), intent(in), value :: nstate
   integer(c_int), intent(in), value :: nens
   real(c_double), intent(out) :: crps
   real(c_double), intent(out) :: reliability
   real(c_double), intent(out) :: resolution
   real(c_double), intent(in) :: ens(nstate,nens)
   real(c_double), intent(in) :: verif(nstate)
   integer(c_int), intent(in) :: partition

!   call crps_score_partition(crps, reliability, resolution, ens, verif, partition)
end subroutine
#endif

subroutine c_rcrv_score_global(nstate, nens, ens_bias, ens_spread, ens, verif) bind(c)
   integer(c_int), intent(in), value :: nstate
   integer(c_int), intent(in), value :: nens
   real(c_double), intent(out) :: ens_bias
   real(c_double), intent(out) :: ens_spread
   real(c_double), intent(in) :: ens(nstate,nens)
   real(c_double), intent(in) :: verif(nstate)

   call rcrv_score_global(ens_bias, ens_spread, ens, verif)
end subroutine

subroutine c_compute_ranks(nstate, nens, ens, verif, ranks) bind(c)
   integer(c_int), intent(in), value :: nstate
   integer(c_int), intent(in), value :: nens
   real(c_double), intent(in) :: ens(nstate,nens)
   real(c_double), intent(in) :: verif(nstate)
   integer(c_int), intent(out) :: ranks(nstate)
!   integer(c_int), intent(out) :: rank_histogram(nens+1)

   call compute_ranks(ens, verif, ranks)
end subroutine

subroutine c_compute_ranks_histogram(nstate, nens, ens, verif, ranks, rank_histogram) bind(c)
   integer(c_int), intent(in), value :: nstate
   integer(c_int), intent(in), value :: nens
   real(c_double), intent(in) :: ens(nstate,nens)
   real(c_double), intent(in) :: verif(nstate)
   integer(c_int), intent(out) :: ranks(nstate)
   integer(c_int), intent(out) :: rank_histogram(nens+1)

   call compute_ranks(ens, verif, ranks, rank_histogram)
end subroutine

end module
