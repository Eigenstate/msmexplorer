"""
Free Energy Plot (Univariate)
=============================
"""
from msmbuilder.featurizer import DihedralFeaturizer
from msmbuilder.decomposition import tICA
from msmbuilder.cluster import MiniBatchKMeans
from msmbuilder.msm import MarkovStateModel

import numpy as np

import msmexplorer as msme
from msmexplorer.example_datasets import FsPeptide

rs = np.random.RandomState(42)

# Load Fs Peptide Data
trajs = FsPeptide().get().trajectories

# Extract Backbone Dihedrals
featurizer = DihedralFeaturizer(types=['phi', 'psi'])
diheds = featurizer.fit_transform(trajs)

# Perform Dimensionality Reduction
tica_model = tICA(lag_time=2, n_components=2)
tica_trajs = tica_model.fit_transform(diheds)

# Perform Clustering
clusterer = MiniBatchKMeans(n_clusters=12, random_state=rs)
clustered_trajs = clusterer.fit_transform(tica_trajs)

# Construct MSM
msm = MarkovStateModel(lag_time=2)
assignments = msm.fit_transform(clustered_trajs)

# Plot Free Energy
data = np.concatenate(tica_trajs, axis=0)
pi_0 = msm.populations_[np.concatenate(assignments, axis=0)]
msme.plot_free_energy(data, n_samples=100000, pi=pi_0,
                      gridsize=100, random_state=rs)
