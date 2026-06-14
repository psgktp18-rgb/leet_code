class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        a=[]
        for i in hours:
            if i>=target:
                a.append(i)
            else:
                continue
        return len(a)