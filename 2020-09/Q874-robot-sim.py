# -*- coding:utf-8 -*-
# @Time : 2020/9/4 21:49 
# @Author : bendan50
# @File : Q874-robot-sim.py 
# @Function : 模拟行走机器人
# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。
# 该机器人可以接收以下三种类型的命令：
# -2：向左转 90 度
# -1：向右转 90 度
# 1 <= x <= 9：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物。
# 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。
# 示例 1：
# 输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
# 示例 2：
# 输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
# 提示：
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# 答案保证小于 2 ^ 31
# @Software: PyCharm

from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        思路：需要返回离原点最远的距离。只需要计算每步后距离原点的距离，若比保存值大则更新。
        类似贪心算法思想，只需要考虑当前。
        下面的代码结果为：超出时间限制！！！
        因为我对obstacles进行了每一步的遍历，可优化为对其进行字典集合式的存储来提高效率。
        这利用了题设，具体代码详见self.robot_Sim(
        :param commands:
        :param obstacles:
        :return:
        """
        d_list = ['UP','RIGHT','DOWN','LEFT']
        d_idx = 0
        d = d_list[d_idx]
        max_val = 0
        x,y = 0,0
        obs_size = len(obstacles)
        for com in commands:
            if com == -1:
                d_idx = (d_idx + 1) % 4
                d = d_list[d_idx]
            elif com == -2:
                d_idx = (d_idx - 1) %4
                d = d_list[d_idx]
            else:
                if d == 'UP':
                    area = [y,y+com]
                    tmp = y + com
                    for obs in range(obs_size):
                        if obstacles[obs][0] == x and obstacles[obs][1] > y and obstacles[obs][1] <= tmp:
                            tmp = min(tmp,obstacles[obs][1]-1)
                    y = tmp
                    max_val = max(max_val,x**2+y**2)
                    pass
                elif d == 'RIGHT':
                    area = [x,x+com]
                    tmp = x + com
                    for obs in range(obs_size):
                        ele = obstacles[obs]
                        if ele[1] == y and ele[0] > x and ele[0] <= tmp:
                            tmp = min(tmp,ele[0]-1)
                    x = tmp
                    max_val = max(max_val,x**2+y**2)
                    pass
                elif d == 'DOWN':
                    area = [y-com,y]
                    tmp = y-com
                    for obs in range(obs_size):
                        ele = obstacles[obs]
                        if ele[0] == x and ele[1] >= tmp and ele[1] < y:
                            tmp = max(tmp,ele[1] + 1)
                    y = tmp
                    max_val = max(max_val,x**2+y**2)
                    pass
                elif d == 'LEFT':
                    area = [x-com,x]
                    tmp = x-com
                    for obs in range(obs_size):
                        ele = obstacles[obs]
                        if ele[1] == y and ele[0] >= tmp and ele[0] < x:
                            tmp = max(tmp,ele[0] + 1)
                    x = tmp
                    max_val = max(max_val,x**2+y**2)
                    pass
        pass
        return max_val

    def robot_Sim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #优化一：移动方向字符串数组变成坐标改变的数值。
        d_list = ['UP','RIGHT','DOWN','LEFT']
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        x,y,d_idx = 0,0,0
        max_val = 0
        obs_set = set(map(tuple,obstacles))     #优化二：储存
        for cmd in commands:
            if cmd == -1:
                d_idx = (d_idx + 1) % 4
            elif cmd == -2:
                d_idx = (d_idx - 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[d_idx], y + dy[d_idx]) in obs_set:
                        break
                    else:
                        x += dx[d_idx]
                        y += dy[d_idx]
                max_val = max(max_val,x*x+y*y)
        return max_val

if __name__ == "__main__":
    cmds = [4,-1,3]
    obs = []
    ret = Solution().robot_Sim(cmds,obs)
    print('ret = {}'.format(ret))
