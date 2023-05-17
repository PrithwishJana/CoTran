var n = int ( input ( ) );
var mat = { [ } for i in range ( n ) ];
var b = { int ( j ) - 1 for j in str ( input ( ) ) . split ( ' ' ) };
for i in range ( n ) :
    mat { i } . append ( b { i } );
var i = 0;
h = '';
i = 0;
while (i < n) {
    l = { 0 for j in range ( n ) };
    a = i;
    while (true) {
        l { a } += 1;
        if (l { a } > 1) {
            break;
        }
         a = mat { a } { 0 };
    }
     m = 0;
    j = 0;
    while (j < n) {
        if (l { j } > m) {
            m = l { j };
            x = j + 1;
        }
         j = j + 1;
    }
     h = h + str ( x ) + ' ';
    i = i + 1;
}
 System.out.println ( h );
