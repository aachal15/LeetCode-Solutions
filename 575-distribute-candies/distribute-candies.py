class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ln = len(candyType) // 2
        type_candy = len(set(candyType))
        if type_candy >= ln:
            return ln
        return type_candy