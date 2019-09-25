from learn_python.temp import tmp_exercise, tmp_user


try:
    def test_hello():
        assert tmp_user.hello() == tmp_exercise.hello()
except AttributeError:
    pass
