# testing_example
Simple test to showcase mocking and its behaviour

Using Python 3, you need to just do:

```python
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests
```

By design you should get one failure to help illustrate what happens when you try to mock with respect to where the code is defined, rather than where you are testing.

