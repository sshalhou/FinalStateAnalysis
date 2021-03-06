'''

Dataset definitions for 8TeV

You can query the information in this file at the command line.

Run

python data8TeVNew.py --help

for more information.

Author: Evan K. Friis, UW Madison

'''

from datacommon import square, cube, quad, picobarns, \
        br_w_leptons, br_z_leptons, query_cli

from data8TeV import datadefs as datadefs52

# Figure this out later.
data_name_map = {}

datadefs = {
   'WZJetsTo3LNu_TuneZ2_8TeV-madgraph-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/WZJetsTo3LNu_TuneZ2_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/ZZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/ZZJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v3/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'WZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/WZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZJetsTo4L_TuneZ2star_8TeV-madgraph-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/ZZJetsTo4L_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_v2' : {
   'analyses': ['HTT'],
   'datasetpath' : "/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_v1' : {
   'analyses': ['HTT'],
   'datasetpath' : "/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball' : {
   'analyses': ['HTT'],
   'datasetpath' : "/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'DYJetsToLL_M-10To50filter_8TeV-madgraph' : {
   'analyses': ['ZZ'],
   'datasetpath' : "/DYJetsToLL_M-10To50filter_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola' : {
   'analyses': ['HTT'],
   'datasetpath' : "/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZTo2e2tau_8TeV-powheg-pythia6' : {
   'analyses': ['ZZ'],
   'datasetpath' : "/ZZTo2e2tau_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZTo2e2mu_8TeV-powheg-pythia6' : {
   'analyses': ['ZZ'],
   'datasetpath' : "/ZZTo2e2mu_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZTo2mu2tau_8TeV-powheg-pythia6' : {
   'analyses': ['ZZ'],
   'datasetpath' : "/ZZTo2mu2tau_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM ",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZTo4mu_8TeV-powheg-pythia6' : {
   'analyses': ['ZZ'],
   'datasetpath' : "/ZZTo4mu_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZTo4e_8TeV-powheg-pythia6' : {
   'analyses': ['ZZ'],
   'datasetpath' : "/ZZTo4e_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'ZZTo4tau_8TeV-powheg-pythia6' : {
   'analyses': ['ZZ'],
   'datasetpath' : "/ZZTo4tau_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },
   
   'WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola' : {
   'analyses' : ['Wbb'],
   'datasetpath' : "/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM",
   'x_sec' : -999,
   'pu' : 'S10',
   },

   'DoubleMu_Run2012B_13Jul2012_v4_embedded_trans1_tau116_ptmu1_13had1_17_v1' : {
   'analyses': ['HTauTau'],
   'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_Run2012B_13Jul2012_v4_embedded_trans1_tau116_ptmu1_13had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'pu' : 'data',
   },

   'DoubleMu_Run2012B_13Jul2012_v4_embedded_trans1_tau115_ptelec1_17had1_17_v1' : {
   'analyses': ['HTauTau'],
   'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_Run2012B_13Jul2012_v4_embedded_trans1_tau115_ptelec1_17had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'pu' : 'data',
   },

   'DoubleMu_Run2012A_13Jul2012_v1_embedded_trans1_tau115_ptelec1_17had1_17_v1' : {
   'analyses': ['HTauTau'],
   'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_Run2012A_13Jul2012_v1_embedded_trans1_tau115_ptelec1_17had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'pu' : 'data',
   },

   'DoubleMu_Run2012A_13Jul2012_v1_embedded_trans1_tau116_ptmu1_13had1_17_v1' : {
   'analyses': ['HTauTau'],
   'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_Run2012A_13Jul2012_v1_embedded_trans1_tau116_ptmu1_13had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'pu' : 'data',
   },

   'DoubleMu_Run2012C_PromptReco_v2_embedded_trans1_tau116_ptmu1_13had1_17_v1' : {
   'analyses': ['HTauTau'],
   'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_Run2012C_PromptReco_v2_embedded_trans1_tau116_ptmu1_13had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'pu' : 'data',
   },

   'DoubleMu_Run2012C_PromptReco_v2_embedded_trans1_tau115_ptelec1_17had1_17_v1' : {
   'analyses': ['HTauTau'],
   'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_Run2012C_PromptReco_v2_embedded_trans1_tau115_ptelec1_17had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'pu' : 'data',
   },

   'DoubleMu_Run2012C_24Aug2012_v1_embedded_trans1_tau116_ptmu1_13had1_17_v1' : {
   'analyses': ['HTauTau'],
   'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_Run2012C_24Aug2012_v1_embedded_trans1_tau116_ptmu1_13had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'pu' : 'data',
   },

   'DoubleMu_Run2012C_24Aug2012_v1_embedded_trans1_tau115_ptelec1_17had1_17_v1' : {
   'analyses': ['HTauTau'],
   'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_Run2012C_24Aug2012_v1_embedded_trans1_tau115_ptelec1_17had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'pu' : 'data',
   },
}

