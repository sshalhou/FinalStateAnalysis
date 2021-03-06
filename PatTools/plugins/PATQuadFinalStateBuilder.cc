#include "FinalStateAnalysis/PatTools/plugins/PATQuadFinalStateBuilderT.h"
#include "FinalStateAnalysis/DataFormats/interface/PATQuadLeptonFinalStates.h"

typedef PATQuadFinalStateBuilderT<PATElecElecElecElecFinalState> PATElecElecElecElecFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecElecMuFinalState> PATElecElecElecMuFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecElecTauFinalState> PATElecElecElecTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecElecPhoFinalState> PATElecElecElecPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecMuMuFinalState> PATElecElecMuMuFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecMuTauFinalState> PATElecElecMuTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecMuPhoFinalState> PATElecElecMuPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecTauTauFinalState> PATElecElecTauTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecTauPhoFinalState> PATElecElecTauPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecElecPhoPhoFinalState> PATElecElecPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecMuMuMuFinalState> PATElecMuMuMuFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecMuMuTauFinalState> PATElecMuMuTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecMuMuPhoFinalState> PATElecMuMuPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecMuTauTauFinalState> PATElecMuTauTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecMuTauPhoFinalState> PATElecMuTauPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecMuPhoPhoFinalState> PATElecMuPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecTauTauTauFinalState> PATElecTauTauTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecTauTauPhoFinalState> PATElecTauTauPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecTauPhoPhoFinalState> PATElecTauPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATElecPhoPhoPhoFinalState> PATElecPhoPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuMuMuMuFinalState> PATMuMuMuMuFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuMuMuTauFinalState> PATMuMuMuTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuMuMuPhoFinalState> PATMuMuMuPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuMuTauTauFinalState> PATMuMuTauTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuMuTauPhoFinalState> PATMuMuTauPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuMuPhoPhoFinalState> PATMuMuPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuTauTauTauFinalState> PATMuTauTauTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuTauTauPhoFinalState> PATMuTauTauPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuTauPhoPhoFinalState> PATMuTauPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATMuPhoPhoPhoFinalState> PATMuPhoPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATTauTauTauTauFinalState> PATTauTauTauTauFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATTauTauTauPhoFinalState> PATTauTauTauPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATTauTauPhoPhoFinalState> PATTauTauPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATTauPhoPhoPhoFinalState> PATTauPhoPhoPhoFinalStateProducer;
typedef PATQuadFinalStateBuilderT<PATPhoPhoPhoPhoFinalState> PATPhoPhoPhoPhoFinalStateProducer;

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(PATElecElecElecElecFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecElecMuFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecElecTauFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecElecPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecMuMuFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecMuTauFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecMuPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecTauTauFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecTauPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecElecPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecMuMuMuFinalStateProducer);
DEFINE_FWK_MODULE(PATElecMuMuTauFinalStateProducer);
DEFINE_FWK_MODULE(PATElecMuMuPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecMuTauTauFinalStateProducer);
DEFINE_FWK_MODULE(PATElecMuTauPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecMuPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecTauTauTauFinalStateProducer);
DEFINE_FWK_MODULE(PATElecTauTauPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecTauPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATElecPhoPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATMuMuMuMuFinalStateProducer);
DEFINE_FWK_MODULE(PATMuMuMuTauFinalStateProducer);
DEFINE_FWK_MODULE(PATMuMuMuPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATMuMuTauTauFinalStateProducer);
DEFINE_FWK_MODULE(PATMuMuTauPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATMuMuPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATMuTauTauTauFinalStateProducer);
DEFINE_FWK_MODULE(PATMuTauTauPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATMuTauPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATMuPhoPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATTauTauTauTauFinalStateProducer);
DEFINE_FWK_MODULE(PATTauTauTauPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATTauTauPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATTauPhoPhoPhoFinalStateProducer);
DEFINE_FWK_MODULE(PATPhoPhoPhoPhoFinalStateProducer);
