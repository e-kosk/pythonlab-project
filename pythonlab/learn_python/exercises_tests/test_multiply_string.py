from learn_python.temp import tmp_exercise, tmp_user

try:
    def test_multiply():
        assert tmp_exercise.multiply_string('a', 10) == tmp_user.multiply_string('a', 10)
        assert tmp_exercise.multiply_string('test ', 1) == tmp_user.multiply_string('test ', 1)
        assert tmp_exercise.multiply_string(-1, 'Abc') == tmp_user.multiply_string(-1, 'Abc')
        assert tmp_exercise.multiply_string(0, '0') == tmp_user.multiply_string(0, '0')
        assert tmp_exercise.multiply_string(15, '15') == tmp_user.multiply_string(15, '15')
except AttributeError:
    pass