for n in range(1,5) :
   datadefs['W%iJetsToLNu_TuneZ2Star_8TeV-madgraph' % n] = {
      'analyses': ['HTT','Wbb'],
      'datasetpath': "/W%iJetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % n,
      'pu' : 'S10',
      'x_sec' : -999,
      }



############################################################################
#### Signal datasets                    ####################################
############################################################################
for mass in range(80,150, 10) + range(160, 220, 20) + range(250, 550, 50) + range(600, 1100, 100) :
   datadefs['SUSYGluGluToHToTauTau_M-%i_8TeV-pythia6-tauola' % mass] = {
      'analyses': ['HTT'],
      'datasetpath': "/SUSYGluGluToHToTauTau_M-%i_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % mass,
      'pu' : 'S10',
      'x_sec' : -999,
      }
   datadefs['SUSYBBHToTauTau_M-%i_8TeV-pythia6-tauola' % mass] = {
      'analyses': ['HTT'],
      'datasetpath': "/SUSYBBHToTauTau_M-%i_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % mass,
      'pu' : 'S10',
      'x_sec' : -999,
      }

datadefs['SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola'] = {
   'analyses': ['HTT'],
   'datasetpath': "/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM",
   'pu' : 'S10',
   'x_sec' : -999,
   }

for mass in range(110, 165, 5) :
   datadefs['GluGluToHToTauTau_M-%i_8TeV-powheg-pythia6' % mass] = {
      'analyses': ['HTT'],
      'datasetpath': "/GluGluToHToTauTau_M-%i_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % mass,
      'pu' : 'S10',
      'x_sec' : -999,
      }
   datadefs['VBF_HToTauTau_M-%i_8TeV-powheg-pythia6' % mass] = {
      'analyses': ['HTT'],
      'datasetpath': "/VBF_HToTauTau_M-%i_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % mass,
      'pu' : 'S10',
      'x_sec' : -999,
      }

for mass in range(115,130) + range(130,150,5) + range(150,200,10) + [200,220] + range(250,600,25) + range(600,1001,50) :
   datadefs['GluGluToHToZZTo4L_M-%i_8TeV-powheg-pythia6' % mass] = {
      'analyses': ['HTT'],
      'datasetpath': "/GluGluToHToZZTo4L_M-%i_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % mass,
      'pu' : 'S10',
      'x_sec' : -999,
      }
   datadefs['VBF_HToZZTo4L_M-%i_8TeV-powheg-pythia6' % mass] = {
      'analyses': ['HTT'],
      'datasetpath': "/VBF_HToZZTo4L_M-%i_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % mass,
      'pu' : 'S10',
      'x_sec' : -999,
      }


for mass in range(110, 165, 5) :
   if mass==135 :
      ver=2
   else :
      ver=1

   datadefs['WH_ZH_TTH_HToTauTau_M-%i_8TeV-pythia6-tauola' % mass] = {
      'analyses': ['HTT'],
      'datasetpath': "/WH_ZH_TTH_HToTauTau_M-%i_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v%i/AODSIM" % (mass,ver),
      'pu' : 'S10',
      'x_sec' : -999,
      }

# Add VH files
for mass in range(110, 145, 5):
   datadefs['VHtautau_lepdecay_%i' % mass] = {
      'analyses': ['VH'],
      'datasetpath': "/WH_ZH_TTH_HToTauTau_M-%i_lepdecay_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % mass,
      'pu' : 'S10',
      'x_sec' : -999,
      }

for mass in range(110, 150, 10):
   datadefs['VHWW_lepdecay_%i' % mass] = {
      'analyses': ['VH'],
      'datasetpath': "/WH_ZH_TTH_HToWW_M-%i_lepdecay_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM" % mass,
      'pu' : 'S10',
      'x_sec' : -999,
      }

# We use the same name for the 53X lepdecay only samples (sigh)
datadefs['VH_H2Tau_M-110'] = {}
datadefs['VH_H2Tau_M-120'] = {}
datadefs['VH_H2Tau_M-130'] = {}
datadefs['VH_H2Tau_M-140'] = {}

