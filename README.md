ES load <acc> number -> accumulator load
ES push <acc> -> stack save
...ASSEMBLY

Analyzed 
    "xor and print"  -->  stack xor "something"
    searched for series, "something" is a Palindromic prime
    3 chunks with respective indexes in Palindromic prime serie
    a^b, a=Palindromic prime [from index..], b=stack
    acc1 used to fill stack, acc2=(index of serie) 

CHUNK_1
acc2=1
    stack [0, 17488, 16758, 16599, 16285, 16094, 15505, 15417, 14832, 14450, 13893, 13926, 13437, 12833, 12741, 12533, 11504, 11342, 10503, 10550, 10319, 975, 1007, 892, 893, 660, 743, 267, 344, 264, 339, 208, 216, 242, 172, 74, 49, 119, 113, 119, 1, 104]

    serie [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929, 10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551, 16061, 16361, 16561, 16661, 17471, 17971, 18181]
 
    [11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551, 16061, 16361, 16561, 16661, 17471] 
    ^ 
    [11504, 12533, 12741, 12833, 13437, 13926, 13893, 14450, 14832, 15417, 15505, 16094, 16285, 16599, 16758, 17488]
    =
    [99, 112, 116, 52, 110, 97, 46, 119, 101, 98, 46, 99, 116, 102, 99, 111]
    [cpt4na.web.ctfco ]

    http://emoji-t0anaxnr3nacpt4na.web.ctfco

load 1 0️⃣ ✋ push 1
load 1 1️⃣ 7️⃣ 4️⃣ 8️⃣ 8️⃣ ✋ push 1
load 1 1️⃣ 6️⃣ 7️⃣ 5️⃣ 8️⃣ ✋ push 1
load 1 1️⃣ 6️⃣ 5️⃣ 9️⃣ 9️⃣ ✋ push 1
load 1 1️⃣ 6️⃣ 2️⃣ 8️⃣ 5️⃣ ✋ push 1
load 1 1️⃣ 6️⃣ 0️⃣ 9️⃣ 4️⃣ ✋ push 1
load 1 1️⃣ 5️⃣ 5️⃣ 0️⃣ 5️⃣ ✋ push 1
load 1 1️⃣ 5️⃣ 4️⃣ 1️⃣ 7️⃣ ✋ push 1
load 1 1️⃣ 4️⃣ 8️⃣ 3️⃣ 2️⃣ ✋ push 1
load 1 1️⃣ 4️⃣ 4️⃣ 5️⃣ 0️⃣ ✋ push 1
load 1 1️⃣ 3️⃣ 8️⃣ 9️⃣ 3️⃣ ✋ push 1
load 1 1️⃣ 3️⃣ 9️⃣ 2️⃣ 6️⃣ ✋ push 1
load 1 1️⃣ 3️⃣ 4️⃣ 3️⃣ 7️⃣ ✋ push 1
load 1 1️⃣ 2️⃣ 8️⃣ 3️⃣ 3️⃣ ✋ push 1
load 1 1️⃣ 2️⃣ 7️⃣ 4️⃣ 1️⃣ ✋ push 1
load 1 1️⃣ 2️⃣ 5️⃣ 3️⃣ 3️⃣ ✋ push 1
load 1 1️⃣ 1️⃣ 5️⃣ 0️⃣ 4️⃣ ✋ push 1          11411
load 1 1️⃣ 1️⃣ 3️⃣ 4️⃣ 2️⃣ ✋ push 1       a   11311
load 1 1️⃣ 0️⃣ 5️⃣ 0️⃣ 3️⃣ ✋ push 1       n  10601
load 1 1️⃣ 0️⃣ 5️⃣ 5️⃣ 0️⃣ ✋ push 1       3   10501
load 1 1️⃣ 0️⃣ 3️⃣ 1️⃣ 9️⃣ ✋ push 1       r  10301 
load 1 9️⃣ 7️⃣ 5️⃣ ✋ push 1              n 929
load 1 1️⃣ 0️⃣ 0️⃣ 7️⃣ ✋ push 1           x 919
load 1 8️⃣ 9️⃣ 2️⃣ ✋ push 1              a 797
load 1 8️⃣ 9️⃣ 3️⃣ ✋ push 1              n 787
load 1 6️⃣ 6️⃣ 0️⃣ ✋ push 1              a 757
load 1 7️⃣ 4️⃣ 3️⃣ ✋ push 1              0 727
load 1 2️⃣ 6️⃣ 7️⃣ ✋ push 1              t 383
load 1 3️⃣ 4️⃣ 4️⃣ ✋ push 1              - 373 
load 1 2️⃣ 6️⃣ 4️⃣ ✋ push 1              i 353
load 1 3️⃣ 3️⃣ 9️⃣ ✋ push 1              j 313
load 1 2️⃣ 0️⃣ 8️⃣ ✋ push 1              o 191
load 1 2️⃣ 1️⃣ 6️⃣ ✋ push 1              m 181
load 1 2️⃣ 4️⃣ 2️⃣ ✋ push 1              e 151
load 1 1️⃣ 7️⃣ 2️⃣ ✋ push 1              / 131
load 1 7️⃣ 4️⃣ ✋ push 1                 / 101
load 1 4️⃣ 9️⃣ ✋ push 1                 : 11
load 1 1️⃣ 1️⃣ 9️⃣ ✋ push 1              p 7
load 1 1️⃣ 1️⃣ 3️⃣ ✋ push 1              t 5
load 1 1️⃣ 1️⃣ 9️⃣ ✋ push 1              t 3
load 1 1️⃣ 0️⃣ 6️⃣ ✋ push 1              h 2
load 2 1️⃣ ✋

