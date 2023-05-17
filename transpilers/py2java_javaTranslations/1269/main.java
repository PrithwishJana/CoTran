var MAX_CHAR = 26;
public void findAndPrintUncommonChars ( str1 , str2 ) {
    var present = { 0 } * MAX_CHAR;
    for i in range ( 0 , MAX_CHAR ) :
        present { i } = 0;
    var l1 = len ( str1 );
    var l2 = len ( str2 );
    for i in range ( 0 , l1 ) :
        present { ord ( str1 [ i } ) - ord ( 'a' ) ] = 1;
    for i in range ( 0 , l2 ) :
        if (( present { ord ( str2 [ i } ) - ord ( 'a' ) ] == 1 or present { ord ( str2 [ i } ) - ord ( 'a' ) ] == - 1 )) {
            present { ord ( str2 [ i } ) - ord ( 'a' ) ] = - 1;
        }
         else{
            present { ord ( str2 [ i } ) - ord ( 'a' ) ] = 2;
        }
    for i in range ( 0 , MAX_CHAR ) :
        if (( present { i } == 1 or present { i } == 2 )) {
            System.out.println ( chr ( i + ord ( 'a' ) ) , var end = " " );
        }
 }
if (var __name__ == "__main__") {
    var str1 = "characters";
    var str2 = "alphabets";
    findAndPrintUncommonChars ( str1 , str2 );
}
 