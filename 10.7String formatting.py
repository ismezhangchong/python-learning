a=23.60*.25
print('The tip is {:.2f}'.format(a))
bill =23.60
tip =23.60*.25
print('Tip:${:.2f},Total:${:.2f}'.format(tip,bill+tip))

#整数格式{:d}
print('{:5d}'.format(2))
print('{:5d}'.format(25))
print('{:5d}'.format(138))
#juzhong
print('{:^5d}'.format(2))
print('{:^5d}'.format(222))
print('{:^5d}'.format(13834))
#zuoweiqi
print('{:<5d}'.format(2))
print('{:<5d}'.format(222))
print('{:<5d}'.format(13834))
#,格式化整数
print('{:,d}'.format(1000000),'\n')

#formatting float(浮点数的格式)   {:f}
print('{:.2f}'.format(a))
print('{:.2f}'.format(4.666643))
print('\n')
'''{:.2f}精确到百分位
              {:.8.2f}对齐,厕所坑位机制'''
print('{:8.2f}'.format(2))
print('{:8.2f}'.format(2.22))
print('{:8.2f}'.format(13.834))
#^,<是居中和左对齐

#formatting strings   {:s}
print('{:^10s}'.format('Hi'))
print('{:^10s}'.format('There!'))
print('To right-justify a string,use the > character:')
print('{:>6s}'.format('Hi'))
print('{:>6s}'.format('There!'))
