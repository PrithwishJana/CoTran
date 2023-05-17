class Test:
    @staticmethod
    def countDistictSubarray(arr, n):
        vis = HashMapAnonymousInnerClass()
        for i in range(0, n):
            vis[arr [i]] = 1
        k = len(vis)
        vis.clear()
        ans = 0
        right = 0
        window = 0
        for left in range(0, n):
            while right < n and window < k:
                vis[arr [right]] = vis[arr [right]] + 1
                if vis[arr [right]] == 1:
                    window += 1
                right += 1
            if window == k:
                ans += (n - right + 1)
            vis[arr [left]] = vis[arr [left]] - 1
            if vis[arr [left]] == 0:
                window -= 1
        return ans

    class HashMapAnonymousInnerClass(dict):
        def get(self, key):
            if not self.containsKey(key):
                return 0
            return super().get(key)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 1, 3, 2, 3]
        print(Test.countDistictSubarray(arr, len(arr)))
