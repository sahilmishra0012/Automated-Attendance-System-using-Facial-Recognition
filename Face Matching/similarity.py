from scipy.spatial import distance

def calc_dist(emb1, emb2):
    return distance.euclidean(emb1, emb2)