--label--
pop 1 push 2 push 1 
load 1 3️⃣ 8️⃣ 9️⃣ ✋
push 1 push 2
jump_to 💰                          //jmp to this func returning Palindromic prime
xor print_top                       // xor acc2 and return of 💰
load 1 1️⃣ ✋ push 1 add pop 2
if_not_zero jump_to 💰  😐

load 1 9️⃣ 8️⃣ 4️⃣ 2️⃣ 6️⃣ ✋ push 1
load 1 9️⃣ 7️⃣ 8️⃣ 5️⃣ 0️⃣ ✋ push 1
load 1 9️⃣ 7️⃣ 6️⃣ 0️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 7️⃣ 2️⃣ 8️⃣ 0️⃣ ✋ push 1
load 1 9️⃣ 6️⃣ 8️⃣ 1️⃣ 5️⃣ ✋ push 1
load 1 9️⃣ 6️⃣ 4️⃣ 4️⃣ 3️⃣ ✋ push 1
load 1 9️⃣ 6️⃣ 3️⃣ 5️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 5️⃣ 9️⃣ 3️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 4️⃣ 8️⃣ 6️⃣ 5️⃣ ✋ push 1
load 1 9️⃣ 4️⃣ 9️⃣ 5️⃣ 2️⃣ ✋ push 1
load 1 9️⃣ 4️⃣ 6️⃣ 6️⃣ 9️⃣ ✋ push 1
load 1 9️⃣ 4️⃣ 4️⃣ 4️⃣ 0️⃣ ✋ push 1
load 1 9️⃣ 3️⃣ 9️⃣ 6️⃣ 9️⃣ ✋ push 1
load 1 9️⃣ 3️⃣ 7️⃣ 6️⃣ 6️⃣ ✋ push 1
load 2 9️⃣ 9️⃣ ✋                   //index 99

http://emoji-t0anaxnr3nacpt4na.web.ctfco
PalindromicPrime[99-1+i], i=[1-len(stack)]

stack    [98426, 97850, 97604, 97280, 96815, 96443, 96354, 95934, 94865, 94952, 94669, 94440, 93969, 93766]
stackrev [93766, 93969, 94440, 94669, 94952, 94865, 95934, 96354, 96443, 96815, 97280, 97604, 97850, 98426]
^
serie    [93739, 94049, 94349, 94649, 94849, 94949, 95959, 96269, 96469, 96769, 97379, 97579, 97879, 98389]
= mpetition.com/
http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/

--label--  pop 1 push 2 push 1 load 1 5️⃣ 6️⃣ 8️⃣ ✋
push 1 push 2
jump_to 💰 
xor print_top
load 1 1️⃣ ✋ push 1 add pop 2
if_not_zero jump_to 💰  😐

