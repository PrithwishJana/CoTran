public void isPower ( x , y ) {
    if (( var x == 1 )) {
        return ( var y == 1 );
    }
     var pow = 1;
    while (( pow < y )) {
        pow = pow * x;
    }
     return ( pow == y );
}
if (( isPower ( 10 , 1 ) )) {
    System.out.println ( 1 );
}
 else{
    System.out.println ( 0 );
}
if (( isPower ( 1 , 20 ) )) {
    System.out.println ( 1 );
}
 else{
    System.out.println ( 0 );
}
if (( isPower ( 2 , 128 ) )) {
    System.out.println ( 1 );
}
 else{
    System.out.println ( 0 );
}
if (( isPower ( 2 , 30 ) )) {
    System.out.println ( 1 );
}
 else{
    System.out.println ( 0 );
}
