from evaluation.compute_compilationErr_strtEnd import computeErrMetric_forPredFile
import argparse

def argParse_helperFunc():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pathPrediction', type=str)
    parser.add_argument('--DEST_LANG', type=str)
    parser.add_argument('--writeDirTmp', type=str)
    args = parser.parse_args()
    return args

args = argParse_helperFunc()
errStrtMetric = computeErrMetric_forPredFile(args.pathPrediction, 
                                            args.DEST_LANG, 
                                            args.writeDirTmp)
                                            
print ("avgFirstErrPos:", errStrtMetric * 100)