from ..module_one.models.sql_model import SqlMock
import random 

class TestSqlMock:
    
    x = []
    y = []
     
    for i in range(15):
        x.append(random.randint(0, 30))
        y.append(random.randint(0, 30))

    def test_sql_mock(self):
        mock = SqlMock()
        mock.run_mock(table_name="coordinates", columns=["x", "y"], values=[self.x, self.y])
        values = mock.read_table(table_name="coordinates")

        assert isinstance(mock, SqlMock)
        assert all(isinstance(coords, tuple) for coords in values) 