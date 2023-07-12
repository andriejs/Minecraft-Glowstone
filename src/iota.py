iota_counter = 0

def iota(reset: bool = False):
    global iota_counter
	iota_counter += 1
    if reset:
        iota_counter = 0
    return iota_counter