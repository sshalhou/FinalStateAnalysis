import FWCore.ParameterSet.Config as cms
from FinalStateAnalysis.Utilities.version import cmssw_major_version

customizePhotonSequence = cms.Sequence()

#prescription for calculating the photon PF isolation
#embeds per-vertex isolation information
from FinalStateAnalysis.PatTools.photons.patPhotonPFIsolationEmbedding_cfi import \
        patPhotonPFIsolation

customizePhotonSequence += patPhotonPFIsolation

# rhos for the photon ID
from FinalStateAnalysis.PatTools.photons.patPhotonRhoEmbedding_cfi import \
     patPhotonRhoEmbedder

customizePhotonSequence += patPhotonRhoEmbedder

from FinalStateAnalysis.PatTools.photons.patPhotonEAEmbedder_cfi import \
     patPhotonEAEmbedder

customizePhotonSequence += patPhotonEAEmbedder

# calculated photon ID
from FinalStateAnalysis.PatTools.photons.patPhotonCutBasedIdEmbedding_cfi import \
     patPhotonCutBasedIdEmbedder

customizePhotonSequence += patPhotonCutBasedIdEmbedder
