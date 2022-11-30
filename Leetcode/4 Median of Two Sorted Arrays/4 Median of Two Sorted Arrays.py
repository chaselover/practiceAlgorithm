class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        partitionLength = (len(nums1)+len(nums2)+1)//2
        isEven = (len(nums1)+len(nums2))%2 == 0
        
        start = 0
        end = len(nums1)
        while start <= end:
            nums1Idx = (start+end)//2
            nums2Idx = (partitionLength - nums1Idx)
            
            # Edge Cases - 왼쪽 그룹이 비었으면 -INF값을,
            # 오른쪽 그룹이 비었으면 +INF값을 적용
            maxLeft1 = nums1[nums1Idx-1] if nums1Idx != 0 else -987654321
            minRight1 = nums1[nums1Idx] if nums1Idx != len(nums1) else 987654321
            
            maxLeft2 = nums2[nums2Idx-1] if nums2Idx != 0 else -987654321
            minRight2 = nums2[nums2Idx] if nums2Idx != len(nums2) else 987654321
            
            if maxLeft1 <= minRight2 and maxLeft2 <=  minRight1:
                if isEven:
                    return (max(maxLeft1,maxLeft2)+min(minRight1,minRight2))/2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                end = nums1Idx - 1
            else:
                start = nums1Idx+1