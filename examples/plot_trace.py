"""
Trace Plot
==========
"""
from msmbuilder.featurizer import RMSDFeaturizer

import msmexplorer as msme
from msmexplorer.example_datasets import FsPeptide

# Load Fs Peptide Data
traj = FsPeptide().get().trajectories[0]

# Calculate RMSD
featurizer = RMSDFeaturizer(reference_traj=traj[0])
rmsd = featurizer.partial_transform(traj).flatten()

# Plot Trace
msme.plot_trace(rmsd, label='traj0', xlabel='Timestep', ylabel='RMSD (nm)')
