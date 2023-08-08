nums=[3,4,2,5,2,1,1,1]
# def majority():
m_count=0
for i in range(len(nums)):
        count=1
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                count=count+1
        if count>m_count :
            m_count=count
            a=i
if m_count>len(nums)/2:
        print(nums[i])               
# majority()




