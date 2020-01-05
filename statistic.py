from collections import Counter 

class statistic():
    dataSet = []

    def __init__(self, ls):
        self.dataSet = ls

    def get_count(self):
        return len(self.dataSet)

    def get_mean(self):
        n = len(self.dataSet) 
        get_sum = sum(self.dataSet) 
        mean = get_sum/n
        return round(mean, 2)

    def get_median(self):
        n = len(self.dataSet) 
        n_num = sorted(self.dataSet)
        if n % 2 == 0: 
            median1 = n_num[n//2] 
            median2 = n_num[n//2 - 1] 
            median = (median1 + median2)/2
        else: 
            median = n_num[n//2] 
        return median

    def get_mode(self):
        n = len(self.dataSet)
        data = Counter(self.dataSet) 
        get_mode = dict(data) 
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
        
        if len(mode) == n: 
            get_mode = "None"
        else: 
            get_mode = ' '.join(map(str, mode)) 
        return get_mode