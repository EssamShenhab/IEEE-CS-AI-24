class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:

        # Check if count list is empty
        if not count:
            raise ValueError("Input list 'count' is empty.")

        # Check if count list contains integers only
        if not all(isinstance(x, int) for x in count):
            raise TypeError("Input list 'count' must contain integers only.")

        number_list = []
        for i in range(256):
            for _ in range(count[i]):
                number_list.append(i)

        total = sum(number_list)
        length = len(number_list)

        # Calculate minimum value
        min_val = min(number_list)

        # Calculate maximum value
        max_val = max(number_list)

        # Calculate mean
        mean = total / length

        # Calculate median
        sorted_list = sorted(number_list)
        mid = length // 2
        if length % 2 == 0:
            median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
        else:
            median = sorted_list[mid]

        # Calculate mode
        mode_freq = max(count)
        mode_index = count.index(mode_freq)
        mode = mode_index

        return [float(min_val), float(max_val), mean, median, mode]
