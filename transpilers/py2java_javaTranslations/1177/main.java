if (var __name__ == '__main__') {
    var line = input ( ) . split ( );
    n , m , k = int ( line { 0 } ) , int ( line { 1 } ) , int ( line { 2 } { 2 : } );
    skills = {};
    for _ in range ( n ) :
        line = input ( ) . split ( );
        skills { line [ 0 } ] = int ( line { 1 } );
    var new_skills = { input ( ) for _ in range ( m ) };
    var count = 0;
    var delete = {};
    for key , value in skills . items ( ) :
        var value = int ( k * value / 100 );
        if (value < 100) {
            delete . append ( key );
        }
         else{
            skills { key } = value;
            count += 1;
        }
    for (int key = 0; key < delete.length; key++){
        del skills { key };
    }
    for (int skill = 0; skill < new_skills.length; skill++){
        if (skill not in skills . keys ( )) {
            skills { skill } = 0;
            count += 1;
        }
    }
     var skills = dict ( sorted ( skills . items ( ) ) );
    System.out.println ( count );
    for key , value in skills . items ( ) :
        System.out.println ( key , value , var sep = ' ' );
}
 