class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = list(set(list1) & set(list2))
        print(common)
        result = []
        map = {}
        print(map)
        for item in common:
            val1 = list1.index(item)
            val2 = list2.index(item)
            total = val1 + val2 
            map[item] = total 

        min_val = min(map.values())
        for key,value in map.items():
            if int(value) == min_val:
                result.append(key)
        return result 
