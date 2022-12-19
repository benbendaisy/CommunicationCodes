from collections import defaultdict


class AllOne:

    def __init__(self):
        self.string_dict = defaultdict(int)
        self.bucket_array = []
        self.bucket_num = 10

    def inc(self, key: str) -> None:
        self.string_dict[key] += 1
        bucket, bucket1 = self.string_dict[key] // self.bucket_num, (self.string_dict[key] - 1) // self.bucket_num
        if bucket != bucket1:
            if len(self.bucket_array) < bucket:
                self.bucket_array.append({})
            self.bucket_array[bucket][key] = self.string_dict[key]
            del self.bucket_array[bucket1][key] # del the key from the prev bucket
        else:
            self.bucket_array[bucket1][key] += 1

    def dec(self, key: str) -> None:
        if key not in self.string_dict:
            return None

        self.string_dict[key] -= 1
        if self.string_dict[key] <= 0:
            del self.string_dict[key]
        bucket, bucket1 = self.string_dict[key] // self.bucket_num, (self.string_dict[key] + 1) // self.bucket_num
        if bucket != bucket1:
            if not self.bucket_array[bucket1]:
                self.bucket_array[bucket1] = {}
            self.bucket_array[bucket1][key] = self.string_dict[key]
            del self.bucket_array[bucket][key] # del the key from the prev bucket
        else:
            self.bucket_array[bucket][key] -= 1

    def getMaxKey(self) -> str:
        if not self.bucket_array:
            return None
        return max(self.bucket_array[-1], key=self.bucket_array[-1].get)

    def getMinKey(self) -> str:
        if not self.bucket_array:
            return None
        return min(self.bucket_array[0], key=self.bucket_array[0].get)
