public void compute ( ) {
    var i = 286;
    var j = 166;
    var k = 144;
    while (true) {
        var triangle = i * ( i + 1 ) // 2;
        var pentagon = j * ( j * 3 - 1 ) // 2;
        var hexagon = k * ( k * 2 - 1 );
        var minimum = min ( triangle , pentagon , hexagon );
        if (minimum == max ( triangle , pentagon , hexagon )) {
            return str ( triangle );
        }
         if minimum == triangle : i += 1;
        if minimum == pentagon : j += 1;
        if minimum == hexagon : k += 1;
    }
 }
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 