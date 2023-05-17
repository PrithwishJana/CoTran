var n = int ( input ( ) );
var lst = { list ( map ( int , input ( ) . split ( ) ) ) for _ in range ( n ) };
var a_start = { x [ 0 } * 60 + x { 1 } for x in lst ];
var a_end = { x [ 2 } * 60 + x { 3 } for x in lst ];
var h_start = { x [ 4 } * 60 + x { 5 } for x in lst ];
var h_end = { x [ 6 } * 60 + x { 7 } for x in lst ];
var b_start = { x [ 8 } * 60 + x { 9 } for x in lst ];
var b_end = { x [ 10 } * 60 + x { 11 } for x in lst ];
public void make_sets ( start , end ) {
    var sets = {};
    member = {};
    for i in range ( 1440 ) :
        upd = false;
        for j in range ( n ) :
            if (start { j } == i) {
                member . append ( j );
                upd = true;
            }
             if (end { j } == i - 1) {
                member . remove ( j );
                upd = true;
            }
         if (upd) {
            sets . append ( set ( member ) );
        }
     return sets;
}
a_sets = make_sets ( a_start , a_end );
h_sets = make_sets ( h_start , h_end );
b_sets = make_sets ( b_start , b_end );
var ans = 0;
for (int s1 = 0; s1 < a_sets.length; s1++){
    for (int s2 = 0; s2 < h_sets.length; s2++){
        for (int s3 = 0; s3 < b_sets.length; s3++){
            ans = max ( ans , len ( s1 & s2 & s3 ) );
        }
    }
}
System.out.println ( ans );
