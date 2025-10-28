def next_bus_wait(m: int) -> int:
    """Return wait time until next multiple-of-5 minute (0..4)."""
    # TODO: arithmetic only (no loops).
    if m%5 == 0 : 
        print('the bus is availble')
    else : 
        time = m%5
        wait = (5-(m%5))%5
        print('the bus is passed {time}, and u should wait {wait}')
      # Dummy variable
    return wait





def nearest_multiple_of_10(n: int) -> int:
    """Return nearest multiple of 10; ties go upward (toward +∞)."""
    # TODO: use arithmetic and comparisons only.
    if 0 < n[-1] < 4 : 
        n = n - n[-1]
    elif 6 < n[-1] < 9 :

        n = (n+10)-n[-1]
    elif n[-1] == 5 :
        print('the number is halfway')
        n = n + 5 
    return n
     
