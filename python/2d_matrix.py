class Solution:
	def maxAreaHist(self,hist):
		maxArea = 0
		stack = [-1]
		top = 0
		i = 0
		while i < len(hist):
			if stack[-1] == -1 or hist[i] > hist[stack[-1]]:
				stack.append(i)
				i+=1
			else:
				top = stack.pop()
				maxArea = max(maxArea,hist[top]*(i-1-stack[-1]))
		while stack[-1]!=-1:
			top = stack.pop()
			maxArea = max(maxArea,hist[top]*(i-1-stack[-1]))
		return maxArea
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
		maxArea = self.maxAreaHist(A[0])
		for i in xrange(1,len(A)):
			for j in xrange(len(A[0])):
				if A[i][j] == 1:
					A[i][j]+= A[i-1][j]
			maxArea = max(maxArea,self.maxAreaHist(A[i]))
		return maxArea
