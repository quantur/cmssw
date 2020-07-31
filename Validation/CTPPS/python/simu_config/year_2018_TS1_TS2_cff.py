import FWCore.ParameterSet.Config as cms

from Validation.CTPPS.simu_config.year_2018_cff import *

# alignment
from CalibPPS.ESProducers.ctppsRPAlignmentCorrectionsDataESSourceXML_cfi import *
alignmentFile = "Validation/CTPPS/alignment/2018_TS1_TS2.xml"
ctppsRPAlignmentCorrectionsDataESSourceXML.MisalignedFiles = [alignmentFile]
ctppsRPAlignmentCorrectionsDataESSourceXML.RealFiles = [alignmentFile]

# timing resolution
ctppsDirectProtonSimulation.timeResolutionDiamonds45 = "2 * ( (x<10)*(-0.0086*(x-10) + 0.100) + (x>=10)*(0.100) )"
ctppsDirectProtonSimulation.timeResolutionDiamonds56 = "2 * ( (x<8) *(-0.0100*(x-8)  + 0.100) + (x>=8) *(-0.0027*(x-8) + 0.100) )"
