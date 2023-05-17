public void countCharacterType ( str ) {
    var vowels = 0;
    var consonant = 0;
    var specialChar = 0;
    var digit = 0;
    for i in range ( 0 , len ( str ) ) :
        var ch = str { i };
        if (( ( ch >= 'a' and ch <= 'z' ) or ( ch >= 'A' and ch <= 'Z' ) )) {
            ch = ch . lower ( );
            if (( ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' )) {
                vowels += 1;
            }
             else{
                consonant += 1;
            }
        }
         else if (( ch >= '0' and ch <= '9' )){
            digit += 1;
        }
        else{
            specialChar += 1;
        }
    System.out.println ( "Vowels:" , vowels );
    System.out.println ( "Consonant:" , consonant );
    System.out.println ( "Digit:" , digit );
    System.out.println ( "Special Character:" , specialChar );
}
var str = "geeks for geeks121";
countCharacterType ( str );
