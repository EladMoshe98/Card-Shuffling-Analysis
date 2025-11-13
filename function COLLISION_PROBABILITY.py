function COLLISION_PROBABILITY(p_cut, p_start, p_run):
    total ← 0
    for each K in support(p_cut):
        for each S in {L, R}:
            w ← (p_cut[K])^2 * (p_start[S])^2
            F ← F_HUMAN(K, 52 - K, S, p_run)
            total ← total + w * F
    return total

# Probability that TWO independent shuffles match in clump sequence
# given cut (L_rem, R_rem) and starting side S.
function F_HUMAN(L_rem, R_rem, S, p_run):
    memo ← empty_map()
    return MATCH_PROB(L_rem, R_rem, S, memo, p_run)

function MATCH_PROB(L_rem, R_rem, turn, memo, p_run):
    # Base cases
    if L_rem == 0 and R_rem == 0:
        return 1.0                      # both piles exactly exhausted, sequences matched
    if L_rem < 0 or R_rem < 0:
        return 0.0                      # infeasible path

    key ← (L_rem, R_rem, turn)
    if key in memo: return memo[key]

    # Determine allowed clump sizes for the current hand
    if turn == 'L':
        max_allowed ← min(5, L_rem)
        # If the right pile is empty, the rest must be dropped from the left in one final clump
        if R_rem == 0: allowed ← { L_rem }       # exact finish
        else:           allowed ← {1,2,3,4,5} ∩ {1..max_allowed}
    else:  # turn == 'R'
        max_allowed ← min(5, R_rem)
        if L_rem == 0: allowed ← { R_rem }
        else:           allowed ← {1,2,3,4,5} ∩ {1..max_allowed}

    prob ← 0.0
    for each t in allowed:
        step_match ← (p_run[t])^2                 # both choose the same clump size t
        if turn == 'L':
            prob ← prob + step_match * MATCH_PROB(L_rem - t, R_rem, 'R', memo, p_run)
        else:
            prob ← prob + step_match * MATCH_PROB(L_rem, R_rem - t, 'L', memo, p_run)

    memo[key] ← prob
    return prob
