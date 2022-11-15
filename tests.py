from interpreterv3 import Interpreter

test10 = [
'func ifunc n:int int',
' return n',
'endfunc',
'',
'func sfunc s:string string',
' return s',
'endfunc',
'',
'func bfunc b:bool bool',
' return b',
'endfunc',
'',
'func main void',
'  var int i',
'  var string s',
'  var bool b',
'  var func f g h',
'  assign f ifunc',
'  assign g sfunc',
'  assign h bfunc',
'',
'  funccall f 42',
'  assign i resulti',
'  funccall print i',
'',
'  funccall g "foo"',
'  assign s results',
'  funccall print s',
'',
'  funccall h True',
'  assign b resultb',
'  funccall print b',
'',
'endfunc',
]

test = [
'func main void',
' var func a',
' assign a foo',
'endfunc',
'',
'func foo void',
' return',
'endfunc'
]

machine = Interpreter()
machine.run(test10)