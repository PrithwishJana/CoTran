public void isVowel ( c ) {
    return ( var c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' );
}
public void encryptString ( s , n , k ) {
    var countVowels = 0;
    countConsonants = 0;
    ans = "";
    for l in range ( n - k + 1 ) :
        countVowels = 0;
        var countConsonants = 0;
        for r in range ( l , l + k ) :
            if (( isVowel ( s { r } ) == true )) {
                countVowels += 1;
            }
             else{
                countConsonants += 1;
            }
        ans += ( str ) ( countVowels * countConsonants );
    return ans;
}
if (var __name__ == '__main__') {
    var s = "hello";
    var n = len ( s );
    var k = 2;
    System.out.println ( encryptString ( s , n , k ) );
}
 