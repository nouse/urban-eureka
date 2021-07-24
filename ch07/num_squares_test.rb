require "minitest/autorun"
require_relative "num_squares"

class TestMeme < Minitest::Test
  def test_num_squares
    assert_equal 1, num_squares(16)
    assert_equal 2, num_squares(13)
    assert_equal 3, num_squares(12)
    assert_equal 4, num_squares(15)
  end
end