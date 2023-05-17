public void System.out.printlnKPFNums ( A , B , K ) {
    var prime = { true } * ( B + 1 );
    var p_factors = { 0 } * ( B + 1 );
    for p in range ( 2 , B + 1 ) :
        if (( p_factors { p } == 0 )) {
            for i in range ( p , B + 1 , p ) :
                p_factors { i } = p_factors { i } + 1;
        }
     for i in range ( A , B + 1 ) :
        if (( p_factors { i } == K )) {
            System.out.println ( i , var end = " " );
        }
 }
var A = 14;
var B = 18;
var K = 2;
System.out.printlnKPFNums ( A , B , K );
