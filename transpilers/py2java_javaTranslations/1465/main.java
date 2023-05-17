public void findNature ( a , b , n ) {
    if (( var n == 0 )) {
        return ( a & 1 ) ;;
    }
     if (( n == 1 )) {
        return ( b & 1 ) ;;
    }
     if (( ( a & 1 ) == 0 )) {
        if (( ( b & 1 ) == 0 )) {
            return false ;;
        }
         else{
            return true if ( n % 3 != 0 ) else false ;;
        }
    }
     else{
        if (( ( b & 1 ) == 0 )) {
            return true if ( ( n - 1 ) % 3 != 0 ) else false ;;
        }
         else{
            return true if ( ( n + 1 ) % 3 != 0 ) else false ;;
        }
    }
}
a = 2 ;;
b = 4 ;;
n = 3 ;;
if (( findNature ( a , b , n ) == true )) {
    System.out.println ( "Odd" , var end = " " ) ;;
}
 else{
    System.out.println ( "Even" , end = " " ) ;;
}
