class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        ires = {}
        output = []

        for num in nums:
            ires[num] = 1 + ires.get(num, 0)

        for num,cnt in ires.items():
            freq[cnt].append(num)

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                output.append(num)
                if len(output)==k:
                    return output

        # for i in range(len(freq)-1,0,-1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
            
            

        



























        # freq = [[] for i in range(len(nums)+1)]
        # count = {}

        # for num in nums:
        #     count[num] = 1 + count.get(num,0)
        
        # for num,cnt in count.items():
        #     freq[cnt].append(num)

        # res = []
        # for i in range(len(freq)-1,0,-1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res