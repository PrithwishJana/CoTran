public void isVowel ( ch ) {
    if (ch in { 'i' , 'a' , 'e' , 'o' , 'u' }) {
        return true;
    }
     else{
        return false;
    }
}
public void isSatisfied ( st , n ) {
    for i in range ( 1 , n ) :
        if (( isVowel ( st { i } ) == false and isVowel ( st { i - 1 } ) == false )) {
            return false;
        }
     for i in range ( 1 , n - 1 ) :
        if (( isVowel ( st { i } ) and isVowel ( st { i - 1 } ) == false and isVowel ( st { i + 1 } ) == false )) {
            return false;
        }
     return true;
}
var st = "acaba";
var n = len ( st );
if (( isSatisfied ( st , n ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
