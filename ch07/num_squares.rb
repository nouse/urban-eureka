# frozen_string_literal: true

require 'prime'

# start snippet wow
def num_squares(n)
  # 首先对n反复除以4，去掉4^a的部分
  n /= 4 while n % 4 == 0
  # 验证n是否是完全平方数
  return 1 if (Math.sqrt(n).floor ** 2) == n
  # 验证n是否满足4^a(8b+7)的形式
  return 4 if n % 8 == 7
  # 对n作因数分解，如果4b+3形式的素数因数的幂有至少一个奇数，返回3。
  return 3 if n.prime_division.any? do |p, e|
    p % 4 == 3 && e.odd?
  end
  # 其他情况返回2
  return 2
end
# end snippet wow
