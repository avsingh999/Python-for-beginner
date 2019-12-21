
	def insertionsort(seq):
		for sliceEnd in range(len(seq)):
			# 각 반복마다 길고 긴 정렬 된 슬라이스를 만듭니다.
			# seq [0 : sliceEnd]이 (가) 이미 정렬되었습니다
			# 정렬된 슬라이스를 왼쪽으로 정렬한 후 첫번째 요소를 올바른 위치에 놓을때까지 이동
			pos = sliceEnd
			while pos > 0 and seq[pos] < seq[pos-1]:
				(seq[pos],seq[pos-1]) = (seq[pos-1].seq[pos])
				pos = pos-1
		return seq
