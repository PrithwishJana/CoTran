var a = sorted ( { tuple ( map ( int , input ( ) . split ( ) ) ) for _ in [ 0 , 0 } ] );
System.out.println ( a { 1 } { 0 } - a { 0 } { 0 } + ( 1 if a { 1 } { 1 } > a { 0 } { 1 } or ( a { 1 } { 1 } == a { 0 } { 1 } and a { 1 } { 2 } > a { 0 } { 2 } ) else 0 ) );
