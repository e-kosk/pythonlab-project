from learn_python.temp import tmp_exercise, tmp_user

try:
    def test_add():
        assert tmp_exercise.add(1, 999) == tmp_user.add(1, 999)
        assert tmp_exercise.add(10, 1) == tmp_user.add(10, 1)
        assert tmp_exercise.add(-15, -15) == tmp_user.add(-15, -15)
        assert tmp_exercise.add(0, 0) == tmp_user.add(0, 0)
        assert tmp_exercise.add(-1, 1) == tmp_user.add(-1, 1)
except AttributeError:
    pass
