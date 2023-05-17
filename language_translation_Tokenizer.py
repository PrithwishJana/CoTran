import argparse, os
from transformers import RobertaTokenizer
from tokenizers import AddedToken
from LexersParsers.java.JavaLexer import JavaLexer
from LexersParsers.python.Python3Lexer import Python3Lexer
import LT_utils_CFLoss

def modifiedPrint(*stringsToPrint):
    for arg in stringsToPrint:
        print (arg, end=" ", flush=True)
    print ("", flush=True)

def argParse_helperFunc():
    #=================== SETTING ARGPARSE ARGUMENTS ====================
    parser = argparse.ArgumentParser()
    parser.add_argument('--writeDir', type = str, required = True)
    args = parser.parse_args()
    modifiedPrint(args)
    return args

def saveTokenizer(tokenizerSavePath):
    print ("Started")
    tokenizer = RobertaTokenizer.from_pretrained("Salesforce/codet5-base")
    print ("Initialized tokenizer")

    # Adding special tokens
    PythonTokenizerExtras = set(["NEW_LINE", "INDENT", "DEDENT"])
    JavaTokenizerExtras = set([])
    JavaKeywords = set(JavaLexer.literalNames) - set(["<INVALID>"])
    PythonKeywords = set(Python3Lexer.literalNames) - set(["<INVALID>"])
    spclTokensToAdd = list(PythonTokenizerExtras | JavaTokenizerExtras | JavaKeywords | PythonKeywords)
    spclTokensToAdd = [x.strip("'") for x in spclTokensToAdd]

    #spclTokensToAdd = [AddedToken(x, single_word = True, 
    #                            lstrip = True, rstrip = False) for x in spclTokensToAdd]

    spclTokensToAdd = sorted(spclTokensToAdd)

    num_added_toks = 0
    for tok in spclTokensToAdd:
        addOrNot = tokenizer.add_tokens(tok)
        if addOrNot:
            print ("Added", tok)
        else:
            print ("Not-added", tok)
        num_added_toks += addOrNot
    print("We have added", num_added_toks, "tokens")
    
    tokenizerPath = os.path.join(tokenizerSavePath, "tokenizer")
    tokenizer.save_pretrained(tokenizerPath)
    print ("Tokenizer saved at path: {}".format(tokenizerPath))

#================== MAIN ======================
if __name__ == '__main__':
    args = argParse_helperFunc()
    saveTokenizer(args.writeDir)

    tokenizer = RobertaTokenizer.from_pretrained(os.path.join(args.writeDir, "tokenizer"))

    '''
    myStr = "age = int ( input ( ) ) NEW_LINE ans = ' YES ' if age == 7 or age == 5 or age == 3 else ' NO ' NEW_LINE print ( ans )"
    print ("\nmyStr: ", myStr)
    tokenIDs = tokenizer(myStr, truncation = True, padding = 'max_length', 
                            max_length=512, return_tensors = 'np')['input_ids'].flatten()
    #tokenIDs = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(myStr))
    print ("\ntokenIDs: ", tokenIDs)
    print ("\nDecoded Str by .decode: ", tokenizer.decode(tokenIDs, 
                                            skip_special_tokens = False,
                                            clean_up_tokenization_spaces = False))

    printStr = "\nToken Mapping: "
    for xIndx, x in enumerate(tokenIDs):
        printStr += "\t{}:{}\n".format(x, tokenizer.decode(x, skip_special_tokens = False))
        if xIndx == 100:
            break
    print (printStr)
    '''

