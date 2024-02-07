import re
import numpy

with open('2023/Inputs/Day24.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
offset = 200000000000000 # 7
bound  = 200000000000000 # 20
paths = []
for i, line in enumerate(lines):
    nums = [int(n) for n in re.findall('-?\d+', line)]
    now = (nums[0]-offset, nums[1]-offset)
    yRate = nums[4] / nums[3]
    yCept = now[1] - yRate * now[0]
    xAtYMin = (0 - yCept) / yRate
    xAtYMax = (bound - yCept) / yRate
    xMin = max(min(xAtYMin, xAtYMax), 0)
    xMax = min(max(xAtYMin, xAtYMax), bound)
    if nums[3] > 0:
        xMin = max(xMin, now[0])
    else:
        xMax = min(xMax, now[0])
    paths.append((yRate, yCept, xMin, xMax))
for i, path1 in enumerate(paths):
    for j, path2 in enumerate(paths[i+1:]):
        if path1[0] == path2[0]:
            continue
        x = (path1[1] - path2[1]) / (path2[0] - path1[0])
        #print(path1, path2, x)
        if path1[2] <= x <= path1[3] and path2[2] <= x <= path2[3]:
            sum1 += 1
print(f'1. Answer is: {sum1}') # 12015

# y0 = y1 = b1 * x1 + j1
# z0 = z1 = c1 * x1 + k1
# x0 = x1 = (j0 - j1) / (b1 - b0) = (k0 - k1) / (c1 - c0)
#      x2 = (j0 - j2) / (b2 - b0) = (k0 - k2) / (c2 - c0)
#      x3 = (j0 - j3) / (b3 - b0) = (k0 - k3) / (c3 - c0)
#      x4 = (j0 - j4) / (b4 - b0) = (k0 - k4) / (c4 - c0)
# j0 = (k0 - k1) * (b1 - b0) / (c1 - c0) + j1 = (k0 - k2) * (b2 - b0) / (c2 - c0) + j2
# k0 = ( k1 * (b1 - b0) / (c1 - c0) - k2 * (b2 - b0) / (c2 - c0) + j2 - j1       ) / ( (b1 - b0) / (c1 - c0) - (b2 - b0) / (c2 - c0) )
#    = ( b1*k1/(c1-c0) - b0*k1/(c1-c0) - b2*k2/(c2-c0) + b0*k2/(c2-c0) + j2 - j1 ) / ( b1/(c1-c0) - b0/(c1-c0) - b2/(c2-c0) + b0/(c2-c0) )
#    = ( b0*(k2/(c2-c0)-k1/(c1-c0)) + b1*k1/(c1-c0) - b2*k2/(c2-c0) + j2 - j1 ) / ( b0*(1/(c2-c0)-1/(c1-c0)) + b1/(c1-c0) - b2/(c2-c0) )
# d1 = 1/(c1-c0), d2 = 1/(c2-c0), etc.
#      ( b0*(k2*d2-k1*d1) + b1*k1*d1 - b2*k2*d2 + j2 - j1 ) * ( b0*(d3-d1) + b1*d1 - b3*d3 ) = ( b0*(k3*d3-k1*d1) + b1*k1*d1 - b3*k3*d3 + j3 - j1 ) * ( b0*(d2-d1) + b1*d1 - b2*d2 )
#      b0^2 * (k2*d2-k1*d1)*(d3-d1) + b0 * ((k2*d2-k1*d1)*(b1*d1-b3*d3) + (b1*k1*d1-b2*k2*d2+j2-j1)*(d3-d1)) + (b1*k1*d1-b2*k2*d2+j2-j1)*(b1*d1-b3*d3) = etc.
#      b0^2 * [(k2*d2-k1*d1)*(d3-d1)-(k3*d3-k1*d1)*(d2-d1)] + b0 * [(k2*d2-k1*d1)*(b1*d1-b3*d3) + (b1*k1*d1-b2*k2*d2+j2-j1)*(d3-d1) - (k3*d3-k1*d1)*(b1*d1-b2*d2) - (b1*k1*d1-b3*k3*d3+j3-j1)*(d2-d1)] + ignored_constant = 0
# b0 = [(k3*d3-k1*d1)*(b1*d1-b3*d3) + (b1*k1*d1-b3*k3*d3+j3-j1)*(d2-d1) - (k2*d2-k1*d1)*(b1*d1-b2*d2) - (b1*k1*d1-b2*k2*d2+j2-j1)*(d3-d1)] / (2*[(k2*d2-k1*d1)*(d3-d1)-(k3*d3-k1*d1)*(d2-d1)])
#    = [d3*d1*(k3*b1+k1*b3+k3*b3-k1*b1) + d1*d2*(b1*k1-k2*b1-k1*b2-k2*b2) + d3*d2*(b2*k2-b3*k3) - d3^2*(k3*b3) + d2^2*(k2*b2) - d3*(j2-j1) + d2*(j3-j1) + d1*(j2-j3)] / [d2*d3*(k2-k3) + d1*d3*(k3-k1) - d2*d3*k2 + d1*d2*k1] / 2
# I give up, let's try linear algebra
#-b1*x1 +    y1         = j1
#-b0*x1 +    y1         = j0
#-c1*x1         +    z1 = k1
#-c0*x1         +    z1 = k0
#    x1                 - a1*t1                                                                                                         = i1
#    x1                                                         - a0*t1                                         -    i0                 = 0
#            y1         - b1*t1                                                                                                         = j1
#            y1                                                         - b0*t1                                         -    j0         = 0
#                    z1 - c1*t1                                                                                                         = k1
#                    z1                                                         - c0*t1                                         -    k0 = 0
#                                    x2                 - a2*t2                                                                         = i1
#                                    x2                                                 - a0*t2                 -    i0                 = 0
#                                            y2         - b2*t2                                                                         = j1
#                                            y2                                                 - b0*t2                 -    j0         = 0
#                                                    z2 - c2*t2                                                                         = k1
#                                                    z2                                                 - c0*t2                 -    k0 = 0
# Can I separate a0,b0,c0 from t1,t2,etc.?
# Redo first approach, but solve for j0c0, k0b0 instead of just c0, b0
# x0 = x1 = (j0 - j1) / (b1 - b0) = (k0 - k1) / (c1 - c0)
#           j0*c1 - j0c0 - j1*c1 + j1*c0 = k0*b1 - k0b0 - k1*b1 + k1*b0
#    k0b0 = j0c0 - j0*c1 + k0*b1 + b0*k1 - c0*j1 + (j1*c1-k1*b1) = j0c0 - j0*c2 + k0*b2 + b0*k2 - c0*j2 + (j2*c2-k2*b2)
#           j0*(c2-c1) + k0*(b1-b2) + b0*(k1-k2) + c0*(j2-j1) + (j1*c1-k1*b1-j2*c2+k2*b2) = 0
#      j0 = k0*(b2-b1)/(c2-c1) + b0*(k2-k1)/(c2-c1) + c0*(j1-j2)/(c2-c1) - (j1*c1-k1*b1-j2*c2+k2*b2)/(c2-c1) = etc.
# Back to linear algebra
#           b0*(k1-k2) + c0*(j2-j1) + j0*(c2-c1) + k0*(b1-b2) = -(j1*c1-k1*b1-j2*c2+k2*b2)
#           b0*(k1-k3) + c0*(j3-j1) + j0*(c3-c1) + k0*(b1-b3) = -(j1*c1-k1*b1-j3*c3+k3*b3)
#           b0*(k1-k4) + c0*(j4-j1) + j0*(c4-c1) + k0*(b1-b4) = -(j1*c1-k1*b1-j4*c4+k4*b4)
#           b0*(k1-k5) + c0*(j5-j1) + j0*(c5-c1) + k0*(b1-b5) = -(j1*c1-k1*b1-j5*c5+k5*b5) # Do I really need this 5th line? Does it resolve the qudratic-ness of k0b0 and j0c0?
# Not abstracting away time
# x0 = x1 = a1 * t1 + i1
# y0 = y1 = b1 * t1 + j1
# z0 = z1 = c1 * t1 + k1
# t0 = t1 = (j0 - j1) / (b1 - b0) = (k0 - k1) / (c1 - c0)
#           j0*c1 - j0c0 - j1*c1 + j1*c0 = k0*b1 - k0b0 - k1*b1 + k1*b0
#           i0*c1 - i0c0 - i1*c1 + i1*c0 = k0*a1 - k0a0 - k1*a1 + k1*a0
#           i0*b1 - i0b0 - i1*b1 + i1*b0 = j0*a1 - j0a0 - j1*a1 + j1*a0
#                        j0*(c2-c1) + k0*(b1-b2)              + b0*(k1-k2) + c0*(j2-j1) = -(j1*c1-j2*c2+k2*b2-k1*b1)
#           i0*(c2-c1)              + k0*(a1-a2) + a0*(k1-k2)              + c0*(i2-i1) = -(i1*c1-i2*c2+k2*a2-k1*a1)
#           i0*(b2-b1) + j0*(a1-a2)              + a0*(j1-j2) + b0*(i2-i1)              = -(i1*b1-i2*b2+j2*a2-j1*a1)
#                        j0*(c3-c1) + k0*(b1-b3)              + b0*(k1-k3) + c0*(j3-j1) = -(j1*c1-j3*c3+k3*b3-k1*b1)
#           i0*(c3-c1)              + k0*(a1-a3) + a0*(k1-k3)              + c0*(i3-i1) = -(i1*c1-i3*c3+k3*a3-k1*a1)
#           i0*(b3-b1) + j0*(a1-a3)              + a0*(j1-j3) + b0*(i3-i1)              = -(i1*b1-i3*b3+j3*a3-j1*a1)
path1 = [int(n) for n in re.findall('-?\d+', lines[0])]
path2 = [int(n) for n in re.findall('-?\d+', lines[1])]
path3 = [int(n) for n in re.findall('-?\d+', lines[2])]
A = numpy.array([[                0, path2[5]-path1[5], path1[4]-path2[4],                 0, path1[2]-path2[2], path2[1]-path1[1]],
                 [path2[5]-path1[5],                 0, path1[3]-path2[3], path1[2]-path2[2],                 0, path2[0]-path1[0]],
                 [path2[4]-path1[4], path1[3]-path2[3],                 0, path1[1]-path2[1], path2[0]-path1[0],                 0], 
                 [                0, path3[5]-path1[5], path1[4]-path3[4],                 0, path1[2]-path3[2], path3[1]-path1[1]],
                 [path3[5]-path1[5],                 0, path1[3]-path3[3], path1[2]-path3[2],                 0, path3[0]-path1[0]],
                 [path3[4]-path1[4], path1[3]-path3[3],                 0, path1[1]-path3[1], path3[0]-path1[0],                 0]])
b = numpy.array([path2[1]*path2[5] - path1[1]*path1[5] + path1[2]*path1[4] - path2[2]*path2[4],
                 path2[0]*path2[5] - path1[0]*path1[5] + path1[2]*path1[3] - path2[2]*path2[3],
                 path2[0]*path2[4] - path1[0]*path1[4] + path1[1]*path1[3] - path2[1]*path2[3],
                 path3[1]*path3[5] - path1[1]*path1[5] + path1[2]*path1[4] - path3[2]*path3[4],
                 path3[0]*path3[5] - path1[0]*path1[5] + path1[2]*path1[3] - path3[2]*path3[3],
                 path3[0]*path3[4] - path1[0]*path1[4] + path1[1]*path1[3] - path3[1]*path3[3]])
rock = numpy.linalg.solve(A, b)
print(f'2. Answer is: {round(sum(rock[0:3]))}') # 1016365642179116
print(f'2.   Rock is: {rock}')