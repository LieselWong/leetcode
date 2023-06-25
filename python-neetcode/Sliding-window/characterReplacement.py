def characterReplacement(s: str, k: int) -> int: 
    # pointer l at 0
    l = 0
    # largest variable 
    lar = 0
    alph = {}
    # define r as moving up unless others
    for r in range(len(s)): 
        # add to hash map
        alph[s[r]] = 1 + alph.get(s[r], 0)
        # when this doesn't meet conditions, move left up 
        while (r - 1 + 1) - max(alph.values()) > k: 
            # subtract from hash map
            alph[s[l]] -= 1
            l += 1
        # record largest sequence that meets condition
        res = max(res, r - l + 1)
    return res
        

