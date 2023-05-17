var st = set ( );
public void generateNumbers ( n , num , a , b ) {
    if (( num > 0 and num < n )) {
        st . add ( num );
    }
     if (( num >= n )) {
        return;
    }
     if (( num * 10 + a > num )) {
        generateNumbers ( n , num * 10 + a , a , b );
    }
     generateNumbers ( n , num * 10 + b , a , b );
}
public void System.out.printlnNumbers ( n ) {
    for i in range ( 10 ) :
        for j in range ( i + 1 , 10 , 1 ) :
            generateNumbers ( n , 0 , i , j );
    System.out.println ( "The numbers are:" , var end = " " );
    var l = list ( st );
    System.out.println ( l );
}
if (var __name__ == '__main__') {
    var n = 12;
    System.out.printlnNumbers ( n );
}
 