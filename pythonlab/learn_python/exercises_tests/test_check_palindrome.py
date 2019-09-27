from learn_python.temp import tmp_exercise, tmp_user

try:
    def test_multiply():
        assert tmp_exercise.check_palindrome('Dont repeat yourself') == tmp_user.check_palindrome('Dont repeat yourself')
        assert tmp_exercise.check_palindrome('This is New test Case') == tmp_user.check_palindrome('This is New test Case')
        assert tmp_exercise.check_palindrome('x') == tmp_user.check_palindrome('x')
        assert tmp_exercise.check_palindrome('asd.df.gdfg.wge.dsf') == tmp_user.check_palindrome('asd.df.gdfg.wge.dsf')
        assert tmp_exercise.check_palindrome('1 2 3') == tmp_user.check_palindrome('1 2 3')
except AttributeError:
    pass
