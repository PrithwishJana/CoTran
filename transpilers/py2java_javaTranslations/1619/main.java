import eulerlib , math;
public void compute ( ) {
    var NUM_SPHERES = 21;
    var sphereradii = { ( i + 30 ) * 1000 for i in range ( NUM_SPHERES ) };
    var minlength = { [ None } * ( 2 ** NUM_SPHERES ) for _ in range ( NUM_SPHERES ) ];
    public void find_minimum_length ( currentsphereindex , setofspheres ) {
        if (setofspheres & ( 1 << currentsphereindex ) == 0) {
            raise ValueError ( );
        }
         if (minlength { currentsphereindex } { setofspheres } is None) {
            if (eulerlib . popcount ( setofspheres ) == 1) {
                var result = sphereradii { currentsphereindex };
            }
             else{
                result = float ( "inf" );
                newsetofspheres = setofspheres ^ ( 1 << currentsphereindex );
                for i in range ( NUM_SPHERES ) :
                    if (newsetofspheres & ( 1 << i ) == 0) {
                        continue;
                    }
                     temp = math . sqrt ( ( sphereradii { i } + sphereradii { currentsphereindex } - 50000 ) * 200000 );
                    temp += find_minimum_length ( i , newsetofspheres );
                    result = min ( temp , result );
            }
            minlength { currentsphereindex } { setofspheres } = result;
        }
         return minlength { currentsphereindex } { setofspheres };
    }
    var ans = min ( ( find_minimum_length ( i , ( 1 << NUM_SPHERES ) - 1 ) + sphereradii { i } ) for i in range ( NUM_SPHERES ) );
    return str ( int ( round ( ans ) ) );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 