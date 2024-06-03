from tasks import add

# Send the task to the Celery worker
result = add.delay(4, 2)

# Optionally, wait for the result
# print(result.get(timeout=10))  # Wait for the result and print it
