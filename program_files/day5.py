class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            match i:
                case "--X":
                    x-=1
                case "X--":
                    x-=1
                case "++X":
                    x+=1
                case "X++":
                    x+=1
        return x
