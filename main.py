from locust import HttpUser, TaskSet, task, between

# Define user behavior
class UserBehavior(TaskSet):

    @task(1)  # Simulates the homepage access (GET request)
    def load_homepage(self):
        # Simulate a user opening the platform page
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to load page: {response.status_code}")

# Define the user class that simulates the test
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 10)  # Simulate users waiting between 1 and 5 seconds between tasks
    host = "url"  # Set the host URL here