datadefs['VH_H2Tau_M-110']['x_sec'] = (1.060*br_w_leptons + 0.5869*br_z_leptons + 0.1887*square(br_w_leptons))*7.95E-02
datadefs['VH_H2Tau_M-120']['x_sec'] = (0.7966*br_w_leptons + 0.4483*br_z_leptons + 0.1470*square(br_w_leptons))*7.04E-02
datadefs['VH_H2Tau_M-130']['x_sec'] = (0.6095*br_w_leptons + 0.3473*br_z_leptons + 0.1157*square(br_w_leptons))*5.48E-02
datadefs['VH_H2Tau_M-140']['x_sec'] = (0.4713*br_w_leptons + 0.2728*br_z_leptons + 0.09207*square(br_w_leptons))*3.54E-02

# Add data files

datadefs['data_DoubleMu_Run2012B_13Jul2012_v4'] = {
   'datasetpath' : "/DoubleMu/Run2012B-13Jul2012-v4/AOD",
   'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/json_DCSONLY.txt",
   'firstRun' : 193834,
   'lastRun' : 196531,
   'analyses' : ['HZZ'],
   }

def build_data_set(pd, analyses):
   subsample_dict = {
      'data_%s_Run2012A_13Jul2012_v1' % pd : {
      'datasetpath' : "/%s/Run2012A-13Jul2012-v1/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt",
      'firstRun' : 190456,
      'lastRun' : 193621,
      'analyses' : analyses,
      },
      'data_%s_Run2012B_13Jul2012_v1' % pd : {
      'datasetpath' : "/%s/Run2012B-13Jul2012-v1/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt",
      'firstRun' : 193834,
      'lastRun' : 196531,
      'analyses' : analyses,
      },
      'data_%s_Run2012C_PromptReco_v2_Run198934_201264' % pd : {
      'datasetpath' : "/%s/Run2012C-PromptReco-v2/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_190456-203002_8TeV_PromptReco_Collisions12_JSON_v2.txt",
      'firstRun' : 198934,
      'lastRun' : 201264,
      'analyses' : analyses,
      },
      'data_%s_Run2012C_PromptReco_v2_Run201265_203755' % pd : {
      'datasetpath' : "/%s/Run2012C-PromptReco-v2/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_190456-203002_8TeV_PromptReco_Collisions12_JSON_v2.txt",
      'firstRun' : 201265,
      'lastRun' : 203755,
      'analyses' : analyses,
      },
      'data_%s_Run2012A_recover_06Aug2012_v1' % pd : {
      'datasetpath' : "/%s/Run2012A-recover-06Aug2012-v1/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_190782-190949_8TeV_06Aug2012ReReco_Collisions12_JSON.txt",
      'firstRun' : 190456, #Not 100% sure about these.. IAR 28.Sep.2012
      'lastRun' : 193621,
      'analyses' : analyses,
      },
      'data_%s_Run2012C_PromptReco_v1' % pd : {
      'datasetpath' : "/%s/Run2012C-PromptReco-v1/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_190456-203002_8TeV_PromptReco_Collisions12_JSON_v2.txt",
      'firstRun' : 19770,
      'lastRun' : 198913,
      'analyses' : analyses,
      },
      'data_%s_Run2012C_24Aug2012_v1' % pd : {
      'datasetpath' : "/%s/Run2012C-24Aug2012-v1/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_198022-198523_8TeV_24Aug2012ReReco_Collisions12_JSON.txt",
      'firstRun' : 198022,
      'lastRun' : 198523,
      'analyses' : analyses,
      },
    }
   sample_dict = {
      'data_%s' % pd : subsample_dict.keys()
      }
   return subsample_dict, sample_dict

# Build all the PDs we use
data_DoubleMu, list_DoubleMu = build_data_set('DoubleMu', ['VH', 'Mu','4L'])
datadefs.update(data_DoubleMu)
data_name_map.update(list_DoubleMu)

data_MuEG, list_MuEG = build_data_set('MuEG', ['VH', 'HTT', 'Mu'])
datadefs.update(data_MuEG)
data_name_map.update(list_MuEG)

data_DoubleE, list_DoubleE = build_data_set('DoubleElectron', ['VH','4L'])
datadefs.update(data_DoubleE)
data_name_map.update(list_DoubleE)

data_SingleMu, list_SingleMu = build_data_set('SingleMu', ['Tau', 'Mu', 'Wbb'])
datadefs.update(data_SingleMu)
data_name_map.update(list_SingleMu)

data_SingleElectron, list_SingleElectron = build_data_set('SingleElectron', ['Tau', 'E', 'Wjets'])
datadefs.update(data_SingleElectron)
data_name_map.update(list_SingleElectron)

data_TauPlusX, list_TauPlusX = build_data_set('TauPlusX', ['HTT', ])
datadefs.update(data_TauPlusX)
data_name_map.update(list_TauPlusX)

if __name__=="__main__":
    query_cli(datadefs)

