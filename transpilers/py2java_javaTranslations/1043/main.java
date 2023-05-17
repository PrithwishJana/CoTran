public void checkUtil ( num , dig , base ) {
    if (( var dig == 1 and num < base )) {
        return true;
    }
     if (( dig > 1 and num >= base )) {
        return checkUtil ( num / base , - - dig , base );
    }
     return false;
}
public void check ( num , dig ) {
    for base in range ( 2 , 33 ) :
        if (( checkUtil ( num , dig , base ) )) {
            return true;
        }
     return false;
}
num = 8;
dig = 3;
if (( check ( num , dig ) == true )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
