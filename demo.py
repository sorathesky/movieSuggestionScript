from lightfm import LightFM as LFM 
from lightfm.datasets import fetch_movielens as fm
from lightfm.evaluation import precision_at_k as ptk

# Loading MovieLens 100k dataset.
# Only five star ratings re treated as positives.
data = fm(min_rating=5.0)

# Instantiating and trainign model
model = LFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)

# Evaluating the training model precision
test_precision = ptk(model, data['test'], k=5).mean()

