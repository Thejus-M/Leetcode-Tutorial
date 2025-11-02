from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.s =defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        arr=self.s.get(key,[])

        l,r=0,len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m][1]==timestamp:
                return arr[m][0]
            elif arr[m][1]<timestamp:
                res=arr[m][0]
                l=m+1
            else:
                r=m-1
        return res

        

if __name__ == "__main__":
    inputs = [
        (["TimeMap","set","set","get","get","get","get","get"], [[],["foo","bar",1],["foo","bar2",4],["foo",1],["foo",3],["foo",4],["foo",5],["baz",1]], [None,None,None,"bar","bar","bar2","bar2",""]),
    ]
    
    for methods, params, expected in inputs:
        obj = None
        results = []
        for method, param, exp in zip(methods, params, expected):
            if method == "TimeMap":
                obj = TimeMap()
                results.append(None)
            elif method == "set":
                result = obj.set(*param)
                results.append(result)
            elif method == "get":
                result = obj.get(*param)
                results.append(result)
        
        status = "✅ Correct" if results == expected else "❌ Incorrect"
        print(f"Methods: {methods}\nParams: {params}\nExpected: {expected}\nResults: {results}\nStatus: {status}\n")
        assert results == expected, f"expected {expected}, but got {results}"