class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalList = []
        nums1Length = len(nums1)
        nums2Length = len(nums2)

        nums1Pointer = 0
        nums2Pointer = 0

        # Iterate through the combined total number of elements
        for x in range(nums1Length + nums2Length):
            # Check bound constraints BEFORE indexing into the lists to avoid IndexError
            if nums1Pointer < nums1Length and (
                nums2Pointer >= nums2Length
                or nums1[nums1Pointer] <= nums2[nums2Pointer]
            ):
                finalList.append(nums1[nums1Pointer])
                nums1Pointer += 1
            else:
                finalList.append(nums2[nums2Pointer])
                nums2Pointer += 1

        finalListLength = len(finalList)

        # Calculate median
        if finalListLength % 2 == 0:
            return (
                finalList[finalListLength // 2 - 1]
                + finalList[finalListLength // 2]
            ) / 2.0
        else:
            # Use integer division (//) to get the exact middle index
            return float(finalList[finalListLength // 2])