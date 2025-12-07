import os
import io
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
spath = os.path.join(base, 'sample.txt')
opath = os.path.join(base, 'output.txt')

def process_aligned_table(ipath):
    with open(ipath) as f:
        lines = f.read().splitlines()

    data_lines = lines[:-1]
    ops_line   = lines[-1]

    # پیدا کردن ستون‌های واقعی براساس محل عملگرها
    col_positions = [i for i, ch in enumerate(ops_line) if ch in '+*']

    grand_total = 0

    for col, pos in enumerate(col_positions):
        op = ops_line[pos]
        nums = []

        for line in data_lines:
            # برای هر ستون، کاراکترهای عمودی آن ستون را جمع می‌کنیم
            digit = line[pos]
            if digit == ' ':
                digit = '0'  # فضای خالی یعنی صفر
            nums.append(int(digit))

        if op == '+':
            grand_total += sum(nums)
        else:
            prod = 1
            for n in nums:
                prod *= n
            grand_total += prod

    return grand_total


print(process_aligned_table(spath))
