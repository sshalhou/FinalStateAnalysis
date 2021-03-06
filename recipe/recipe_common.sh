#!/bin/bash
set -o errexit
set -o nounset

pushd $CMSSW_BASE/src

#for standalone version of svfit
 cvs co -r V00-01-04s TauAnalysis/CandidateTools

# for some reason patTuple creation fails due to lack  of plugin PFCandIsolatorFromDeposits
# to fix
cvs co -r V00-03-13 CommonTools/ParticleFlow

# Tags that work in any release

# To install lumiCalc.py
if [ "$LUMI" = "1" ] 
then
  cvs co -r V04-01-06 RecoLuminosity/LumiDB 
fi

# Add and patch to way speed up trigger matching
# Don't crash if patch already applied.
set +o errexit 
echo "Applying pat trigger matching speedup"
patch -N -p0 < FinalStateAnalysis/recipe/patches/V06-04-16_DataFormats_PatCandidates_PassStrByRef.patch

#echo "Adding 2D expression histogram feature"
#addpkg -z CommonTools/Utils 
#patch -N -p0 < FinalStateAnalysis/recipe/patches/V00-04-02_CommonTools_Utils_Add2DHistoFeature.patch
#set -o errexit

# Only checkout PAT tuple production dependencies if requested.
if [ "$PATPROD" = "1" ]
then
  # Set the compile time flag which enables PAT modules that have external
  # dependencies. 
  cat > $CMSSW_BASE/src/FinalStateAnalysis/PatTools/interface/PATProductionFlag.h << EOF 
#define ENABLE_PAT_PROD
EOF

  # Add support for PU Jet ID
  # See https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetID
  cvs co -r V00-04-01 CondFormats/EgammaObjects
  cvs co -r V00-02-05 -d CMGTools/External UserCode/CMG/CMGTools/External
  cvs co -r V00-02 -d  pharris/MVAMet UserCode/pharris/MVAMet
  rm pharris/MVAMet/data/gbrmet.root
  rm pharris/MVAMet/data/*unityresponse*root
  cvs up -r 1.24 CMGTools/External/src/PileupJetIdAlgo.cc

  ## MOVED TO VERSION SPECIFIC
  #Add Electron ID MVA, Photon and Electron PFIsolation Estimators
  #cvs co -r V00-00-21 -d EGamma/EGammaAnalysisTools UserCode/EGamma/EGammaAnalysisTools
  #individual file tweaks a'la: https://twiki.cern.ch/twiki/bin/view/CMS/HtoZgPhotonID
  #cvs up -r 1.13 EGamma/EGammaAnalysisTools/interface/PFIsolationEstimator.h
  #cvs up -r 1.22 EGamma/EGammaAnalysisTools/src/PFIsolationEstimator.cc
  ## MOVED TO VERSION SPECFIC
  # apply patch so we can configure the passing mask for the PassWP function
  patch -N -p0 < FinalStateAnalysis/recipe/patches/EGammaAnalysisTools_configpatch.patch

  # Add Electron ID MVA  
  pushd EGamma/EGammaAnalysisTools/data
  cat download.url | xargs wget
  popd

  # Add muon effective area code
  cvs co -r V00-00-10 -d Muon/MuonAnalysisTools UserCode/sixie/Muon/MuonAnalysisTools 
  # Remove trainings we don't use
  rm Muon/MuonAnalysisTools/data/*xml

else
  cat > $CMSSW_BASE/src/FinalStateAnalysis/PatTools/interface/PATProductionFlag.h << EOF 
//#define ENABLE_PAT_PROD
EOF

fi

# Get the VBF MVA weight files
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2012#VBF_selection_Matthew
cvs co -r 1.2 UserCode/MitHtt/data/VBFMVA/MuTau/VBFMVA_BDTG.weights.xml

popd
