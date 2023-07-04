Program main
  Implicit None
  INTEGER :: A, B, C
  CHARACTER(len=100) :: S

  READ(*, *) A
  READ(*, *) B, C
  READ(*, *) S

  WRITE(*, *) A + B + C, S

END Program main