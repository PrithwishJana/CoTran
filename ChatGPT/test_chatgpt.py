from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from tqdm import tqdm
from openai import OpenAI
import os, sys
os.environ["OPENAI_API_KEY"] = "XXXXXX"

root_folder = "./AVATAR_data/third_party"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)

src = "java"
tgt = "python"

suffix = "\nDo not return anything other than the translated code."

if (src == "python") and (tgt == "java"):
  #instruct = "Translate the input Python code to an equivalent Java code. Only output the Java code, don't explain."
  # such that the output Java code is syntactically correct and is runtime equivalent to the input Python code. 
  prefix = "Translate Python to Java:"
  srcProc = pyprocessor
  tgtProc = jprocessor
  dirn = "P2J"
  testPath = "./AVATAR-TC/test.java-python.python"
elif (src == "java") and (tgt == "python"):
  #instruct = "Translate the input Java code to an equivalent Python code. Only output the Python code, don't explain."
  #, such that the output Python code is syntactically correct and is runtime equivalent to the input Java code.
  prefix = "Translate Java to Python:"
  srcProc = jprocessor
  tgtProc = pyprocessor
  testPath = "./AVATAR-TC/test.java-python.java"
  dirn = "J2P"
else:
  sys.exit(1)

client = OpenAI()
#messagesStrt = [{
#            "role": "system",
#            "content": instruct
#          }]

programs = []
with open(testPath, encoding='utf8') as f:
    for line in f:
        programs.append(line.strip())

translations = []

for oneLineProgIndx, oneLineProg in tqdm(enumerate(programs), total=len(programs)):
    program = srcProc.detokenize_code(oneLineProg)
    #print (repr(program))
    #"gpt-3.5-turbo-0301"
    messages = [{
            "role": "user",
            "content": prefix + program + suffix
          }]
    print (messages, flush = True)
    response = client.chat.completions.create(
      model = "gpt-3.5-turbo-0301",
      messages = messages,
      temperature = 0,
      max_tokens = 512,
      top_p = 0,
      frequency_penalty = 0,
      presence_penalty = 0
    )
    print ("tt----------tt", flush = True)
    translation = response.choices[0].message.content
    print (translation, flush = True)
    print ("ll----------ll", flush = True)
    try:
      txOneLine = " ".join(tgtProc.tokenize_code(translation))
    except:
      txOneLine = "0ERROR"
    print (txOneLine, flush = True)
    translations.append(txOneLine)
    print ("dd----------dd\n\n", flush = True)
    #if (oneLineProgIndx == 100):
    #  break

with open(os.path.join("ChatGPT", "chatgpt0301{}.{}".format(dirn, tgt)), 
            'w', encoding = 'utf-8') as f:
    for line in translations:
        f.write(f"{line}\n")