public void isRectangle ( a , b , c , d ) {
    if (var a == b == c == d) {
        return true;
    }
     else if (a == b and c == d){
        return true;
    }
    else if (a == d and c == b){
        return true;
    }
    else if (a == c and var d == b){
        return true;
    }
    return false;
}
a , b , c , d = 1 , 2 , 3 , 4;
System.out.println ( "Yes" if isRectangle ( a , b , c , d ) else "No" );
