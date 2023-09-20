N = input()
set flag = true
for Q from 2 to ( round_up( squareroot(N) )) do
   if remainder of N divided by Q == 0 then
      set flag = false
   end if
end for
if flag is true then
   output "yes"
else
   output "no"
