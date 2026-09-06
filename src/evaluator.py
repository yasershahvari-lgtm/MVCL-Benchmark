class DetectionEvaluator:
    def evaluate(self, ground_truth_count: int, tp: int, fp: int, fn: int):
        precision = tp / (tp + fp) if (tp + fp) else 1.0
        recall = tp / (tp + fn) if (tp + fn) else 1.0
        f1 = 2*precision*recall/(precision+recall) if (precision+recall) else 0.0
        return {"tp":tp,"fp":fp,"fn":fn,"precision":precision,"recall":recall,"f1":f1}
