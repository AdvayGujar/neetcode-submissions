class Solution:
    def volume(self, height1, height2, breadth):
        if height1 <= height2:
            return height1 * breadth
        else:
            return height2 * breadth

    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        fP = 0
        rP = len(height)-1
        isRunning = True

        while isRunning:
            tempVol = self.volume(height[fP],height[rP],int(rP-fP))
            if tempVol > maxVol:
                maxVol = tempVol
            
            if height[fP] < height[rP]:
                fP += 1
            else:
                rP -= 1

            if fP == rP:
                isRunning = False
        
        return maxVol