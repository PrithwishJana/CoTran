public void isVowel ( ch ) {
    if (ch in { 'a' , 'e' , 'i' , 'o' , 'u' }) {
        return true;
    }
     else{
        return false;
    }
}
public void vowelPairs ( s , n ) {
    var cnt = 0;
    for i in range ( n - 1 ) :
        if (( isVowel ( s { i } ) and isVowel ( s { i + 1 } ) )) {
            cnt += 1;
        }
     return cnt;
}
var s = "abaebio";
var n = len ( s );
System.out.println ( vowelPairs ( s , n ) );