load 1 1️⃣ 0️⃣ 1️⃣ 1️⃣ 4️⃣ 1️⃣ 0️⃣ 5️⃣ 8️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 1️⃣ 0️⃣ 6️⃣ 0️⃣ 2️⃣ 0️⃣ 6️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 1️⃣ 0️⃣ 3️⃣ 0️⃣ 0️⃣ 5️⃣ 5️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 9️⃣ 9️⃣ 8️⃣ 9️⃣ 6️⃣ 6️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 8️⃣ 8️⃣ 7️⃣ 9️⃣ 9️⃣ 0️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 7️⃣ 6️⃣ 7️⃣ 0️⃣ 8️⃣ 5️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 7️⃣ 0️⃣ 7️⃣ 0️⃣ 3️⃣ 6️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 6️⃣ 5️⃣ 6️⃣ 1️⃣ 1️⃣ 1️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 4️⃣ 0️⃣ 4️⃣ 0️⃣ 9️⃣ 4️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 1️⃣ 6️⃣ 0️⃣ 9️⃣ 2️⃣ 2️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 1️⃣ 3️⃣ 1️⃣ 0️⃣ 1️⃣ 9️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 1️⃣ 1️⃣ 1️⃣ 1️⃣ 0️⃣ 0️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 0️⃣ 5️⃣ 9️⃣ 9️⃣ 2️⃣ 6️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 0️⃣ 4️⃣ 9️⃣ 9️⃣ 8️⃣ 2️⃣ ✋ push 1
load 1 1️⃣ 0️⃣ 0️⃣ 0️⃣ 3️⃣ 0️⃣ 0️⃣ 4️⃣ 5️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 8️⃣ 9️⃣ 9️⃣ 9️⃣ 7️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 8️⃣ 1️⃣ 8️⃣ 5️⃣ 8️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 8️⃣ 0️⃣ 8️⃣ 1️⃣ 5️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 7️⃣ 8️⃣ 8️⃣ 4️⃣ 2️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 6️⃣ 5️⃣ 7️⃣ 9️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 5️⃣ 7️⃣ 5️⃣ 6️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 3️⃣ 8️⃣ 3️⃣ 0️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 3️⃣ 5️⃣ 4️⃣ 2️⃣ 7️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 3️⃣ 2️⃣ 2️⃣ 8️⃣ 9️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 3️⃣ 1️⃣ 4️⃣ 9️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 2️⃣ 7️⃣ 3️⃣ 8️⃣ 8️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 2️⃣ 6️⃣ 3️⃣ 7️⃣ 6️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 2️⃣ 3️⃣ 2️⃣ 1️⃣ 3️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 2️⃣ 1️⃣ 3️⃣ 9️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 1️⃣ 9️⃣ 1️⃣ 5️⃣ 4️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 1️⃣ 8️⃣ 0️⃣ 8️⃣ 2️⃣ ✋ push 1
load 1 9️⃣ 9️⃣ 1️⃣ 6️⃣ 2️⃣ 3️⃣ 9️⃣ ✋ push 1
load 2 7️⃣ 6️⃣ 5️⃣ ✋                                 //index 765

serie [9916199, 9918199, 9919199, 9921299, 9923299, 9926299, 9927299, 9931399, 9932399, 9935399, 9938399, 9957599, 9965699, 9978799, 9980899, 9981899, 9989899, 100030001, 100050001, 100060001, 100111001, 100131001, 100161001, 100404001, 100656001, 100707001, 100767001, 100888001, 100999001, 101030101, 101060101, 101141101, 101171101, 101282101, 101292101]

stack [9916239, 9918082, 9919154, 9921394, 9923213, 9926376, 9927388, 9931494, 9932289, 9935427, 9938304, 9957564, 9965794, 9978842, 9980815, 9981858, 9989997, 100030045, 100049982, 100059926, 100111100, 100131019, 100160922, 100404094, 100656111, 100707036, 100767085, 100887990, 100998966, 101030055, 101060206, 101141058]

result [104, 117, 109, 97, 110, 115, 95, 97, 110, 100, 95, 99, 97, 117, 108, 105, 102, 108, 111, 119, 101, 114, 115, 95, 110, 101, 116, 119, 111, 114, 107, 47]

http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/

--label--  pop 1 push 2 push 1 load 1 1️⃣ 0️⃣ 2️⃣ 3️⃣ ✋
push 1 push 2
jump_to 💰 
xor print_top
load 1 1️⃣ ✋ push 1 add pop 2
if_not_zero jump_to 💰  😐
exit

--label-- 
load 1 2️⃣ ✋ push 1 --label-- 
jump_to 💰 
--label--  if_zero pop_out jump_to 💰  ✋   
pop_out jump_to 💰 
--label--  if_zero pop_out jump_to 💰  😐
pop_out pop 1 load 2 1️⃣ ✋ push 2 sub
if_zero pop_out pop 2 push 1 push 2 jump_top 😐 push 1
--label--  load 2 1️⃣ ✋ push 2 add jump_to 💰 

--label-- 
clone load 1 2️⃣ ✋ push 1
--label--  sub if_zero pop_out load 1 1️⃣ ✋ push 1
jump_to 💰  😐
pop_out clone push 1
modulo if_zero jump_to 💰  😐
pop_out clone push 1 load 1 1️⃣ ✋
push 1 add clone pop 1 jump_to 💰 

--label-- 
clone clone load 2 0️⃣ ✋ push 2
--label--  load 1 1️⃣ 0️⃣ ✋ push 1
multiply pop 2 push 1 modulo
push 2 add pop 2 pop 1 clone push 2 sub
if_zero pop_out load 2 1️⃣ ✋ push 2 jump_to 💰  😐
pop_out push 1 load 1 1️⃣ 0️⃣ ✋ push 1 divide
if_zero jump_to 💰  😐
clone push 2 jump_to 💰 
