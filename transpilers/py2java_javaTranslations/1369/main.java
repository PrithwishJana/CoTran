public void multipleOfThree ( K , dig0 , dig1 ) {
    var sum = 0;
    temp = ( dig0 + dig1 ) % 10;
    sum = dig0 + dig1;
    if (( var K == 2 )) {
        if (( sum % 3 == 0 )) {
            return true;
        }
         else{
            return false;
        }
    }
     sum += temp;
    numberofGroups = ( K - 3 ) // 4;
    remNumberofDigits = ( K - 3 ) % 4;
    sum += ( numberofGroups * 20 );
    for i in range ( remNumberofDigits ) :
        temp = ( 2 * temp ) % 10;
        sum += temp;
    if (( sum % 3 == 0 )) {
        return true;
    }
     else{
        return false;
    }
}
if (__name__ == "__main__") {
    K = 5;
    var dig0 = 3;
    var dig1 = 4;
    if (( multipleOfThree ( K , dig0 , dig1 ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 