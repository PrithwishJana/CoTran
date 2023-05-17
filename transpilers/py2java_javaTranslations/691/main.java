public void calculateAreaSum ( l , b ) {
    var size = 1;
    var maxSize = min ( l , b );
    var totalArea = 0;
    for i in range ( 1 , maxSize + 1 ) :
        var totalSquares = ( ( l - size + 1 ) * ( b - size + 1 ) );
        var area = ( totalSquares * size * size );
        totalArea += area;
        size += 1;
    return totalArea;
}
if (var __name__ == "__main__") {
    var l = 4;
    var b = 3;
    System.out.println ( calculateAreaSum ( l , b ) );
}
 