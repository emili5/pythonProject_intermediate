# emili2020=['emili',('woman','Korea'),[170,21]]
# #emili2021=['emili',('woman','Korea'),[172,22]] 로 변경하고 싶음
#
# emili2021=list(emili2020)
# emili2021[2][0]+=2
# emili2021[2][1]+=1
# print(emili2021)

emili2020=['emili',('woman','Korea'),[170,21]]
import copy
emili2021=copy.deepcopy(emili2020)
emili2021[2][0]+=2
emili2021[2][1]+=1
print(emili2021)
print(emili2020 is emili2021)
print(emili2021[0] is emili2020[0])
print(emili2021[2] is emili2020[2])