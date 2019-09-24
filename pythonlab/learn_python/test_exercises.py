import pytest

import tmp_user
import tmp_exercise


try:
    def test_hello():
        assert tmp_user.hello() == tmp_exercise.hello()
except AttributeError:
    pass


try:
    def test_add():
        assert tmp_user.add(1, 999) == tmp_exercise.add(1, 999)
        assert tmp_user.add(10, 1) == tmp_exercise.add(10, 1)
        assert tmp_user.add(-15, -15) == tmp_exercise.add(-15, -15)
        assert tmp_user.add(0, 0) == tmp_exercise.add(0, 0)
        assert tmp_user.add(-1, 1) == tmp_exercise.add(-1, 1)
except AttributeError:
    pass