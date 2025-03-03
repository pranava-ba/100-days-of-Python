class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        r=[]
        m=[]
        for i in nums:
            if (i<pivot):
                l.append(i)
            elif (i>pivot):
                r.append(i)
            else:
                m.append(i)
        x=l+m+r
        return x

