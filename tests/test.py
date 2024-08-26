import pytest
from class_Stack import Stack
from function_balanced_chek import balanced_check

stack = Stack()


@pytest.mark.parametrize(
    'a, expected',
    (
            ['(((([{}]))))', 'Balanced'],
            ['[([])((([[[]]])))]{()}', 'Balanced'],
            ['{{[()]}}', 'Balanced'],
            ['}{}', 'Unbalanced'],
            ['{{[(])]}}', 'Unbalanced'],
            ['[[{())}]', 'Unbalanced'],
    )
)
def test_balanced_check(a, expected):
    result = balanced_check(a)
    assert result == expected


