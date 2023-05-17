import collections.Counter;
public void main ( ) {
    var n = int ( input ( ) );
    var aa = list ( map ( int , input ( ) . split ( ) ) );
    var cs_a0 = Counter ( a for i , a in enumerate ( aa ) if i % 2 == 0 );
    var cs_a1 = Counter ( a for i , a in enumerate ( aa ) if i % 2 == 1 );
    var vs_a0 = sorted ( ( ( v , k ) for k , v in cs_a0 . items ( ) ) , reverse = true );
    var vs_a1 = sorted ( ( ( v , k ) for k , v in cs_a1 . items ( ) ) , reverse = true );
    if (vs_a0 { 0 } { 1 } != vs_a1 { 0 } { 1 }) {
        System.out.println ( n - vs_a0 { 0 } { 0 } - vs_a1 { 0 } { 0 } );
    }
     else{
        var res = 1 << 30;
        if (len ( vs_a0 ) == 1 and len ( vs_a1 ) == 1) {
            res = n // 2;
        }
         if (len ( vs_a0 ) > 1) {
            res = min ( res , n - vs_a0 { 1 } { 0 } - vs_a1 { 0 } { 0 } );
        }
         if (len ( vs_a1 ) > 1) {
            res = min ( res , n - vs_a0 { 0 } { 0 } - vs_a1 { 1 } { 0 } );
        }
         System.out.println ( res );
    }
}
if (var __name__ == "__main__") {
    main ( );
}
 