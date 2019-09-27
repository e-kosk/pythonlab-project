from learn_python.temp import tmp_exercise, tmp_user

try:
    def test_multiply():
        assert tmp_exercise.shorten('Dont repeat yourself') == tmp_user.shorten('Dont repeat yourself')
        assert tmp_exercise.shorten('') == tmp_user.shorten('')
        assert tmp_exercise.shorten('x') == tmp_user.shorten('x')
        assert tmp_exercise.shorten('asd.df.gdfg.wge.dsf') == tmp_user.shorten('asd.df.gdfg.wge.dsf')
        assert tmp_exercise.shorten('1 2 3') == tmp_user.shorten('1 2 3')
except AttributeError:
    pass
