# // package Take 2;

# public class getMaxBarriers {
#     static int getMaxBarrier(int initialEnergy[], int th) {
#         // This method returns maximum value of a barrier such that final
#         // sum of energies is greater than or equal to given threshold (th)
      
#         // declare and initialize required variables
#         int ans = 0, sum = 0;
#         // binary searching for the result
#         int s = 0, e = Integer.MAX_VALUE;
#         while (s < e) {
#           int mid = (s + e) / 2;
#           // assume mid as the value of barrier and calculate the sum
#           sum = 0;
#           for (int i = 0; i < initialEnergy.length; i++)
#             sum += Math.max(initialEnergy[i] - mid, 0);
#           // if sum greater than th, search in the range [mid + 1, e)
#           if (sum >= th) {
#             ans = Math.max(ans, mid);
#             s = mid + 1;
#           }
#           // else, search in the range [e, mid)
#           else {
#             e = mid;
#           }
#         }
#         // return ans
#         return ans;
#        }
# }

def solution(initialEnergy, th):
  ans,sum,s=0,0,0
  e = 100000000
  while (s < e):
    mid = (s + e) // 2
    sum = 0
    for i in range(len(initialEnergy)):
      sum+=max(initialEnergy[i] - mid,0)
    if (sum>=th):
      ans = max(ans,mid)
      s = mid + 1
    else:
      e = mid
  return ans

print(solution([5,2,13,10], 8))