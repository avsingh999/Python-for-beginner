def insertionsort(seq):
	for sliceEnd in range(len(seq)):
		# Build longer and longer sorted slices in each iteration
		# seq[0:sliceEnd] already sorted
		# move first element after sorted slice left till is in the correcr place

		pos = sliceEnd

		while pos > 0 and seq[pos] < seq[pos-1]:
			(seq[pos],seq[pos-1]) = (seq[pos-1].seq[pos])
			pos = pos-1
	return seq