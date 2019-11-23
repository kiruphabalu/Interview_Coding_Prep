class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        length = len(A)
        maj = math.floor(length/2)
        maj_dict = {}
        for element in A:
            if element in maj_dict.keys():
                maj_dict[element] +=1
            else:
                maj_dict[element] = 1

        for key in maj_dict:
            if maj_dict[key] > maj:
                return key
