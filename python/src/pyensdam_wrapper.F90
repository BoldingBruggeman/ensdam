module pyensdam

use iso_c_binding, only: c_ptr, c_int, c_double, c_char, c_loc, c_f_pointer, C_NULL_CHAR, C_NULL_PTR

use ensdam_score_crps

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

end module
