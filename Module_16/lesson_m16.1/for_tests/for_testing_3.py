from unittest.mock import MagicMock, patch

thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key="value")

thing.method.assert_called_with(3, 4, 5, key="value")


# patch
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)

mock_method.assert_called_once_with(1, 2, 3)


from unittest.mock import patch


@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    module.ClassName1()
    module.ClassName2()
    assert MockClass1 is module.ClassName1
    assert MockClass2 is module.ClassName2

    assert MockClass1.called
    assert MockClass2.called


test()
