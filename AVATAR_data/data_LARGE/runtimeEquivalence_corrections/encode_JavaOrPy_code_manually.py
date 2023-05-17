from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
root_folder = "../../third_party"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)

pyCode = """
n , k = map ( int , input ( ) . split ( ) )
a = list ( map ( int , input ( ) . split ( ) ) )
if ( ( n - k ) % ( k - 1 ) == 0 ):
    ans = ( n - k ) // ( k - 1 )
else:
    ans = ( n - k ) // ( k - 1 ) + 1
print (ans+1)
"""

javaCode = """
import java . util . * ; 
public class Solution {
  public void duplicateZeros ( int [ ] arr ) {
    int movePos = 0 ;
    int lastPos = arr . length - 1 ;
    for ( int i = 0 ;
    i <= lastPos - movePos ;
    i ++ ) {
      if ( arr [ i ] == 0 ) {
        if ( i == lastPos - movePos ) {
          arr [ lastPos ] = 0 ;
          lastPos -- ;
          break ;
        }
        movePos ++ ;
      }
    }
    lastPos = lastPos - movePos ;
    for ( int i = lastPos ;
    i >= 0 ;
    i -- ) {
      if ( arr [ i ] == 0 ) {
        arr [ i + movePos ] = 0 ;
        movePos -- ;
        arr [ i + movePos ] = 0 ;
      }
      else {
        arr [ i + movePos ] = arr [ i ] ;
      }
    }
  }

  public static void main(String [] args){
      Solution sObj = new Solution();
      int [] arr = {1,0,2,3,0,4,5,0};
     sObj.duplicateZeros(arr);
      System.out.println(Arrays . toString ( arr ));
  }
}
"""

oneLineCodePy = " ".join(pyprocessor.tokenize_code(pyCode))
oneLineCodeJava = " ".join(jprocessor.tokenize_code(javaCode))

print (oneLineCodePy)
print ()
print (oneLineCodeJava)

#" { : . 2 f } " . format ( x )
#String . format ( " % . 2 f " , x )