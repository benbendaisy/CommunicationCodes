class Codec:
    def __init__(self):
        self.cacheStore = {}
        self.cnt = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.cacheStore[str(self.cnt)] = longUrl
        self.cnt += 1
        return str(self.cnt - 1)


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.cacheStore.get(shortUrl)


if __name__ == "__main__":
    url = "https://leetcode.com/problems/design-tinyurl"
    codec = Codec()
    ret = codec.decode(codec.encode(url))
    print(ret)