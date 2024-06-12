using Printf
N = parse(Int, readline())
A = parse.(Int, split(readline()))
ans = 0 - sum(A)
@printf(stdout, "%d", ans )
