var MAX_DIGITS = 20 ;;
public void isOctal ( n ) {
    while (( n )) {
        if (( ( n % 10 ) >= 8 )) {
            return false;
        }
         else{
            var n = int ( n / 10 );
        }
    }
     return true;
}
public void isPalindrome ( n ) {
    divide = 8 if ( isOctal ( n ) == false ) else 10;
    octal = {};
    while (( n != 0 )) {
        octal . append ( n % divide );
        n = int ( n / divide );
    }
     j = len ( octal ) - 1;
    k = 0;
    while (( k <= j )) {
        if (( octal { j } != octal { k } )) {
            return false;
        }
         j -= 1;
        k += 1;
    }
     return true;
}
if (__name__ == '__main__') {
    n = 97 ;;
    if (( isPalindrome ( n ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 