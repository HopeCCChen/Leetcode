class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        dp = [[ 0 for _ in range(s_len+1)] for _ in range( p_len+1)]

        #Step 1
        dp[0][0] =True
        # "" compare ""

        #Step2
        for index in range(1,s_len+1,1):
            dp[0][index] = False

        #Step3 
        for index in range(1,p_len+1,1):
            dp[index][0] = dp[index-1][0] and p[index-1]=='*'
            #s='' p="********"
        #Step 4

        for p_index  in range(1,p_len+1,1):
            for s_index  in range(1,s_len+1,1):
                    if(p[p_index-1] == '*'):
                        dp[p_index][s_index] = dp[p_index-1][s_index]  or dp[p_index][s_index-1]

                    elif(s[s_index-1] == p[p_index-1]) or(p[p_index-1] == '?'): 
                        # char=char or char = ?
                        dp[p_index][s_index] = dp[p_index-1][s_index-1]


                    else:
                        dp[p_index][s_index] = False
        #print(dp)
        return dp[p_len][s_len] 
