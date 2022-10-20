class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=dict(Counter(words))
        sorted_freq = sorted(freq, key = lambda x: (-freq[x], x))
        return sorted_freq[:k]