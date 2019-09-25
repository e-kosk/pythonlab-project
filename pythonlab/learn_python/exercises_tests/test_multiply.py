from learn_python.temp import tmp_exercise, tmp_user

try:
    def test_multiply():
        assert tmp_exercise.multiply(1, 999) == tmp_user.multiply(1, 999)
        assert tmp_exercise.multiply(10, 1) == tmp_user.multiply(10, 1)
        assert tmp_exercise.multiply(-15, -15) == tmp_user.multiply(-15, -15)
        assert tmp_exercise.multiply(0, 0) == tmp_user.multiply(0, 0)
        assert tmp_exercise.multiply(-1, 1) == tmp_user.multiply(-1, 1)
except AttributeError:
    pass
