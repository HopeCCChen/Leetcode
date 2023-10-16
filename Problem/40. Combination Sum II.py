

class Solution:
    answer_list=[]

    def run(self, candidates, target,summ,ans_array):

        for index, value in enumerate(candidates):
            #remove the used data
            temp_array = candidates[index+1:]
            temp_sum= summ+candidates[index]
            temp_ans=ans_array.copy()
            temp_ans.append(value)

            if(temp_sum >= target):
                if(temp_sum==target):
                    # find the answer
                    if(temp_ans  not in self.answer_list):
                        self.answer_list.append(temp_ans)
                else:
                    # temp_sum> target
                    break
            else:
                #not yet
                if(index>0 and candidates[index] == candidates[index-1]):
                    continue
                else:
                    self.run(temp_array,target,temp_sum,temp_ans)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer_list=[]
        candidates= sorted(candidates)
        self.run(candidates,target,0,[])
        return  self.answer_list

