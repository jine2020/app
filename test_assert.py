from hamcrest import assert_that, equal_to, close_to, contains_string


class TestAssertDemo:

    def test_hamrest(self):
        # assert_that(4,equal_to(10),'不相等')
        # assert_that(15,close_to(10,2),'不在范围内')
        assert_that('contains some string',contains_string('string1'),'不在里面')

