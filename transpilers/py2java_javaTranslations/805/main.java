public void maxFreq ( s , a , b ) {
    var fre = { 0 for i in range ( 10 ) };
    var n = len ( s );
    if (( a > b )) {
        swap ( a , b );
    }
     for i in range ( 0 , n , 1 ) :
        var a = ord ( s { i } ) - ord ( '0' );
        fre { a } += 1;
    if (( fre { a } == 0 and fre { b } == 0 )) {
        return - 1;
    }
     else if (( fre { a } >= fre { b } )){
        return a;
    }
    else{
        return b;
    }
}
if (__name__ == '__main__') {
    a = 4;
    var b = 7;
    var s = "47744";
    System.out.println ( maxFreq ( s , a , b ) );
}
 