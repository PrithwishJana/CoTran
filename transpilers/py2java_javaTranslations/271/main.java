public void charCheck ( input_char ) {
    if (( ( int ( ord ( input_char ) ) >= 65 and int ( ord ( input_char ) ) <= 90 ) or ( int ( ord ( input_char ) ) >= 97 and int ( ord ( input_char ) ) <= 122 ) )) {
        System.out.println ( " Alphabet " );
    }
     else if (( int ( ord ( input_char ) ) >= 48 and int ( ord ( input_char ) ) <= 57 )){
        System.out.println ( " Digit " );
    }
    else{
        System.out.println ( " Special Character " );
    }
}
var input_char = '$';
charCheck ( input_char );
