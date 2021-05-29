import sys

with open('sales.txt', 'r', encoding='utf-8') as f:
    sales = (sale for sale in f.read().split('\n'))
    if len(sys.argv) == 1:
        for sale in sales:
            print(sale)
    elif len(sys.argv) == 2:
        count1 = int(sys.argv[1])
        for sale in sales:
            count1 -= 1
            if count1 > 0:
                continue
            else:
                print(sale)
    elif len(sys.argv) == 3:
        count1 = int(sys.argv[1])
        count2 = int(sys.argv[2]) - count1
        for sale in sales:
            count1 -= 1
            if count1 > 0:
                continue
            else:
                print(sale)
                count2 -= 1
                if count2 < 0:
                    break
exit()
