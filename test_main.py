import unittest
from unittest.mock import patch, MagicMock
from main import generate_response

class TestGenerateResponse(unittest.TestCase):
    @patch('main.aiplatform')
    def test_generate_response(self, mock_aiplatform):
        mock_model = MagicMock()
        mock_model.predict.return_value = "Test response"
        mock_aiplatform.Model.return_value = mock_model
        
        request = MagicMock()
        request.get_json.return_value = {'prompt': 'Test prompt'}
        
        response = generate_response(request)
        self.assertEqual(response, {'response': 'Test response'})

if __name__ == '__main__':
    unittest.main()