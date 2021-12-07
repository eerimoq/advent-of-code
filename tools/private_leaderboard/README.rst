.. code-block:: text

   mys build
   ./build/speed/app ../../api.json 7 | sort -n -k 3 | awk 'BEGIN {i=1} {printf("%d) %s\n", i, $0) ; i++}' 
