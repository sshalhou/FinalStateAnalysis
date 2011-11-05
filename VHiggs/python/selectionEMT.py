import FWCore.ParameterSet.Config as cms

import FinalStateAnalysis.Selectors.selectors.selectors as selectors
from FinalStateAnalysis.VHiggs.selectionCommon import common
from FinalStateAnalysis.Utilities.PSetTemplate import PSetTemplate

leg1 = {
    'name' : 'Elec', 'getter' :'daughter(0).', 'nicename' : 'Electron',
    'index' : 0,
}
leg2 = {
    'name' : 'Mu', 'getter' :'daughter(1).', 'nicename' : 'Muon',
    'index' : 1,
}
leg3 = {
    'name' : 'Tau', 'getter' :'daughter(2).', 'nicename' : 'Tau',
    'index' : 2,
}

selections = cms.VPSet(

    ###########################################################################
    # Basic acceptance cuts
    ###########################################################################
    PSetTemplate(selectors.candidate.rect_pt).replace(
        threshold1 = '20', threshold2 = '10',
        getter1 = leg2['getter'], getter2 = leg1['getter'],
        name = 'ElecMuPtCut', nicename = 'Electron-Muon'
    ),

    PSetTemplate(selectors.candidate.eta).replace(
        threshold = '2.1', **leg2),
    PSetTemplate(selectors.candidate.eta).replace(
        threshold = '2.5', **leg1),

    # Select tau leg 3
    PSetTemplate(selectors.candidate.pt).replace(threshold = '20', **leg3),
    # Select tau eta
    PSetTemplate(selectors.candidate.eta).replace(threshold = '2.5', **leg3),

    ###########################################################################
    # ID and Iso cuts
    ###########################################################################

    PSetTemplate(selectors.muons.id).replace(
        muID = 'WWID', **leg2),
    PSetTemplate(selectors.muons.reliso).replace(
        threshold = '0.15', **leg2),

    PSetTemplate(selectors.electrons.id).replace(
        eID = 'WWID', **leg1),
    PSetTemplate(selectors.electrons.reliso).replace(
        threshold = '0.1', **leg1),

    PSetTemplate(selectors.taus.id).replace(
        tauID = 'decayModeFinding', **leg3),
    PSetTemplate(selectors.taus.id).replace(
        tauID = 'byLooseCombinedIsolationDeltaBetaCorr', **leg3),
    PSetTemplate(selectors.taus.id).replace(
        tauID = 'againstElectronLoose', **leg3),
    PSetTemplate(selectors.taus.id).replace(
        tauID = 'againstMuonTight', **leg3),
    PSetTemplate(selectors.candidate.charge).replace(
        getter = '', name = 'finalState', nicename='Final State', charge = '1'),

    PSetTemplate(selectors.extras.e_veto).replace(
        name = 'finalState', nicename='Final State',
        pt_threshold=common['eveto_pt_threshold'], eta_threshold='2.5',
        eID='WWID', getter='', threshold=common['eveto_iso_threshold']),

    PSetTemplate(selectors.extras.mu_veto).replace(
        name = 'finalState', nicename='Final State',
        pt_threshold=common['muveto_pt_threshold'], eta_threshold='2.5',
        muID='WWID', getter='', threshold=common['muveto_iso_threshold']),

    PSetTemplate(selectors.topology.z_veto).replace(
        name = 'Leg1Leg2', nicename='Leg 1-Leg 2',
        index1 = 0, index2 = 1
    ),
    PSetTemplate(selectors.topology.z_veto).replace(
        name = 'Leg1Leg3', nicename='Leg 1-Leg 3',
        index1 = 0, index2 = 2
    ),
    PSetTemplate(selectors.topology.z_veto).replace(
        name = 'Leg2Leg3', nicename='Leg 2-Leg 3',
        index1 = 1, index2 = 2
    ),
    PSetTemplate(selectors.extras.bjet_veto).replace(
        name = 'finalState', nicename='Final State',
        pt_threshold=common['bveto_pt_threshold'], eta_threshold='2.5',
        btag_threshold = common['btag_threshold']),
)

###########################################################################
# Define plots
###########################################################################

from FinalStateAnalysis.Selectors.plotBuilder import makePlots
all_plots, ntuple = makePlots(leg1, leg2, leg3)

# Split into OS/SS regions
plots = cms.PSet(
    histos = cms.VPSet(),
    ntuple = ntuple,
    SS = cms.PSet(
        all_plots,
        SELECT = cms.string('likeSigned(0,1)'),
    ),
    OS = cms.PSet(
        all_plots,
        SELECT = cms.string('!likeSigned(0,1)'),
    ),
)
