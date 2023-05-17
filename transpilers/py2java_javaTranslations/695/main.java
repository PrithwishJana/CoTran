public void findOptimalSolution ( a , N ) {
    a . sort ( );
    var points = 0;
    for i in range ( 0 , N ) :
        points += a { i } * i;
    return points;
}
if (var __name__ == "__main__") {
    var a = { 1 , 4 , 2 , 3 , 9 };
    var N = len ( a );
    System.out.println ( findOptimalSolution ( a , N ) );
}
 