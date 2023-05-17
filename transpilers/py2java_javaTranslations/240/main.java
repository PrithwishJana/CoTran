var bigres = {};
var t = int ( input ( ) );
for m in range ( t ) :
    var n = int ( input ( ) );
    var a = list ( map ( int , input ( ) . strip ( ) . split ( ) ) );
    var res = a { 0 } * a { 1 };
    for q in range ( len ( a ) - 1 ) :
        res = max ( res , ( a { q } * a { q + 1 } ) );
    bigres += { res };
for i in range ( len ( bigres ) ) :
    System.out.println ( bigres { i } );
