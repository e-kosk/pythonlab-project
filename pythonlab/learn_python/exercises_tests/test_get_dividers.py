from learn_python.temp import tmp_exercise, tmp_user

try:
    def test_multiply():
        assert tmp_exercise.get_dividers(20) == tmp_user.get_dividers(20)
        assert tmp_exercise.get_dividers(-20) == tmp_user.get_dividers(-20)
        assert tmp_exercise.get_dividers(0) == tmp_user.get_dividers(0)
        assert tmp_exercise.get_dividers(1) == tmp_user.get_dividers(1)
        assert tmp_exercise.get_dividers(-2) == tmp_user.get_dividers(-2)
except AttributeError:
    pass
